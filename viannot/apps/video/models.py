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
	original_publisher = models.CharField(max_length=50)
	original_date = models.DateTimeField()
	description = models.CharField(max_length=500)
	

class Comment(models.Model) :
	author = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=140)
	up = models.IntegerField('upvotes')
	down = models.IntegerField('downvotes')
	x_coord = models.IntegerField()
	y_coord = models.IntegerField()

class Tag(models.Model) :
        tag_name = models.CharField(max_length=50)
        video_tagged = models.ForeignKey(Video)
