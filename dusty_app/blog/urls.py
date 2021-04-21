
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'), #views.home
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'), #pk-> primary key
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view() , name='post-delete'),
    path('aboutus/', views.aboutus, name='blog-aboutus'),

]

#blog/post_list.html
#<app>/<model>_<view-type>.html