# Generated by Django 3.2.7 on 2021-09-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profession',
            name='test',
            field=models.CharField(default='manasi', max_length=50),
            preserve_default=False,
        ),
    ]