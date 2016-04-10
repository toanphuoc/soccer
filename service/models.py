from django.db import models

# Create your models here.

class Country(models.Model):
	name  = models.CharField(max_length=200)
	short_name = models.CharField(max_length=20)

	def __str__(self):
		return self.short_name


class Club(models.Model):
	"""docstring for Club"""
	name = models.CharField(max_length=100)
	country = models.ForeignKey(Country, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

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
		