# Generated by Django 3.0.7 on 2020-10-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='credito',
            field=models.IntegerField(default=20),
        ),
    ]
