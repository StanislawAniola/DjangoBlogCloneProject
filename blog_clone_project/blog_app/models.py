from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.urls import reverse

# Create your models here.


class UserPostModel(models.Model):

    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.TextField()
    post_text = models.TextField()

    post_creation_date = models.DateTimeField(default=timezone.now())
    post_published_date = models.DateTimeField(blank=True, null=True)

    def publish_post(self):
        self.post_published_date = timezone.now()
        self.save()

    def approved_comment(self):
        return self.comment_belong.filter(comment_approved=True)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class UserCommentModel(models.Model):

    comment_belong = models.ForeignKey(UserPostModel, related_name='comment_belong', on_delete=models.CASCADE)

    comment_author = models.CharField()
    comment_text = models.TextField()

    comment_creation_date = models.DateTimeField(default=timezone.now())
    comment_approved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('comment_list')

    def comment_approve(self):
        self.comment_approved = True
        self.save()

    def __str__(self):
        return self.comment_text
