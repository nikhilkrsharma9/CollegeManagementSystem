from django.db import models
from django.contrib.auth.models import User

# college_app/models.py
from django.db import models
from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()  # Ensure this field exists
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PlacementDrive(models.Model):
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    drive_date = models.DateTimeField()
    registration_deadline = models.DateTimeField()
    salary_package = models.CharField(max_length=100)
    eligibility_criteria = models.TextField()
    contact_person = models.ForeignKey(User, on_delete=models.CASCADE)
    brochure = models.FileField(upload_to='placements/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-drive_date']

    def __str__(self):
        return f"{self.company_name} - {self.drive_date.strftime('%Y-%m-%d')}"

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    established_date = models.DateField(default=date.today)  # Add default
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credit = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.code} - {self.name}"

from django.db import models
from django.contrib.auth.models import User

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    join_date = models.DateField()
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.faculty_id})"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    admission_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)
    courses = models.ManyToManyField(Course, through='Enrollment')
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.student_id})"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, null=True, blank=True)
    
    class Meta:
        unique_together = ('student', 'course')
    
    def __str__(self):
        return f"{self.student} - {self.course}"
    
class InstitutionalInfo(models.Model):
    summary = models.TextField()
    about_us = models.TextField()
    vision = models.TextField()
    mission = models.TextField()
    infrastructure_details = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Institutional Information"

    def __str__(self):
        return "Institutional Information"

class Placement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company_name = models.CharField(max_length=200)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.contrib.auth.models import User

