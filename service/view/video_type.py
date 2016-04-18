from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from service.serializers import VideoTypeSerializer
from service.models import VideoType
from django.test.client import RequestFactory

def index(request):
	return HttpResponse("Hello Match View")

@csrf_exempt
@api_view(['GET'])
def  get_list(request):
	if request.method == 'GET':
		video_type = VideoType.objects.all()
		serialized = VideoTypeSerializer(video_type, many=True)
		json = JSONRenderer().render(serialized.data)
		return HttpResponse(json);