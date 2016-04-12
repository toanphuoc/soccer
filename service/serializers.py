from rest_framework import serializers
from service.models import Country, Club

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('id', 'name_country', 'short_name')

	def create(self, validated_data):
		return Country.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name_country = validated_data.get('name_country', instance.name_country)
		instance.short_name = validated_data.get('short_name', instance.short_name)
		instance.save()
		return instance

class ClubSerializer(serializers.ModelSerializer):
	country = CountrySerializer()
	class Meta:
		model = Club
		fields = ('id', 'name', 'country')