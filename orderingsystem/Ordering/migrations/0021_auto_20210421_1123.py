# Generated by Django 3.1.6 on 2021-04-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering', '0020_auto_20210410_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordering',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
