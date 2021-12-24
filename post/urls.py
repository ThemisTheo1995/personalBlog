from django.urls.resolvers import URLPattern
from .views import BlogListView
from django.urls import path

app_name = 'post'

urlpatterns =[
    path('', BlogListView.as_view(), name='posts'),
]