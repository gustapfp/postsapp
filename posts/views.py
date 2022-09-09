from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Posts

class PostsFirstView(ListView):
    model = Posts
    template_name = "home.html"
    context_object_name = 'all_posts_list' 

# Create your views here.
