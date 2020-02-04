from django.contrib import admin
from post_app import models

# Register your models here.


class PostModelAdmin(admin.ModelAdmin):

    def group_post_count(self, obj):
        return obj.post_belong_to_group.count()

    fields = ['post_author', 'post_belong', 'post_text', 'post_creation_date', 'post_approved']

    search_fields = ['post_belong', 'post_author']

    list_filter = ['post_belong', 'post_creation_date', 'post_approved']

    list_editable = ['post_approved']

    list_display = ['post_author', 'post_belong', 'post_creation_date', 'post_approved']


admin.site.register(models.PostModel, PostModelAdmin)
