# Generated by Django 3.2.7 on 2021-09-28 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profession_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='test',
        ),
    ]
