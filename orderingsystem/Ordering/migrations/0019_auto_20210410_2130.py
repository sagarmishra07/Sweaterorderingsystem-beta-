# Generated by Django 3.1.6 on 2021-04-10 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering', '0018_auto_20210408_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordering',
            name='delivered_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='ordered_date',
            field=models.DateField(auto_now=True),
        ),
    ]
