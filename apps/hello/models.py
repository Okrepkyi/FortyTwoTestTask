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
	photo = models.ImageField(upload_to="photo", blank=True)

	def __str__(self):
		return self.name


class Request(models.Model):

	date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
	request_method = models.CharField(max_length=10)
	uri = models.CharField(max_length=10)
	server_protocol = models.CharField(max_length=10)
	status_code = models.IntegerField()
	content_length = models.IntegerField()

	class Meta:
		ordering = ['date_time']