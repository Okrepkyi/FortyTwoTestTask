from django.db import models


class PersonModel(models.Model):

	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	date = models.DateField(verbose_name="Date of birth")
	bio = models.CharField(max_length=300)
	jabber = models.CharField(max_length=20)
	email = models.EmailField(max_length=50)
	skype = models.CharField(max_length=50)
	other = models.CharField(max_length=300)

	def __str__(self):
		return self.name


class HttpRequests(models.Model):

	date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
	method = models.CharField(max_length=10)
	uri = models.CharField(max_length=100)
	protocol = models.CharField(max_length=10)
	status_code = models.IntegerField(max_length=3)
	content_length = models.IntegerField(max_length=10)