# Generated by Django 4.2.6 on 2023-10-28 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_contacty_email_alter_contacty_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactY',
        ),
    ]