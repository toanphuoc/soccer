from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Country

# Create your views here.

def index(request):
	return HttpResponse("Hello Toan")
