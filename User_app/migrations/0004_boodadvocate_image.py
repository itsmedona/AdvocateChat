# Generated by Django 4.1 on 2022-10-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0003_boodadvocate'),
    ]

    operations = [
        migrations.AddField(
            model_name='boodadvocate',
            name='image',
            field=models.ImageField(default='null.jpg', upload_to='Image'),
        ),
    ]
