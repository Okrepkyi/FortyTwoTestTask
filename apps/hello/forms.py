from .models import PersonModel
from django import forms


class PersonForm(forms.ModelForm):

	class Meta:
		model = PersonModel
		fields = '__all__'
