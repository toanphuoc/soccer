from django.http import HttpResponse
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from service.serializers import ClubSerializer, CountrySerializer, StatusSerializer
from service.models import Club, Country, Status
from django.test.client import RequestFactory
import base64
import os
import json

context = dict(request=RequestFactory().get('/'))

def index(request):
	return HttpResponse("Hello Club View")

@api_view(['GET'])
def get_list(request):
	club = Club.get_list()
	serialized = ClubSerializer(club, context=context, many=True)
	json = JSONRenderer().render(serialized.data)
	return HttpResponse(json);

@api_view(['GET'])
def get_club_by_id(request, club_id):
	try:
		club = Club.objects.get(pk=club_id)
	except Club.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serialized = ClubSerializer([club, ][0])
	json = JSONRenderer().render(serialized.data)
	return HttpResponse(json)

@csrf_exempt
@api_view(['POST'])
def create(request, *args, **kwargs):
	if request.method == 'POST':
		status = Status(status=False, msg='')
		data = request.data
		try:
			country = Country.objects.get(pk=data['country'])
		except Club.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		logo_file = request.FILES['logo']

		name = logo_file.name
		logo_folder = 'logo_folder'
		file_name = logo_folder + '/' + name

		if not os.path.exists(logo_folder):
			os.makedirs(logo_folder)

		#save file to logo_folder folder
		des = open(file_name, 'wb+')
		for chunk in logo_file.chunks():
			des.write(chunk)
			des.close()

		#validate image file type in here
		validate_file_type = Club.validate_logo_type(file_name)
		if validate_file_type == False:
			os.remove(file_name);
			status.msg = 'File type is not support'
			return HttpResponse(status.parse_json(), content_type='application/json')

		#validate image file size in here
		validate_file_size = Club.validate_logo_size(file_name)
		if validate_file_size == False:
			os.remove(file_name);
			status.msg = 'File size is not gather than 1M'
			return HttpResponse(status.parse_json(), content_type='application/json')

		#encode file to base64 
		with open(file_name, "rb") as img:
			encode_string = base64.b64encode(img.read())

		os.remove(file_name);

		#save object club
		club = Club.objects.create(name=data['name'], stadium=data['stadium'], logo=encode_string, country=country)
		
		# img_data = base64.b64decode(encode_string)
		# file_name = 'temp.png' 
		# with open(file_name, 'wb') as f:
		# 	f.write(img_data)
		if club.id > 0:
			status.status = True
			status.msg = 'Success'
			return HttpResponse(status.parse_json(), content_type='application/json')
		return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
