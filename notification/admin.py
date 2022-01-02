from django.contrib import admin
from .models import Notification

# Notification admin
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    
    model = Notification
    list_display = ['id', 'sender', 'recipient','message', 'read', 'sent_date']
    list_filter = ['sender', 'recipient', 'read', 'sent_date']
    list_display_links = ['id']
    list_editable = ['read',]
    search_fields = ['sender', 'recipient', 'read', 'sent_date']
    list_per_page = 100