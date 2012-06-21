from django.http import HttpResponse
from jobs.models import Jobs
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def job_request(request):
    job = Jobs.objects.filter(number=jobNumber, id=wedRef)
    return HttpResponse(job)
