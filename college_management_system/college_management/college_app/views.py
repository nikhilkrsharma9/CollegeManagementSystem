from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Faculty, Course, Department, Placement, Event
from .forms import UserRegisterForm, StudentForm, FacultyForm, CourseForm, DepartmentForm, PlacementForm, EventForm
from django.contrib import messages
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from .forms import FacultyUserForm, FacultyForm

from django.shortcuts import render, redirect
from .forms import FacultyUserForm, FacultyForm

from django.shortcuts import render, redirect
from .forms import FacultyUserForm, FacultyForm

from django.shortcuts import render, redirect
from .forms import FacultyUserForm, FacultyForm

from django.contrib.auth.models import User
from .models import PlacementDrive

from django.contrib.auth import login, authenticate
from .forms import StudentUserForm, StudentForm
from .models import Student

def student_register(request):
    if request.method == 'POST':
        user_form = StudentUserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            login(request, user)  # Automatically log in the student after registration
            return redirect('student-details')
    else:
        user_form = StudentUserForm()
        student_form = StudentForm()
    return render(request, 'college_app/student_register.html', {
        'user_form': user_form,
        'student_form': student_form
    })

@login_required
def student_details(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return render(request, 'college_app/no_student.html')  # Render a page if no student record exists
    return render(request, 'college_app/student_details.html', {'student': student})

def faculty_add(request):
    if request.method == 'POST':
        user_form = FacultyUserForm(request.POST)
        faculty_form = FacultyForm(request.POST)
        
        if user_form.is_valid() and faculty_form.is_valid():
            user = user_form.save()
            faculty = faculty_form.save(commit=False)
            faculty.user = user
            faculty.save()
            return redirect('faculty-list')
    else:
        user_form = FacultyUserForm()
        faculty_form = FacultyForm()

    return render(request, 'college_app/faculty_form.html', {
        'user_form': user_form,
        'faculty_form': faculty_form
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'college_app/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'college_app/dashboard.html')

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    else:
        form = StudentForm()
    
    return render(request, 'college_app/student_form.html', {'form': form})

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'college_app/student_list.html'
    context_object_name = 'students'

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import StudentUserForm, StudentForm

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'college_app/student_form.html'
    success_url = reverse_lazy('student-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = StudentUserForm(self.request.POST)
        else:
            context['user_form'] = StudentUserForm()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        
        if user_form.is_valid():
            # Save user first
            self.user = user_form.save()
            
            # Save student with user relationship
            self.object = form.save(commit=False)
            self.object.user = self.user
            self.object.save()
            form.save_m2m()  # Save many-to-many relationships
            
            messages.success(self.request, 'Student created successfully!')
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'college_app/student_form.html'
    success_url = reverse_lazy('student-list')

# Similar views for Faculty, Course, and Department
# (FacultyListView, FacultyCreateView, etc.)
# Add these to your existing views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class FacultyListView(LoginRequiredMixin, ListView):
    model = Faculty
    template_name = 'college_app/faculty_list.html'
    context_object_name = 'faculties'
    ordering = ['user__last_name']

class FacultyCreateView(LoginRequiredMixin, CreateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'college_app/faculty_form.html'
    success_url = reverse_lazy('faculty-list')

class FacultyUpdateView(LoginRequiredMixin, UpdateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'college_app/faculty_form.html'
    success_url = reverse_lazy('faculty-list')

class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'college_app/course_list.html'
    context_object_name = 'courses'

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'college_app/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'college_app/course_form.html'
    success_url = reverse_lazy('course-list')

class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'college_app/department_list.html'
    context_object_name = 'departments'

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'college_app/department_form.html'
    success_url = reverse_lazy('department-list')

class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'college_app/department_form.html'
    success_url = reverse_lazy('department-list')

from django.shortcuts import render

def home(request):
    return render(request, 'college_app/home.html')

def summary(request):
    return render(request, 'college_app/summary.html')

def about_us(request):
    return render(request, 'college_app/about_us.html')

def vision_mission(request):
    return render(request, 'college_app/vision_mission.html')

def infrastructure(request):
    return render(request, 'college_app/infrastructure.html')

@login_required
def placement_list(request):
    placements = Placement.objects.all().order_by('-date')
    return render(request, 'college_app/placement_list.html', {'placements': placements})

@login_required
def placement_create(request):
    if request.method == 'POST':
        form = PlacementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('placement-list')
    else:
        form = PlacementForm()
    return render(request, 'college_app/placement_form.html', {'form': form})

@login_required
def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'college_app/event_list.html', {'events': events})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'college_app/event_form.html', {'form': form})

from django.contrib.auth.models import User
from .models import PlacementDrive

def create_placement_drive(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)  # Get the logged-in user
        placement_drive = PlacementDrive.objects.create(
            company_name="Tech Corp",
            description="Campus placement drive for Tech Corp.",
            drive_date="2025-05-01 10:00:00",
            registration_deadline="2025-04-30 23:59:59",
            salary_package="10 LPA",
            eligibility_criteria="Minimum 7.5 CGPA",
            contact_person=user,  # Assign a valid User instance
        )
        placement_drive.save()
