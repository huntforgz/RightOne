from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User


# Create your models here.
# The search features


class music(models.Model):
	genre = models.CharField(max_length = 30)

class movie(models.Model):
	genre = models.CharField(max_length = 30)

class hobbies(models.Model):
	hobby_name = models.CharField(max_length = 50)

class health(models.Model):
	SMOKE_CHOICE = (
		(0, 'Never smoked'),
		(1, 'Tried smoking'),
		(3, 'Former smoker'),
		(4, 'Current smoker'),
		)
	DRINK_CHOICE =(
		(0, 'Never'),
		(1, 'Social drinker'),
		(2, 'Drink a lot'),
		)
	smoking = models.IntegerField(choices = SMOKE_CHOICE,default = 0)
	drinking = models.IntegerField(choices = DRINK_CHOICE,default = 0)
	health_lifesty = models.IntegerField(default = 0)
	user = models.OneToOneField(User)

	class Meta:
		pass

class spend(models.Model):
	user = models.OneToOneField(User)
	save_all = models.IntegerField(default = 0)
	shopping_center = models.IntegerField(default = 0)
	branded_clothing = models.IntegerField(default = 0)
	partying_socializing = models.IntegerField(default = 0)
	appearance = models.IntegerField(default = 0)
	gadgets = models.IntegerField(default = 0)
	food = models.IntegerField(default = 0)

	class Meta:
		pass

class userfeature(models.Model):
	user = models.OneToOneField(User)
	enjoymusic = models.IntegerField(default = 0)
	musicloved = models.ManyToManyField( music, blank = True, related_name ='lmusic')
	musichated = models.ManyToManyField( music, blank = True, related_name ='hmusic')
	enjoymovie = models.IntegerField(default = 0)
	movieloved = models.ManyToManyField( movie, blank = True, related_name ='lmovie')
	moviehated = models.ManyToManyField( movie, blank = True, related_name ='hmovie')
	hobbies = models.ManyToManyField( hobbies, blank = True)

	class Meta:
		pass
