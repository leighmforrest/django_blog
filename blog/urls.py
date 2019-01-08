from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/<str:username>', views.UserPostIndexView.as_view(), name='user-posts'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('blog/create/', views.PostCreateView.as_view(), name='create'),
    path('blog/<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]
