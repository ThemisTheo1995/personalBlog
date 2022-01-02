import datetime
from datetime import date
from django.db import models
from django.db.models.deletion import DO_NOTHING
from account.models import CustomUser
from post.models import Post
from django.db.models.signals import post_save

class Notification(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=DO_NOTHING, null=True, related_name='sender_notification')
    recipient = models.ForeignKey(CustomUser,on_delete=DO_NOTHING, related_name='recipient_notification', blank=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    sent_date = models.DateField(default=datetime.datetime.now, blank=True)
    
    @property
    def is_past_due(self):
        days_due = date.today() - self.sent_date 
        zero_days = datetime.timedelta(days=0)
        one_day = datetime.timedelta(days=1)
        if days_due == zero_days:
            return 'Today'
        elif days_due == one_day:
            return 'Yesterday'
        else:
            return self.sent_date
    
    def __str__(self):
        return self.message + ' by: ' + str(self.sender)
    
# Signal to send notification on new post creation.
def send_notification(sender, instance, created, **kwargs):
    sender = instance.author
    message = instance.title
    published = instance.published
    re_published = instance.re_published
    if (published and created) or (published and not re_published):
        recipients = CustomUser.objects.all()
        for recipient in recipients:
            Notification.objects.create(sender=sender, 
                                        recipient=recipient, 
                                        message=message)
        try:
            Post.objects.filter(pk=instance.pk).update(re_published=True)
        except:
            pass
        
    else:
        pass
    

post_save.connect(send_notification, sender=Post)
