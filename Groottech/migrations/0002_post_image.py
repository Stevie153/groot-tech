# Generated by Django 4.1.7 on 2023-04-12 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groottech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
