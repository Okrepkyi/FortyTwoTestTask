from apps.hello.models import PersonModel
from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):

	list_display = ["name", "surname", "date", "jabber", "email", "skype", "other"]

admin.site.register(PersonModel, PersonAdmin)