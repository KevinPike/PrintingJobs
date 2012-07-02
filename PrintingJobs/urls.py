from django.conf.urls import patterns, include, url
from views import hello, current_datetime, jobRequest, bootstrap, index, download
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PrintingJobs.views.home', name='home'),
    # url(r'^PrintingJobs/', include('PrintingJobs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
    url('^time/$', current_datetime),
    url('^$', index),
    url('^base/$', bootstrap),
    url('^search/$', jobRequest),
    url('^download/(\d{1,})/$', download),
)
