from apps.hello.models import PersonModel
from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):

	list_display = ["name", "surname", "date", "jabber", "email", "skype"]

admin.site.register(PersonModel, PersonAdmin)