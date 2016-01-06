from django.db import models


class PersonModel(models.Model):

	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	date_of_birth = models.DateField()
	bio = models.CharField(max_length=300)
	jabber = models.CharField(max_length=20)
	email = models.EmailField(max_length=50)
	skype = models.CharField(max_length=50)
	other = models.CharField(max_length=300)