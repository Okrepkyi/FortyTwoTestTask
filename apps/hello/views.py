from apps.hello.models import PersonModel
from django.shortcuts import render


def person_view(request):

    data = PersonModel.objects.get(pk=1)
    context = {
    	"person_data": data,
    }
    return render(request, 'home.html', context)