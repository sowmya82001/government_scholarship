from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, scholarship_detail, register
from .views import logout_view

urlpatterns = [
    path('', home, name='home'),
    path('scholarship/<int:pk>/', scholarship_detail, name='scholarship_detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='scholarships/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', logout_view, name='logout'),
]
