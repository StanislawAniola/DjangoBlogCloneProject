from django.db import models

from django.utils import timezone
from django.urls import reverse

from django.contrib.auth import get_user_model
user_current = get_user_model()

# Create your models here.


class GroupModel(models.Model):

    group_auth = models.ForeignKey(user_current, on_delete=models.CASCADE)

    group_title = models.TextField(max_length=264)
    group_description = models.TextField(max_length=264)

    group_creation_date = models.DateTimeField(default=timezone.now)
    group_published_date = models.DateTimeField(blank=True, null=True)

    def publish_group(self):
        self.group_published_date = timezone.now()
        self.save()

    def view_approved_comment(self):
        return self.post_belong_to_group.filter(post_approved=True)

    def get_absolute_url(self):
        return reverse('group_app:group_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.group_title
