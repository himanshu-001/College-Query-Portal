# Generated by Django 2.0.4 on 2018-04-22 10:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='Query Description'),
        ),
    ]