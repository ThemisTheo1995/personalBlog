# Generated by Django 4.0 on 2022-01-03 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_avatar'),
        ('post', '0011_alter_post_author_alter_post_body_alter_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customuser'),
        ),
    ]
