from .views import nav_notifications_handler
from django.urls import path, re_path

app_name = 'notification'

urlpatterns =[
    re_path(r'^ajax/nav_notifications_handler/$', nav_notifications_handler, name = 'nav_notifications_handler'),
]