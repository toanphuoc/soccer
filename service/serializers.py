from rest_framework import serializers
from service.models import Country, Club

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('id', 'name_country', 'short_name')

class ClubSerializer(serializers.ModelSerializer):
	country = CountrySerializer()
	class Meta:
		model = Club
		fields = ('id', 'name', 'country')