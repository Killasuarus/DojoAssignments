# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='oops', max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]