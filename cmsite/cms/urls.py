from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpForm,home,student_dashboard,teacher_dashboard,about,contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
   # path('signup/', views.signup, name='signup'),
    path('student/dashboard', views.signup, name='student_dashboard'),
    path('login/', views.login_view, name='login'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('teacher/profile/', views.teacher_profile, name='teacher_profile'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('attendance/', views.attendance, name='attendance'),
    path('enroll/', views.enroll_course, name='enroll_course'),
    path('grades/', views.manage_grades, name='manage_grades'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Add other URL patterns as needed
]

