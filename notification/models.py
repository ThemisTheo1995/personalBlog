import datetime
from datetime import date
from django.db import models
from django.db.models.deletion import CASCADE
from account.models import CustomUser
from post.models import Post
from django.db.models.signals import post_save


### Notifications model ###
class Notification(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=CASCADE, null=True, related_name='sender_notification')
    recipient = models.ForeignKey(CustomUser,on_delete=CASCADE, related_name='recipient_notification', blank=True)
    message = models.ForeignKey(Post,on_delete=CASCADE)
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
        return self.message.title + ' | ' + str(self.sender)
    
# Signal to send notification on new post creation.
def send_notification(sender, instance, created, **kwargs):
    sender = instance.author
    message = instance
    published = instance.published
    re_published = instance.re_published
    # Post is created for the first time.
    if (published and created):
        recipients = CustomUser.objects.all()
        # Create notifications for the users.
        for recipient in recipients:
            Notification.objects.create(sender=sender, 
                                        recipient=recipient, 
                                        message=message)
    # Post is re-published.
    elif(published and re_published):
        try:
            recipients = CustomUser.objects.all()
            
            # New users should get the notifications too.
            Notification.objects.filter(message=message).delete()
            for recipient in recipients:
                Notification.objects.create(sender=sender, 
                                        recipient=recipient, 
                                        message=message)
            # Re-publish flag returned to false.
            Post.objects.filter(pk=instance.pk).update(re_published=False)
        except:
            print('Error:bnm_send_notification_#2')
        
    else:
        pass

post_save.connect(send_notification, sender=Post)

### Views/Clicks model ###
class Click(models.Model):
    entity = models.CharField(max_length=255, blank=True)
    post = models.ForeignKey(Post, on_delete=CASCADE)
    clicked_datetime = models.DateTimeField(default=datetime.datetime.now, blank=True)
    
    @property
    def total_clicks(self):
        return self.post.count()
    
    def __str__(self):
        return self.post.title + 'clicked by: '+ self.entity

### Likes model ###

### Comments model ###

