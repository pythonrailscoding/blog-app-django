# Generated by Django 3.1.5 on 2021-04-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
