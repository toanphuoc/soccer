from django.db import models
import json
import os
# Create your models here.

class Status(object):
	status = False
	msg = ''

	def __init__(self, status, msg):
		self.status = status
		self.msg = msg

	def parse_json(self):
		return json.dumps(self.__dict__)

class Country(models.Model):
	name_country  = models.CharField(max_length=200)
	short_name = models.CharField(max_length=20)

	class Meta:
		ordering = ['name_country']
		unique_together = (('name_country'), ('short_name'),)

	def __str__(self):
	 	return self.short_name

	def get_list():
		return Country.objects.all()

	def get_country_by_id(country_id):
		data = Country.objects.get(pk=country_id)
		return [data,]

class Club(models.Model):
	"""docstring for Club"""
	name = models.CharField(max_length=100)
	country = models.ForeignKey(Country, related_name='clubs')
	stadium = models.CharField(max_length=100, null=False, blank=True)
	logo = models.TextField(null=True)

	class Meta:
		unique_together = (('name'), )

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.country.name_country

	def get_list():
		return Club.objects.all()

	def validate_logo_type(path_file):
		file_types = ['.png', '.jpg', '.gif', '.tiff', '.jpeg', '.bmp']
		fileName, fileExtension = os.path.splitext(path_file);
		for file_type in file_types:
			if fileExtension.lower() == file_type.lower():
				return True;
		return False

	def validate_logo_size(file_name):
		try:
			file_size = os.path.getsize(file_name)
		except:
			file_size = os.stat(file_name).st_size 
		
		if file_size / 1024 < 1024:
			return True
		return False

class Position(models.Model):
	"""docstring for Position"""
	short_name = models.CharField(max_length=20)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.short_name
		

class Player(models.Model):
	name = models.CharField(max_length=200)
	club = models.ForeignKey(Club, on_delete=models.CASCADE)
	position = models.ForeignKey(Position, on_delete=models.CASCADE)
	number_player = models.IntegerField
	age = models.IntegerField

	def __str__(self):
		return self.name

class Tournaments(models.Model):
	name = models.CharField(max_length=200, null=False)
	country = models.ForeignKey(Country, null=True)
	logo = models.TextField(null=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class VideoType(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Match(models.Model):
	host_club = models.ForeignKey(Club, on_delete=models.CASCADE, null=False, related_name='host_club')
	guest_club = models.ForeignKey(Club, on_delete=models.CASCADE, null=False, related_name='guest_club')
	date = models.DateTimeField()
	thumnail = models.URLField(max_length=200, default='')
	tournaments = models.ForeignKey(Tournaments, null=True, related_name='tournaments')


	def __str__(self):
		return '%s - %s' % (self.host_club, self.guest_club)
	class Meta:
		ordering = ['-date']

class MatchDetail(models.Model):
	match = models.ForeignKey(Match, related_name='matchs')
	video_type = models.ForeignKey(VideoType, on_delete=models.CASCADE)
	url = models.CharField(max_length=500)

	def __str__(self):
		return self.url

	class Meta:
		ordering = ['video_type']






		
