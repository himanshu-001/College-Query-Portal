# Generated by Django 2.0.4 on 2018-04-22 11:01

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_auto_20180422_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Query Description'),
        ),
    ]