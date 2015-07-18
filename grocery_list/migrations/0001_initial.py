# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'pink', max_length=50)),
                ('fontcolor', models.CharField(default=b'green', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.TextField()),
                ('remarks', models.TextField(blank=True)),
                ('cat', models.ManyToManyField(related_name='grocery_list', null=True, to='grocery_list.Cat', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
