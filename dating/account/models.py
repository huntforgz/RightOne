from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import os
AVATAR_ROOT = 'avatar'
AVATAR_DEFAULT = os.path.join(AVATAR_ROOT, 'default.jpeg')
class Profile(models.Model):
	# user = models.OneToOneField(settings.AUTH_USER_MODEL)
	# date_of_birth = models.DateField(blank=True, null=True)
	# photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	# def __str__(self):
	# 	return 'Profile for user {}'.format(self.user.username)
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	nickname = models.CharField(max_length = 50,blank = True)
	intro = models.TextField(max_length = 500, blank = True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', default = AVATAR_DEFAULT,blank = True)
	# GENDER = {
    #
	# 'F':'female',
	# 'M':'male',
    #
	# }
	GENDER = (

	('F','female'),
	('M','male'),

	)

	EDUCATION =(
		(0, 'currently a primary school pupil'),
		(1, 'primary school'),
		(2, 'secondary school'),
		(3, 'college/bachelor degree'),
		(4, 'masters degree'),
		(5, 'doctorate degree')
		)

	# age = models.IntegerField(default = 0)
	# height = models.IntegerField(default = 0)
	# weight = models.IntegerField(default = 0)
	# gender = models.CharField(max_length = 1, choices = GENDER,default = '')
	# education = models.IntegerField(choices = EDUCATION,default = 0)
	# only_child = models.BooleanField(blank = True,default = True)
	# location = models.CharField(max_length = 2,default = '')
	age = models.IntegerField()
	height = models.IntegerField(blank = True)
	weight = models.IntegerField(blank = True)
	gender = models.CharField(max_length = 1, choices = GENDER,blank = True)
	education = models.IntegerField(choices = EDUCATION,blank = True)
	only_child = models.BooleanField(blank = True)
	location = models.CharField(max_length = 2,blank = True)



	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)
# User.profile = property(lambda u:Profile.objects.get_or_create(user=u)[0])
# 	@models.permalink
# 	def get_absolute_url(self):
# 		return 'sp_profile_other_view_page', [self.user.username]
#
#
#
# def create_user_profile(sender, instance, created, **kwargs):
#     """Creates a UserProfile Object Whenever a User Object is Created"""
#     if created:
#         Profile.objects.create(user=instance)
#
#
# post_save.connect(create_user_profile, sender=User)


def create_user_profile(sender, instance, created, **kwargs):
    """Creates a UserProfile Object Whenever a User Object is Created"""
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
