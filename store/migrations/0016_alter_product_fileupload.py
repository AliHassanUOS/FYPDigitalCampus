# Generated by Django 3.2.3 on 2021-07-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210706_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fileupload',
            field=models.FileField(blank=True, null=True, upload_to='upload/products'),
        ),
    ]
