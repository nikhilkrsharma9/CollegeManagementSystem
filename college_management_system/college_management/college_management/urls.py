from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from college_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('college_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='college_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='college_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]