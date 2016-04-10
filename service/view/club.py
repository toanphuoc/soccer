from django.http import HttpResponse
from django.core import serializers
from service.models import Club

def index(request):
	return HttpResponse("Hello Club View")

def get_list(request):
	club = Club.get_list()
	data = serializers.serialize("json", club)
	return HttpResponse(data)