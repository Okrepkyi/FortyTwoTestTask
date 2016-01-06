from apps.hello.models import PersonModel
from django.shortcuts import render


def person_view(request):

    data = PersonModel.objects.get(pk=1)
    context = {
    	"context_data": data,
    }
    return render(request, 'hello/home.html', context)