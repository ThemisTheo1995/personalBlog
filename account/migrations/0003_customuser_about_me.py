# Generated by Django 4.0 on 2022-01-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about_me',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]