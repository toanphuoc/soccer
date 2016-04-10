from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from service.models import Country

def index(request):
	return HttpResponse("Hello Country View")

def get_list(request):
	country = Country.get_list()
	data = serializers.serialize("json", country, fields=('name', 'short_name'))
	return HttpResponse(data)

def get_country_by_id(request, country_id):
	country = Country.get_country_by_id(country_id)
	data = serializers.serialize("json", country)
	data = data.strip("[]")
	return HttpResponse(data)

def create(request):
	pass

def update(request, country_id, name, short_name):
	pass

def delete(request):
	pass