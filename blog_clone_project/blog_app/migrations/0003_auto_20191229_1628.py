# Generated by Django 2.2.3 on 2019-12-29 15:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20191229_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercommentmodel',
            name='comment_creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userpostmodel',
            name='post_creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]