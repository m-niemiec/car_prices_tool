# Generated by Django 3.1.3 on 2021-02-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_prices_tool', '0009_delete_carmake'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date_issued',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='date_scraped',
            field=models.DateField(null=True),
        ),
    ]