# Generated by Django 4.1 on 2022-10-05 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0004_law'),
        ('Advocate_app', '0003_advocatedb_district'),
        ('User_app', '0004_boodadvocate_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BoodAdvocate',
            new_name='BookAdvocatedb',
        ),
    ]
