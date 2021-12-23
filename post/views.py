from django.shortcuts import render
from django.views import generic

### List view ###
class BlogListView(generic.ListView):
    paginate_by = 4
    template_name = "post/post_listview.html"
    context_object_name = "list"
    
    def get_queryset(self):
        queryset = ''
        return queryset
