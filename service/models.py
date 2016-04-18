from django.db import models

# Create your models here.

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

class Match(models.Model):
	host_club = models.ForeignKey(Club, on_delete=models.CASCADE, null=False, related_name='host_club')
	guest_club = models.ForeignKey(Club, on_delete=models.CASCADE, null=False, related_name='guest_club')
	ulr_video = models.CharField(max_length=200, null=False)
	date = models.DateTimeField()
	tournaments = models.ForeignKey(Tournaments, null=True, related_name='tournaments')

	class Meta:
		ordering = ['-date']




		