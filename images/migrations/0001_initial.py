# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=False, db_index=True)),
                ('order', models.PositiveIntegerField(default=0, blank=True)),
                ('title', models.CharField(max_length=1024, blank=True)),
                ('alt', models.CharField(max_length=1024, blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('file', models.ImageField(max_length=1024, null=True, upload_to=b'images/', blank=True)),
                ('_url', models.CharField(max_length=1024, verbose_name=b'url', blank=True)),
                ('caption', models.TextField(default=b'', blank=True)),
                ('is_icon', models.BooleanField(default=False)),
                ('is_listing', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Attached Image',
                'verbose_name_plural': 'Attachable Images',
            },
            bases=(models.Model,),
        ),
    ]
