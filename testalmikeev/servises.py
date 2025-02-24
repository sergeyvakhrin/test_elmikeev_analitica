import time
from pathlib import Path
import os
import csv

import psycopg2
from django.db import connection
from django.db.models import Sum

from testalmikeev.models import GoogleTab, FileCsv, Report
from users.models import User


def createsuperuserone():
    """  """
    user = User.objects.create(
        email='admin@sky.pro',
        first_name='Admin',
        last_name='SkyPro',
        is_staff=True,
        is_superuser=True,
        is_active=True,
    )
    user.set_password('1234')
    user.save()


def get_path_last_file():
    """  """
    path = FileCsv.objects.order_by('id').last()
    if path:
        path = str(path.file)
        path = path.split('/')
        ROOT_PATH = Path(__file__).parent.parent
        FILE_PATH = ROOT_PATH.joinpath('media', *path)
        return FILE_PATH


def load_file(path):
    """ Загрузка данных из файла csv """
    with open(path, 'r', encoding='utf-8') as file:
        obj_list = []
        reader_dict = csv.DictReader(file, delimiter=',')
        for obj in reader_dict:
            obj['total_price'] = obj['total_price'].replace(',', '.')
            date, _ = obj.get('date').split(' ')
            _, obj_month, _ = date.split('.')
            if obj_month != '01':
                continue
            obj_list.append(obj)
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
    unique_id_for_csv = unique_id.copy()
    summa = 0
    for obj in unique_id_for_csv:
        summa += obj[1]
    unique_id_for_csv.insert(0, ('',summa))
    unique_id_for_csv.insert(1,('Артикул', 'Сумма'))

    with open('report.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(unique_id_for_csv)

        print("Сохранение отчета базу данных.", end=' ')
        for_report_bulk = []
        for obj in unique_id:
            for_report_bulk.append(Report(nm_id=obj[0], report=obj[1]))
        Report.objects.bulk_create(for_report_bulk)
