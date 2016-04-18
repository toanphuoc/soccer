import json
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from service.models import MatchDetail, Match, VideoType
from service.serializers import MatchDetailSerializer

def  index(request):
	return HttpResponse('Hello Match Detail')

@csrf_exempt
@api_view(['POST'])
def create(request):
	if request.method == 'POST':
		data = request.data
		match_id = data['match_id']
		try:
			match = Match.objects.get(pk=match_id)	
		except Match.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		list_video = data['list_video']
		print(type(list_video))
		object_json = json.loads(list_video)
		for item in object_json:
			type_video = item['type']
			url = item['url']
			try:
				videoType = VideoType.objects.get(pk=type_video)
			except VideoType.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)
			
			match_detail = MatchDetail.objects.create(match=match, video_type=videoType, url=url)
			match_detail.save()
			if match_detail.id < 0:
				return HttpResponse(False)
		return HttpResponse(True, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['GET'])
def get_video_match(request, match_id):
	if request.method == 'GET':
		match_detail = MatchDetail.objects.filter(match=match_id)
		serialized = MatchDetailSerializer(match_detail, many=True)
		json = JSONRenderer().render(serialized.data)
		return HttpResponse(json);