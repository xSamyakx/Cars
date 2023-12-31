# Generated by Django 4.2.6 on 2023-10-28 16:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carss', '0003_alter_car_description_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
    ]
