# Generated by Django 4.2.6 on 2023-10-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('subject', models.TextField(blank=True)),
                ('phone', models.IntegerField()),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]