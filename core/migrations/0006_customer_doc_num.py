# Generated by Django 3.2.7 on 2021-09-29 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_customer_documentname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='doc_num',
            field=models.CharField(default='', max_length=12, unique=True),
            preserve_default=False,
        ),
    ]
