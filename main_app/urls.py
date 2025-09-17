from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('movie/', views.movie, name='movie'),
    path('posts/<int:post_id>/', views.post_detail, name='post-detail'),
    path('posts/create/', views.PostCreate.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('comments/create/', views.CommentCreate.as_view(), name='comment-create'),
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment-delete'),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment-update'),
    path('posts/<int:post_id>/comments/<int:comment_id>/reply/', views.CommentReply.as_view(), name='comment-reply'),
]