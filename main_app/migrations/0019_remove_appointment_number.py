# Generated by Django 4.0.4 on 2022-06-08 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='number',
        ),
    ]
