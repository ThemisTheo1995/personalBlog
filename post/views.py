from django.shortcuts import redirect, render
from django.views import generic
from .models import Post
from .forms import PostCreationForm
from notification.models import Click

### List view ###
class BlogListView(generic.ListView):
    paginate_by = 15
    template_name = "post/post_listview.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = Post.objects.filter(published=True).order_by('-post_date')
        return queryset

### Detail view ###
class BlogDetailView(generic.DetailView):
    template_name = "post/post_detailview.html"
    context_object_name = "post"
    
    def get_queryset(self):
        post_pk = self.kwargs.get('pk', None)
        # Save the view/click
        entity = ''
        if self.request.user.is_authenticated:
            entity = self.request.user.email
        else:
            x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR', '')
            if x_forwarded_for:
                entity = x_forwarded_for.split(',')[0]
            else:
                entity = self.request.META.get('REMOTE_ADDR', '')
        
        try:
            Click.objects.filter(post=post_pk).get(entity=entity)
        except:
            Click.objects.create(entity = entity,
                                 post=Post.objects.get(pk = post_pk))
        
        # Save the total number to Post model.
        clicks = Click.objects.filter(post = post_pk).count()
        Post.objects.filter(pk=post_pk).update(clicks = clicks)
        
        # Return post detail view
        queryset = Post.objects.filter(published=True)
        return queryset
    
### Create view ###
class BlogCreateView(generic.CreateView):
    template_name = "post/post_createview.html"
    form_class = PostCreationForm
    
    def get_success_url(self, form):
        
        return redirect("blog:posts")
    
    # def form_valid(self, form):
    #     post = form.save(commit = False)
    
    #     post.save()
        
    #     return super(BlogCreateView, self).form_valid(form)