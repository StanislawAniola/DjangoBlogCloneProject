from django.db import models

from django.urls import reverse
from django.utils import timezone

from group_app import models as group_app_models

# Create your models here.


class PostModel(models.Model):

    post_belong = models.ForeignKey(group_app_models.GroupModel, related_name='post_belong_to_group', on_delete=models.CASCADE)

    post_author = models.TextField(max_length=264)
    post_text = models.TextField(max_length=264)

    post_creation_date = models.DateTimeField(default=timezone.now)
    post_approved = models.BooleanField(default=False)

    def post_approve(self):
        self.post_approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('group_app:group_list')

    def __str__(self):
        return self.post_author





