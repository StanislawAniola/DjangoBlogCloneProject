# Generated by Django 2.2.9 on 2020-02-03 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupmodel',
            old_name='group_auth',
            new_name='group_author',
        ),
    ]
