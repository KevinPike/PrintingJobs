from jobs.models import Job
from django.contrib import admin

class JobAdmin(admin.ModelAdmin):
	list_display = ('id', 'number', 'title', 'type', 'file', 'downloads')
	search_fields = ('number', 'title')
	list_filter = ('id', 'number')

admin.site.register(Job, JobAdmin)
