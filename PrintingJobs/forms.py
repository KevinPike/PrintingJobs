from django import forms
from jobs.models import Job

class JobForm(forms.Form):
    number = forms.CharField(max_length=8)
    id = forms.IntegerField()
    type = forms.ChoiceField(choices=Job.JOB_TYPES)

