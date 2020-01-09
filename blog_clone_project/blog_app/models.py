from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.urls import reverse

# Create your models here.


class UserPostModel(models.Model):

    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=264)
    post_text = models.TextField(max_length=264)

    post_creation_date = models.DateTimeField(default=timezone.now)
    post_published_date = models.DateTimeField(blank=True, null=True)

    def publish_post(self):
        self.post_published_date = timezone.now()
        self.save()

    def view_approved_comment(self):
        return self.related_comment_belong.filter(comment_approved=True)

    def get_absolute_url(self):
        return reverse('blog_app:post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.post_title


class UserCommentModel(models.Model):

    comment_belong = models.ForeignKey(UserPostModel, related_name='related_comment_belong', on_delete=models.CASCADE)

    comment_author = models.CharField(max_length=264)
    comment_text = models.TextField(max_length=264)

    comment_creation_date = models.DateTimeField(default=timezone.now)
    comment_approved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blog_app:post_list')

    def comment_approve(self):
        self.comment_approved = True
        self.save()

    def __str__(self):
        return self.comment_text
