from rest_framework import serializers
from service.models import Country

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('id', 'name_country', 'short_name')
