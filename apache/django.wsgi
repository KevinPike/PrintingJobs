import os, sys
sys.path.append('/var/www/PrintingJobs/')
os.environ['DJANGO_SETTING_MODULE'] = 'PrintJobs.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

