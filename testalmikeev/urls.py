from django.urls import path

from testalmikeev.apps import TestalmikeevConfig
from testalmikeev.views import home

app_name = TestalmikeevConfig.name

urlpatterns = [
    path('', home, name='home'),
]