import json

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render

from testalmikeev.forms import ResumeForm
from testalmikeev.models import GoogleTab


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
