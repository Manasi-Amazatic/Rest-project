# Generated by Django 3.2.7 on 2021-09-29 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_customer_doc_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='data_sheet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.datasheet'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='doc_num',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
