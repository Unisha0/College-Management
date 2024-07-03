from email.headerregistry import Group
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from .forms import SignUpForm, StudentProfileForm, TeacherProfileForm, AttendanceForm, EnrollmentForm, GradeForm
from .models import StudentProfile, TeacherProfile, Attendance, Enrollment, Grade, Course

def home(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Students').exists():
            return redirect('student_dashboard')
        elif request.user.groups.filter(name='Teachers').exists():
            return redirect('teacher_dashboard')
    return render(request, 'cms/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    
#         if form.is_valid():
#             user = form.save()

#             role = form.cleaned_data['role']
#             #print(f'******{role}******')
#             print(type())
#             if role == 'student':
#                 group = Group.objects.get(name='Students')
#                 user.groups.add(group)
#                 user.save()
#                 login(request, user)
#                 return redirect('student_dashboard')
#             elif role == 'teacher':
#                 group = Group.objects.get(name='Teachers')
#                 user.groups.add(group)
#                 user.save()
#                 login(request, user)
#                 return redirect('teacher_dashboard')
#     else:
#         form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.groups.filter(name='Students').exists():
                return redirect('student_dashboard')
            elif user.groups.filter(name='Teachers').exists():
                return redirect('teacher_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'cms/login.html', {'form': form})


def student_profile(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            student_dashboard = form.save(commit=False)
            student_dashboard.user = request.user
            student_dashboard.save()
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm()
    return render(request, 'cms/student_profile.html', {'form': form})

def teacher_profile(request):
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST)
        if form.is_valid():
            teacher_dashboard = form.save(commit=False)
            teacher_dashboard.user = request.user
            teacher_dashboard.save()
            return redirect('teacher_dashboard')
    else:
        form = TeacherProfileForm()
    return render(request, 'cms/teacher_profile.html', {'form': form})

def attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')  # Redirect to student dashboard after saving attendance
    else:
        form = AttendanceForm()
    return render(request, 'cms/attendance.html', {'form': form})

def enroll_course(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')  # Redirect to student dashboard after enrollment
    else:
        form = EnrollmentForm()
    return render(request, 'cms/enroll_course.html', {'form': form})

def manage_grades(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_dashboard')  # Redirect to teacher dashboard after managing grades
    else:
        form = GradeForm()
    return render(request, 'cms/manage_grades.html', {'form': form})

def student_dashboard(request):
    return render(request,'student_dashboard.html')

def teacher_dashboard(request):
    return render(request,'teacher_dashboard.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

