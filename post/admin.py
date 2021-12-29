from django.contrib import admin
from .models import Post

# Properties admin
@admin.register(Post)
class PropertiesAdmin(admin.ModelAdmin):
    
    model = Post
    list_display = ['id', 'title', 'title_tag','author', 'post_date', 'category', 'published']
    list_filter = ['title_tag', 'category', 'author', 'published']
    list_display_links = ['id']
    list_editable = ['published',]
    search_fields = ['title', 'title_tag', 'author', 'body', 'category']
    list_per_page = 100