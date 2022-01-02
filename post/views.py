from django.shortcuts import render
from django.views import generic
from .models import Post

### List view ###
class BlogListView(generic.ListView):
    paginate_by = 15
    template_name = "post/post_listview.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = Post.objects.filter(published=True).order_by('-post_date')
        return queryset
