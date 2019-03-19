# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Project')),
            ],
        ),
        migrations.CreateModel(
            name='DesignRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Project')),
            ],
        ),
        migrations.CreateModel(
            name='UsabilityRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Project')),
            ],
        ),
    ]