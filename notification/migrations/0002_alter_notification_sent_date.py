# Generated by Django 4.0 on 2021-12-31 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sent_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
