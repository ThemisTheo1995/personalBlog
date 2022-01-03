from .views import BlogListView, BlogDetailView
from django.urls import path

app_name = 'post'

urlpatterns =[
    path('', BlogListView.as_view(), name='posts'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
]