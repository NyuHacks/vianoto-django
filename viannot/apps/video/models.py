from django.db import models
from django.contrib.auth.models import User

class Video(models.Model) :
	title = models.CharField(max_length=140)
	url = models.CharField(max_length=200)
	publisher = models.ForeignKey(User)
	time = models.DateTimeField(auto_now_add=True)
	up = models.IntegerField('upvotes')
	down = models.IntegerField('downvotes')
	original_publisher = models.CharField(max_length=50)
	original_date = models.DateTimeField()
	description = models.CharField(max_length=500)

class Comment(models.Model) :
	author = models.ForeignKey(User)
	time = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=140)
	videotime = models.IntegerField('seconds')
	x = models.IntegerField('x coordinate')
	y = models.IntegerField('y coordinates')
	up = models.IntegerField('upvotes')
	down = models.IntegerField('downvotes')

class Reply(models.Model)
	comment = models.ForeignKey(Comment)
	author = models.ForeignKey(User)
	time = models.DateTimeField(auto_now_add=True)

class Tag(models.Model) :
    tag_name = models.CharField(max_length=50)
    video_tagged = models.ForeignKey(Video)