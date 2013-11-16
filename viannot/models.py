from django.db import models

# Create your models here.

class User(models.Model) :
	name = models.CharField(max_length=30)
	date = 

class Video(models.Model) :
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	publisher = models.ForeignKey(User)