# Generated by Django 4.1 on 2022-09-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advocate_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advocatedb',
            old_name='idproof',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='advocatedb',
            name='email',
        ),
        migrations.RemoveField(
            model_name='advocatedb',
            name='name',
        ),
        migrations.AddField(
            model_name='advocatedb',
            name='adname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='advocatedb',
            name='emailid',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='advocatedb',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='advocatedb',
            name='advocatetype',
            field=models.CharField(default='', max_length=20),
        ),
    ]
