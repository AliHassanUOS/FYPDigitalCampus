# Generated by Django 3.2.3 on 2021-07-05 07:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210705_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='semester',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
    ]
