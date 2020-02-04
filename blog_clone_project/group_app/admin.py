from django.contrib import admin
from group_app import models

# Register your models here.


class GroupModelAdmin(admin.ModelAdmin):

    def group_post_count(self, obj):
        return obj.post_belong_to_group.count()

    fields = ['group_title', 'group_author', 'group_description', 'group_creation_date', 'group_published_date']

    search_fields = ['group_title', 'group_author']

    list_filter = ['group_title', 'group_author', 'group_creation_date', 'group_published_date']

    list_display = ['group_title', 'group_author', 'group_creation_date', 'group_published_date', 'group_post_count']


admin.site.register(models.GroupModel, GroupModelAdmin)
