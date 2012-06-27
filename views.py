from django.core.context_processors import csrf
from django.http import HttpResponse
from jobs.models import Job
from PrintingJobs.forms import JobForm
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

def jobRequest(request):
    if not request.POST:
	return render_to_response('JobForm.html')
    c = {}
    c.update(csrf(request))
    form = JobForm(request.POST)
    if form.is_valid():
            return HttpResponse('valid form')
    return render_to_response('JobForm.html')

def bootstrap(request):
    return render_to_response('base.html')

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def job_request(request):
    job = Jobs.objects.filter(number=jobNumber, id=wedRef)
    return HttpResponse(job)
