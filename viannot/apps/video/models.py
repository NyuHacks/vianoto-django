from django.db import models

 
class User(models.Model) :
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	pswd = 

class Video(models.Model) :
	title = models.CharField(max_length=140)
	url = models.CharField(max_length=200)
	publisher = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	up = models.IntegerField('upvotes')
	down = models.IntegerField('downvotes')

class Comment(models.Model) :
	author = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=140)
	up = models.IntegerField('upvotes')
	down = models.IntegerField('downvotes')