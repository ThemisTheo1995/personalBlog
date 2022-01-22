from .views import BlogListView, BlogDetailView, BlogCreateView
from django.urls import path

app_name = 'post'

urlpatterns =[
    path('', BlogListView.as_view(), name='posts'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('post/create', BlogCreateView.as_view(), name='create'),
]