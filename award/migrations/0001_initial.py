# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 12:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('bio', models.TextField()),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=70)),
                ('rating', models.TextField()),
                ('profile', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='award.Profile')),
                ('user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['posted_on'],
            },
        ),
    ]