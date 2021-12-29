from django.db import models
from django.db.models.deletion import DO_NOTHING
from account.models import CustomUser
from .validators import validate_file_size

class Post(models.Model):
    TAG_CHOICES = [
        ('',''),
        ('Technology','Technology'),
        ('Environment','Environment'),
        ('Aviation', 'Aviation'),
        ('Civil', 'Civil'),
        ('Engineering', 'Engineering'),
    ]
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=50, choices=TAG_CHOICES, default='', blank=True)
    author = models.ForeignKey(CustomUser, on_delete=DO_NOTHING)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='', blank=True)
    likes = models.ManyToManyField(CustomUser, blank=True, related_name='likes')
    published = models.BooleanField(default=False, verbose_name="Published immediately after submission?")
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', validators=[validate_file_size], blank=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
