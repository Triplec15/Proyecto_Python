# Generated by Django 4.0.4 on 2022-07-23 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='SKU',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]