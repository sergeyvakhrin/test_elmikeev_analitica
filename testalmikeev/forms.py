from django import forms

from testalmikeev.models import FileCsv


class ResumeForm(forms.ModelForm):

   class Meta:
      model = FileCsv
      fields = ['file']