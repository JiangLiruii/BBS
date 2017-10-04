from django.db import models

# Create your models here.
class User_type(models.Model):
	display = models.CharField(max_length=50)
	def __str__(self):return self.display

class Admin(models.Model):
	user = models.CharField(max_length=50)
	password = models.CharField(max_length=256)
	# creat_date = models.DateTimeField(auto_now_add="True")
	email = models.EmailField()
	user_type = models.ForeignKey('User_type')

	def __str__(self): return self.user


class Chat(models.Model):
	content = models.CharField(max_length=512)
	user = models.ForeignKey('Admin')
	creat_date = models.DateTimeField(auto_now_add="True")
	def __str__(self):return self.content

class NewsType(models.Model):
	display = models.CharField(max_length=32)
	def __str__(self):return self.display

class News(models.Model):
	title = models.CharField(max_length=32)
	user = models.ForeignKey('Admin')
	summary = models.CharField(max_length=256)
	url = models.URLField()
	news_type = models.ForeignKey('NewsType')
	favor_count = models.IntegerField(default=0)
	reply_count = models.IntegerField(default=0)
	create_date = models.DateTimeField(auto_now_add="True")
	def __str__(self):return self.title


class Reply(models.Model):
	content = models.TextField()
	news = models.ForeignKey('News')
	user = models.ForeignKey('Admin')
	create_date = models.DateTimeField(auto_now_add="True")
	def __str__(self):return self.content