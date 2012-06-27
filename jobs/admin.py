from jobs.models import Job
from django.contrib import admin

class JobAdmin(admin.ModelAdmin):
	list_display = ('number', 'id', 'title', 'type', 'file')
	search_fields = ('number', 'title')
	list_filter = ('id', 'number')

admin.site.register(Job, JobAdmin)
