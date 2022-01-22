import datetime
from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_DEFAULT, SET_NULL
from account.models import CustomUser
from .validators import validate_file_size

class Post(models.Model):
    TAG_CHOICES = [
        ('Other','Other'),
        ('Technology','Technology'),
        ('Environment','Environment'),
        ('Aviation', 'Aviation'),
        ('Civil', 'Civil'),
        ('Healthcare', 'Healthcare'),
        ('Bio-Engineering', 'Bio-Engineering'),
        ('Engineering', 'Engineering'),
    ]
    CATEGORY_CHOICES = [
        ('Other','Other'),
        ('Technology','Technology'),
        ('Environment','Environment'),
        ('Aviation', 'Aviation'),
        ('Civil', 'Civil'),
        ('Healthcare', 'Healthcare'),
        ('Bio-Engineering', 'Bio-Engineering'),
        ('Engineering', 'Engineering'),
        ('Politics', 'Politics'),
    ]
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=50, choices=TAG_CHOICES, default='', blank=True)
    author = models.ForeignKey(CustomUser, on_delete=SET_NULL, null=True)
    body = models.TextField(max_length=12000)
    summary = models.TextField(max_length=300,verbose_name="Summary(Card description on landing page)")
    post_date = models.DateField(default=datetime.datetime.now, blank=True)
    category = models.CharField(max_length=255, default='', blank=True, choices= CATEGORY_CHOICES)
    likes = models.ManyToManyField(CustomUser, blank=True, related_name='likes')
    clicks = models.CharField(max_length=255, blank=True, null= True)
    published = models.BooleanField(default=False, verbose_name="Published")
    re_published =  models.BooleanField(default=False,verbose_name="Re-published")
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', validators=[validate_file_size])
    
    def save(self, *args, **kwargs):
        if self.published and self.re_published:
            self.post_date = datetime.datetime.today().strftime('%Y-%m-%d')
        super(Post, self).save(*args, **kwargs)
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
