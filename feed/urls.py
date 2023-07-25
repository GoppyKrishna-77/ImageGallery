from django.urls import path
from .views import HomePageView, DetailPageView, PostView, delete_post

app_name = "feed"

urls = [
    path('', HomePageView.as_view(), name="index"),
    path('', delete_post, name='delete_post'),
    path('detail/<int:pk>/', DetailPageView.as_view(), name="detail"),
    path('post/', PostView.as_view(), name="post"),
]
