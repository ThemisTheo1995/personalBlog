# Generated by Django 4.0 on 2022-01-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_post_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('Other', 'Other'), ('Technology', 'Technology'), ('Environment', 'Environment'), ('Aviation', 'Aviation'), ('Civil', 'Civil'), ('Healthcare', 'Healthcare'), ('Bio-Engineering', 'Bio-Engineering'), ('Engineering', 'Engineering'), ('Politics', 'Politics')], default='', max_length=255),
        ),
    ]
