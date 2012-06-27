from bootstrap.forms import BootstrapForm, Fieldset
from jobs.models import Job
from django import forms 

class JobForm(BootstrapForm):
    class Meta:
        layout = (
            Fieldset("Please enter job information", "job_number", "reference_number", "job_type", ),
        )

    job_number = forms.CharField(max_length=8)
    reference_number = forms.IntegerField()
    job_type = forms.ChoiceField(choices=Job.JOB_TYPES)
   
