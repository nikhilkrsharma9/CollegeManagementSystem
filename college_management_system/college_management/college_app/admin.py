from django.contrib import admin
from .models import Student, Faculty, Course, Department, Enrollment
from django.contrib import admin
from .models import InstitutionalInfo

@admin.register(InstitutionalInfo)
class InstitutionalInfoAdmin(admin.ModelAdmin):
    list_display = ('last_updated',)
    fieldsets = (
        ('Summary', {'fields': ('summary',)}),
        ('About Us', {'fields': ('about_us',)}),
        ('Vision & Mission', {
            'fields': ('vision', 'mission')
        }),
        ('Infrastructure', {
            'fields': ('infrastructure_details',)
        }),
    )

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Enrollment)

