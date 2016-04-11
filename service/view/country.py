from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
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

def create(request):
	pass

@api_view(['GET', 'POST'])
def update(request, country_id, name, short_name):
	# row = Country.update(country_id, name, short_name)
	if request.method == 'POST':
		serializer = CountrySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete(request):
	pass