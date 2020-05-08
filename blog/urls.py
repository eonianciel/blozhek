from django.contrib import admin
from django.urls import path

from .views import*

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('drafts/', post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', post_publish, name='post_publish'),
    path('post/<pk>/remove/', post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>', tag_detail, name='tags_detail_url'),
]
