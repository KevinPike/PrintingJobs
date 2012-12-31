from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from jobs.models import Job
from PrintingJobs.forms import JobForm
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import datetime, mimetypes, os
from django.core.servers.basehttp import FileWrapper
from django.conf import settings
from PrintingJobs.settings import SITE_ROOT

def download(request, reference):
    job = Job.objects.get(id=reference)
    job.downloads += 1
    job.save()
    filename = SITE_ROOT + "/media/" + unicode(job.file)
    delimit = unicode(job.file).rsplit('/')
    download_name = delimit[2]
    wrapper = FileWrapper(open(filename))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper, content_type=content_type)
    response["Content-Disposition"] = "attachment; filename=%s"%download_name
    response['Content-Length'] = os.path.getsize(filename)
    return response

def index(request):
    if not request.method == 'GET':
        raise Http404
    if not ('number' in request.GET and 'ref' in request.GET):
	    return render_to_response('JobForm.html')
    form = JobForm(request.GET)
    if not form.is_valid():
        return render_to_response('JobForm.html', {'error' : 'please fill in the fields'})
    try:
        job = Job.objects.get(pk=request.GET['ref'],number=request.GET['number'],
        type=request.GET['type'])
    except Job.DoesNotExist:
         return render_to_response('JobForm.html', {'error' : 'please fill in the fields'})
    #return render_to_response('JobForm.html', {'success': 'yippee', 'file': 'asdf.zip'})
    filename = unicode(job.file).rsplit('/')[2]
    if job.downloads:
        return render_to_response('DownloadForm.html', {'job': job, 'file': filename, 'warning': job.downloads})
    return render_to_response('DownloadForm.html', {'job': job, 'file': filename,'success': 'success'})

def jobRequest(request):
    if not request.method == 'GET':
        raise Http404
    #look for job with current job and ref, if so, return datafile
    #edit JobForm to have download blocks
    #data = {'job': request.GET['job'], 'ref': request.GET['ref'], 'type': request.GET['type']}
    #form = JobForm(data)
    form = JobForm(request.GET)
    if not form.is_valid():
        error = 'The form was not properly filled out, try again.'
        return redirect('/', {'error': error})
    return HttpResponse(form.is_valid())

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
