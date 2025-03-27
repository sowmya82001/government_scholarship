from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Scholarship, Application
from .forms import  ApplicationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm  # Ensure this form exists
from django.contrib.auth import logout

def home(request):
    scholarships = Scholarship.objects.all()
    return render(request, 'scholarships/home.html', {'scholarships': scholarships})

def scholarship_detail(request, pk):
    scholarship = get_object_or_404(Scholarship, pk=pk)
    # Check if the user already applied for this scholarship
    existing_application = None
    if request.user.is_authenticated:
        existing_application = Application.objects.filter(student=request.user, scholarship=scholarship).first()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user
            application.scholarship = scholarship
            application.save()
            return redirect('home')
    else:
        form = ApplicationForm()

    return render(request, 'scholarships/scholarship_detail.html', {
        'scholarship': scholarship,
        'form': form,
        'existing_application': existing_application
    })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, "Successfully registered! Welcome.")
            return redirect('home')  # Change 'home' to your actual home URL name
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to homepage
        else:
            return render(request, "scholarships/login.html", {"error": "Invalid username or password"})

    return render(request, "scholarships/login.html")