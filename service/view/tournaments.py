from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from service.models import Tournaments
from service.serializers import TournamentsSerializer

def index(request):
	return HttpResponse('Hello Tournaments')

@csrf_exempt
def get_list(request):
	if request.method == 'GET':
		tournaments = Tournaments.objects.all()
		serialized = TournamentsSerializer(tournaments, many=True)
		json = JSONRenderer().render(serialized.data)
		return HttpResponse(json);

@csrf_exempt
@api_view(['POST'])
def create(request, format=None):
	if request.method == 'POST':
		serializer = TournamentsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def get_all_tournaments_in_country(request, country_id):
	if request.method == 'GET':
		tournaments = Tournaments.objects.filter(country=country_id)
		serializer = TournamentsSerializer(tournaments, many=True)
		json = JSONRenderer().render(serializer.data)
		return HttpResponse(json)

