from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    #body = models.TextField(null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    second_image = models.ImageField(null=True, blank=True)
    #likes = models.ManyToManyField(User, related_name='blog_like')

    def __str__(self):
        return self.title


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
	body = RichTextField(null=True, blank=True)
	date = models.DateField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return str(self.user)

class Profile(models.Model):
    #ForeignKey is also known as OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    body = RichTextField(null=True, blank=True)

    def __str__(self):
        #Always make self.user a string value, if wanna return it
        return str(self.user)

class FeedBackModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=200)
    complaint = RichTextField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class FeedBackReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(FeedBackModel, related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    complaint = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=250)
    body = RichTextField()
    
    def __str__(self):
        return str(self.user)

