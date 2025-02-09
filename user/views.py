from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import StyledUserCreationForm, StyledAuthenticationForm
from .forms import ComplaintForm
from django.contrib import messages
from .models import Complaint


def Index(request):
    # Retrieve the counts
    total_complaints = Complaint.objects.count()
    resolved_complaints = Complaint.objects.filter(status='Resolved').count()
    in_progress_complaints = Complaint.objects.filter(status='In Progress').count()
    rejected_complaints = Complaint.objects.filter(status='Rejected').count()

    # Pass the data to the template
    context = {
        'total_complaints': total_complaints,
        'resolved_complaints': resolved_complaints,
        'in_progress_complaints': in_progress_complaints,
        'rejected_complaints' : rejected_complaints
    }
    return render(request, 'index.html', context)

def UserHome(request):
    return render(request, 'user/user_home.html')

def register(request):
    if request.method == "POST":
        form = StyledUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user:user-home")
    else:
        form = StyledUserCreationForm()
    return render(request, 'user/register.html', {"form": form})

def login_view(request):
    if request.method == "POST":
        form = StyledAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("user:user-home")
    else:
        form = StyledAuthenticationForm()
    return render(request, 'user/login.html', {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("user:index")
    
# complaint
def file_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your complaint has been submitted successfully!')
            return redirect('user:file-complaint')  # Redirect to the same page to show the message
    else:
        form = ComplaintForm()
    return render(request, 'user/file_complaint.html', {'form': form})


# Status
def track_status(request):
    complaints = None  # Initialize variable to store complaints
    if request.method == "POST":
        email = request.POST.get('email')
        complaints = Complaint.objects.filter(email=email)
    return render(request, 'user/track_status.html', {'complaints': complaints})

