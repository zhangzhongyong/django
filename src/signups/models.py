from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
#test
class SignUp(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	#none empty in db, none blank in view
	email = models.EmailField(null=False, blank=False)
	#auto set time stamp when created
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	#set unicode data
	def __unicode__(self):
		#note for user after signups
		return smart_unicode(self.email)