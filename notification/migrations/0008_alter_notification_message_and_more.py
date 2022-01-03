# Generated by Django 4.0 on 2022-01-02 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_avatar'),
        ('post', '0008_alter_post_summary'),
        ('notification', '0007_alter_notification_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipient_notification', to='account.customuser'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_notification', to='account.customuser'),
        ),
    ]
