from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (StudentListView, StudentCreateView, StudentUpdateView,
                    FacultyListView, FacultyCreateView, FacultyUpdateView,
                    CourseListView, CourseCreateView, CourseUpdateView,
                    DepartmentListView, DepartmentCreateView, DepartmentUpdateView)

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('register/', views.student_register, name='student-register'),
    path('login/', auth_views.LoginView.as_view(template_name='college_app/login.html'), name='student-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='college_app/logout.html'), name='student-logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Ensure this exists
    path('summary/', views.summary, name='summary'),
    path('about-us/', views.about_us, name='about_us'),
    path('vision-mission/', views.vision_mission, name='vision_mission'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    
    # Student URLs
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/add/', StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student/details/', views.student_details, name='student-details'),
    
    # Faculty URLs
    path('faculty/', FacultyListView.as_view(), name='faculty-list'),
    path('faculty/add/', views.faculty_add, name='faculty-add'),
    path('faculty/<int:pk>/', FacultyUpdateView.as_view(), name='faculty-update'),
    
    # Course URLs
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/add/', CourseCreateView.as_view(), name='course-add'),
    path('courses/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    
    # Department URLs
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/add/', DepartmentCreateView.as_view(), name='department-add'),
    path('departments/<int:pk>/', DepartmentUpdateView.as_view(), name='department-update'),
    
    # Placement URLs
    path('placements/', views.placement_list, name='placement-list'),
    path('placements/add/', views.placement_create, name='placement-create'),
    
    # Event URLs
    path('events/', views.event_list, name='event-list'),
    path('events/add/', views.event_create, name='event-create'),
    
    path('faculty/register/', views.faculty_register, name='faculty-register'),
]