from django import forms
from .models import Post

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = (
            'title_tag',
            'post_date',
            'likes',
            # 'comments',
            'clicks',
            'author',
            're_published',
        )
        labels = {
            "title":"Title",
            "thumbnail":"Thumbnail",
            "category":"Category",
            "summary":"Summary",
            "body":"Blogpost Content",
            "published": "Published",
        }         
    field_order = ['title','thumbnail','category',
                   'summary', 'body', 'published']
    