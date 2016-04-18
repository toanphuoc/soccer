from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from service.models import Match, Club, Tournaments
from service.serializers import MatchSerializer

def index(request):
	return HttpResponse("Hello Match View")

@csrf_exempt
@api_view(['POST'])
def create(request, *args, **kwargs):
	if request.method == 'POST':
		data = request.data
		try:
			host_club = Club.objects.get(pk=data['host_club'])
		except Club.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		try:
			guest_club = Club.objects.get(pk=data['guest_club'])
		except Club.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		
		try:
			tournament = Tournaments.objects.get(pk=data['tournament'])
		except Tournaments.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		match = Match.objects.create(host_club=host_club, guest_club=guest_club, tournaments=tournament, ulr_video=data['ulr_video'], date=data['date'])
		match.save()
		if match.id > 0:
			return Response(True, status=status.HTTP_201_CREATED)
		return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def get_list(request):
	if request.method =='GET':
		match = Match.objects.all()
		serialized = MatchSerializer(match, many=True)
		json = JSONRenderer().render(serialized.data)
		return HttpResponse(json);


@csrf_exempt
@api_view(['GET'])
def get_match_today(request):
	if request.method == 'GET':
		match = Match.objects.filter(date=datetime.now().date())
		serialized = MatchSerializer(match, many=True)
		json = JSONRenderer().render(serialized.data)
		return HttpResponse(json);

@csrf_exempt
@api_view(['GET'])
def get_match_by_tournament(request, tournament_id):
	if request.method == 'GET':
		match = Match.objects.filter(tournaments=tournament_id)
		serialized = MatchSerializer(match, many=True)
		json = JSONRenderer().render(serialized.data)
		return HttpResponse(json);