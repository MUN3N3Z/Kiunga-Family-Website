# Generated by Django 4.1.5 on 2023-05-20 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(help_text='DD/MM/YYYY', null=True),
        ),
    ]
