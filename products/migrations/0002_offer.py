# Generated by Django 4.0.4 on 2022-04-15 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=150)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
