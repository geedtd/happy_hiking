# Generated by Django 3.2.6 on 2021-08-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210830_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='difficulty',
            field=models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermidiate'), ('E', 'Experienced')], default='B', max_length=1),
        ),
    ]
