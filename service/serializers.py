from rest_framework import serializers
from service.models import Country, Club, Tournaments, Match, VideoType, MatchDetail

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('id', 'name_country')

class ClubSerializer(serializers.ModelSerializer):
	country = CountrySerializer()
	class Meta:
		model = Club
		fields = ('id', 'name', 'logo', 'stadium', 'country')

class TournamentsSerializer(serializers.ModelSerializer):
	"""docstring for TournamentsSerializer"""
	country = CountrySerializer()
	class Meta:
		model = Tournaments
		fields  = ('id', 'name', 'logo' ,'country')

class VideoTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = VideoType
		fields = ('id', 'name')

class MatchSerializer(serializers.ModelSerializer):
	# host_club = ClubSerializer(required=True)
	host_club = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
	# guest_club = ClubSerializer(required=True)
	guest_club = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
	tournaments = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
	class Meta:
		model = Match
		fields = ('id', 'host_club', 'guest_club', 'date', 'tournaments')

class MatchDetailSerializer(serializers.ModelSerializer):
	match = MatchSerializer(many=False)
	video_type = VideoTypeSerializer(many=False)

	class Meta:
		model = MatchDetail
		fields = ('id', 'match', 'video_type', 'url')
