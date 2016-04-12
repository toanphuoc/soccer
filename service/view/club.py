from django.http import HttpResponse
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from service.serializers import ClubSerializer
from service.models import Club, Country

def index(request):
	return HttpResponse("Hello Club View")

def get_list(request):
	club = Club.get_list()
	serialized = ClubSerializer(club, many=True)
	json = JSONRenderer().render(serialized.data)
	return HttpResponse(json);

def get_club_by_id(request, club_id):
	club = Club.objects.get(pk=club_id)
	serialized = ClubSerializer([club, ][0])
	json = JSONRenderer().render(serialized.data)
	return HttpResponse(json)

@csrf_exempt
@api_view(['POST'])
def create(request, format=None):
	if request.method == 'POST':
		country = Country.objects.get(pk=request.data['country'])
		serialized = ClubSerializer(data=request.data)
		if serialized.is_valid():
			serialized.save()
			return Response(serialized.data, status=status.HTTP_201_CREATED)
		return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)