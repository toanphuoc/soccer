from rest_framework import serializers
from service.models import Country

<<<<<<< HEAD
class CountrySerialzer(serializers.Serializer):
=======
class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('id', 'name_country', 'short_name')
>>>>>>> 436f2b66978aa6cd555060d33d610556ecaf605d
