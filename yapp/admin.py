from django.contrib import admin
from .models import Post, Comment, Profile, FeedBackModel, FeedBackReply, Note

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(FeedBackModel)
admin.site.register(FeedBackReply)
admin.site.register(Note)
