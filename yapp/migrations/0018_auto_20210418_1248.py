# Generated by Django 3.1.5 on 2021-04-18 07:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yapp', '0017_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]