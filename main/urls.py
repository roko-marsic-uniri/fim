from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('film/<int:pk>/', views.film_detail, name='film_detail'),
    path('film/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('film/<int:pk>/update_review/<int:review_pk>/', views.update_review, name='update_review'),
    path('film/<int:pk>/delete_review/<int:review_pk>/', views.delete_review, name='delete_review'),
]