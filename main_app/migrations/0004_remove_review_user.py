# Generated by Django 3.2.6 on 2021-08-30 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210830_0312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]
