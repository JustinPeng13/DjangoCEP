# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0003_auto_20150713_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'purple', max_length=50)),
                ('fontcolor', models.CharField(default=b'white', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'red', max_length=50)),
                ('fontcolor', models.CharField(default=b'black', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='item',
            name='folder',
            field=models.ForeignKey(related_name='notes', blank=True, to='grocery_list.Folder', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.ManyToManyField(related_name='notes', null=True, to='grocery_list.Tag', blank=True),
            preserve_default=True,
        ),
    ]
