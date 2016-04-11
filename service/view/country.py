from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from service.models import Country
from service.serializers import CountrySerializer

def index(request):
	return HttpResponse("Hello Country View")

def get_list(request):
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

def update(request, country_id, name, short_name):
	pass

def delete(request):
	pass