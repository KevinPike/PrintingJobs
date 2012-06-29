from django import forms
from jobs.models import Job

class JobForm(forms.Form):
    number = forms.IntegerField()
    ref = forms.IntegerField()
    type = forms.ChoiceField(choices=Job.JOB_TYPES)

