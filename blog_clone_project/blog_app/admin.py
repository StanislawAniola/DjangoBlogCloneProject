from django.contrib import admin
from blog_app import models

# Register your models here.


admin.site.register(models.UserPostModel)
admin.site.register(models.UserCommentModel)
