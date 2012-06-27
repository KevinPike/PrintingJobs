from django.db import models
import os

# Create your models here.

class Job (models.Model) :
	number = models.CharField('Job Number', max_length=8)
	id = models.AutoField('Reference Number', primary_key=True) 
	title = models.CharField('Job Title', max_length=20)
	#description = models.CharField(max_length=200)
	# true is lc, false is hs
	JOB_TYPES = (
			('LC', 'Lettercomm Services'),
			('HS', 'Harris Services'),
	)
	type = models.CharField('Job Type', max_length=2, choices=JOB_TYPES, )
	file = models.FileField('Upload File', upload_to='media')
	#need to add completed file
	def __unicode__(self):
		return 'J#:' + self.number + ' R#' + unicode(self.id) + ' ' + self.type
