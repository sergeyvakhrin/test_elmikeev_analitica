from django.urls import path

from testalmikeev.apps import TestalmikeevConfig
from testalmikeev.views import home, report_csv

app_name = TestalmikeevConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('report/', report_csv, name='report_csv')
]