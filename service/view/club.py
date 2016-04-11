from django.http import HttpResponse
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from service.serializers import ClubSerializer
from service.models import Club

def index(request):
	return HttpResponse("Hello Club View")

def get_list(request):
	club = Club.get_list()
	serialized = ClubSerializer(club, many=True)
	json = JSONRenderer().render(serialized.data)
	return HttpResponse(json);