# Generated by Django 3.1.3 on 2021-01-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_prices_tool', '0003_car_price_dollars'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_make', models.CharField(max_length=50)),
            ],
        ),
    ]
