# Generated by Django 2.0.5 on 2018-05-19 18:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0021_auto_20180422_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Leave a Comment :'),
        ),
    ]