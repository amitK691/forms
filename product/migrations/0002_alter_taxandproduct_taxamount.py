# Generated by Django 3.2.4 on 2021-06-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxandproduct',
            name='TaxAmount',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
