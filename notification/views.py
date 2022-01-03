from .models import Notification
from django.http import JsonResponse
from django.core import serializers


### Landing view - Auto complete ###
def nav_notifications_handler(request):
    if  request.method == 'GET':
        try:
            user = request.user
            Notification.objects.filter(recipient=user).update(read=True)
            re = True
        except:
            re = False
    return JsonResponse(re, safe=False)