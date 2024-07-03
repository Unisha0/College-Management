from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import StudentProfile, TeacherProfile, Administration, Attendance

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'address', 'phone_number')
    search_fields = ('user__username', 'user__email', 'phone_number')

class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'phone_number')
    search_fields = ('user__username', 'user__email', 'department')

class AdministrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'phone_number')
    search_fields = ('user__username', 'user__email', 'position')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('student__user__username', 'student__user__email')

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)
admin.site.register(Administration, AdministrationAdmin)
admin.site.register(Attendance, AttendanceAdmin)
