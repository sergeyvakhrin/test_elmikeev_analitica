import time
from pathlib import Path
import os

import psycopg2
from django.db import connection
from django.db.models import Sum

from testalmikeev.models import GoogleTab, FileCsv, Report


def get_path_last_file():
    """  """
    path = FileCsv.objects.order_by('id').last()
    if path:
        path = str(path.file)
        path = path.split('/')
        ROOT_PATH = Path(__file__).parent.parent
        FILE_PATH = ROOT_PATH.joinpath('media', *path)
        return FILE_PATH


def validate_line(line):
    """ Валидация на дробные числа в поле total_price, Замена , на . """
    a = 0
    index = -1
    data = list(line)
    for l in data:
        index += 1
        if a == 2:
            a = 0
            continue
        if l == ',' and a == 1:
            data[index] = '.'
            continue
        if l == '"':
            a += 1
    line = ''.join(data)
    line = line.replace('"', '')
    return line


def load_file(path):
    """ Загрузка данных из файла csv """
    head = ['date', 'last_change_date', 'total_price', 'discount_percent', 'warehouse_name', 'oblast', 'nm_id',
            'category', 'brand', 'is_cancel', 'cancel_dt', 'created_at', 'updated_at', 'order_type']
    with open(path, 'r', encoding='utf-8') as f:
        obj_list = []

        for line in f:
            if '"' in line:
                line = validate_line(line)

            obj = line.split(',')
            if obj[0] == 'date':
                continue

            date, _ = obj[0].split(' ')
            _, obj_month, _ = date.split('.')
            if obj_month != '01':
                continue

            obj[-1] = obj[-1][:-1]

            obj_list.append(dict(zip(head, obj)))
    return obj_list

def db_in_to_data(obj_list):
    """ Заполняем базу данных """
    list_for_create = []
    for obj in obj_list:
        list_for_create.append(GoogleTab(**obj))

    GoogleTab.objects.bulk_create(list_for_create)


def get_unique_id():
    """ Делаем запрос к базе данных по ТЗ """
    cur = connection.cursor()
    cur.execute('SELECT DISTINCT nm_id, SUM(total_price)/2 FROM testalmikeev_googletab GROUP BY nm_id;')
    list_unique = cur.fetchall()

    # list_unique = GoogleTab.objects.order_by('nm_id').distinct('nm_id')
    # list_unique = [unique.nm_id for unique in list_unique]
    # for unique in list_unique:
    #     obj = GoogleTab.objects.filter(nm_id=unique).aggregate(Sum('total_price'))
    #     print(obj)

    return list_unique


def save_report(unique_id):
    """ Сохраняем результат в .csv и в базу """
    with open('report.csv', 'w', encoding='utf-8') as file:
        summa = 0
        for obj in unique_id:
            summa += obj[1]
        file.write(f',{summa}\n')
        file.write('Артикул,Сумма\n')
        for_report_bulk = []
        for obj in unique_id:
            file.write(f'{obj[0]},{obj[1]}\n')
            for_report_bulk.append(Report(nm_id=obj[0], report=obj[1]))
        Report.objects.bulk_create(for_report_bulk)
