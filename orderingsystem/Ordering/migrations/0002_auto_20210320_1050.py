# Generated by Django 3.1.6 on 2021-03-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordering',
            name='delivered_date',
            field=models.DateField(max_length=50),
        ),
    ]
