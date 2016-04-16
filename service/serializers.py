from rest_framework import serializers
from service.models import Country, Club, Tournaments

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('id', 'name_country', 'short_name')

class ClubSerializer(serializers.ModelSerializer):
	country = CountrySerializer(required=True)
	class Meta:
		model = Club
		fields = ('id', 'name', 'country')

class TournamentsSerializer(serializers.ModelSerializer):
	"""docstring for TournamentsSerializer"""
	class Meta:
		model = Tournaments
		fields  = ('id', 'name', 'country')
		
		
