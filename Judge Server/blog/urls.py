from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,comment,upvote,downvote,deleteComment
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/upvote/',views.upvote,name='upvote'),
    path('post/downvote/',views.downvote,name='downvote'),
    path('post/delete/<int:comment>/',views.deleteComment,name='deleteComment'),
    path('post/comment',views.comment,name='comment'),
    path('post/savecomment/',views.savecomment,name='savecomment')
]

