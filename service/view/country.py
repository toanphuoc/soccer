from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from service.models import Country
from service.serializers import CountrySerializer

def index(request):
	return HttpResponse("Hello Country View")

def get_list(request):
	if request.method == 'GET':
		country = Country.get_list()
		serialized = CountrySerializer(country, many=True)
		json = JSONRenderer().render(serialized.data)
		return HttpResponse(json);

def get_country_by_id(request, country_id):
	country = Country.get_country_by_id(country_id)
	serialized = CountrySerializer(country[0])
	json = JSONRenderer().render(serialized.data)
	return HttpResponse(json);

@api_view(['GET', 'POST', 'PUT'])
def update(request, country_id, format=None):
	try:
		country = Country.objects.get(pk=country_id)
	except Country.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = CountrySerializer(country, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, country_id):
	try:
		country = Country.objects.get(pk=country_id)
	except Country.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if(request.method == 'DELETE'):
		country.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def create(request, format=None):
	# row = Country.update(country_id, name, short_name)
	if request.method == 'POST':
		serializer = CountrySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(request):
	pass