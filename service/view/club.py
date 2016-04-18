from django.http import HttpResponse
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from service.serializers import ClubSerializer, CountrySerializer
from service.models import Club, Country
from django.test.client import RequestFactory


context = dict(request=RequestFactory().get('/'))

def index(request):
	return HttpResponse("Hello Club View")

def get_list(request):
	club = Club.get_list()
	serialized = ClubSerializer(club, context=context, many=True)
	json = JSONRenderer().render(serialized.data)
	return HttpResponse(json);

def get_club_by_id(request, club_id):
	club = Club.objects.get(pk=club_id)
	serialized = ClubSerializer([club, ][0])
	json = JSONRenderer().render(serialized.data)
	return HttpResponse(json)

@csrf_exempt
@api_view(['POST'])
def create(request, *args, **kwargs):
	if request.method == 'POST':
		data = request.data
		try:
			country = Country.objects.get(pk=data['country'])
		except Club.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		club = Club.objects.create(name=data['name'], stadium=data['stadium'], logo=data['logo'], country=country)
		club.save()
		if club.id > 0:
			return Response('Create success', status=status.HTTP_201_CREATED)
		return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
