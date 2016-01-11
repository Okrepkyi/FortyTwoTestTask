from .models import PersonModel, Request
from django.shortcuts import render


def person_view(request):
    data = PersonModel.objects.get(pk=1)

    context = {
    	"data": data,
    }

    return render(request, "home.html", context)


def view_requests(request):
	request_list = Request.objects.order_by("-date_time")[:10]

	context = {
		"request_list": request_list,
	}

	return render(request, "request_list.html", context)