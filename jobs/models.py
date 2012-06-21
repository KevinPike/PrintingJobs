from django.db import models

# Create your models here.

class Job (models.Model) :
	number = models.CharField('Job Number', max_length=8)
	title = models.CharField('Job Title', max_length=20)
	#description = models.CharField(max_length=200)
	# true is lc, false is hs
	JOB_TYPES = (
			('LC', 'Lettercomm Services'),
			('HS', 'Harris Services'),
	)
	type = models.CharField('Job Type', max_length=2, choices=JOB_TYPES, )
	file = models.FileField('Upload File', upload_to='/home/kevin/Videos')
	
	def __unicode__(self):
		return self.title + ('%i', self.number)
	
