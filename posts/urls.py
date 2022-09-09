from django.urls import path
from .views import PostsFirstView 

urlpatterns = [
    path('', PostsFirstView.as_view(), name='home'),

]
    