from .models import Notification
from django.db.models import Count

def notifications_view(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(recipient_id = request.user.pk).order_by('-sent_date')[:100]
    else:
        notifications = Notification.objects.values('message__title', 'message__pk', 'sent_date').annotate(dcount=Count("message__body")).order_by('-sent_date')[:2]

    pending_to_read = Notification.objects.filter(recipient_id = request.user.pk, read=False).order_by('-sent_date')[:100].count()
    if pending_to_read > 0:
        is_read = False
    else:
        is_read = True
    
    return {'notifications':notifications,
            'is_read': is_read}