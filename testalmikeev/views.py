import datetime
import time
from pathlib import Path
import csv

from django.db import connection
from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from testalmikeev.forms import ResumeForm
from testalmikeev.models import FileCsv, GoogleTab, Report
from testalmikeev.servises import get_path_last_file, load_file, db_in_to_data, get_unique_id, save_report


def home(request):
    """ Контроллер стартовой страницы """
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ResumeForm
    return render(request, 'resume.html', {'form': form})


def report_csv(request):
    """  """
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ResumeForm

    print("Загрузка данных из файла .csv")
    start_time = datetime.datetime.now()
    path = get_path_last_file()
    if path:
        list_dict_file = load_file(path)
        finish_time = datetime.datetime.now()
        print("Время выполнения:", finish_time - start_time)
    else:
        return render(request, 'resume.html', {'form': form})

    print("Очистка базы данных.")
    start_time = datetime.datetime.now()
    GoogleTab.objects.all().delete()
    Report.objects.all().delete()
    cur = connection.cursor()
    cur.execute(f'TRUNCATE TABLE testalmikeev_googletab RESTART IDENTITY CASCADE;')
    cur.execute(f'TRUNCATE TABLE testalmikeev_report RESTART IDENTITY CASCADE;')
    print("Запись данных в базу.")
    db_in_to_data(list_dict_file)
    finish_time = datetime.datetime.now()
    print("Время выполнения:", finish_time - start_time)

    print("Получаем список уникальных продуктов")
    unique_id = get_unique_id()
    print(unique_id)

    print("Сохранение отчета в .csv")
    start_time = datetime.datetime.now()
    save_report(unique_id)
    finish_time = datetime.datetime.now()
    print("Время выполнения:", finish_time - start_time)

    # Создаём объект HttpResponse с соответствующим заголовком CSV [1](https://djangodoc.ru/3.2/howto/outputting-csv/)
    response = HttpResponse(content_type='text/csv',
                            headers={'Content-Disposition': 'attachment; filename="report.csv"'})
    writer = csv.writer(response, dialect="excel", delimiter=",")
    summa = Report.objects.all().aggregate(Sum('report'))
    writer.writerow(['', summa.get('report__sum')])
    writer.writerow(['Code', 'Sum'])
    reports = Report.objects.all().values_list('nm_id', 'report')
    writer.writerows(reports)


    return response

    # return render(request, 'resume.html', {'form': form})
