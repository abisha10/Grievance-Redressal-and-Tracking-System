from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from user.forms import StyledAuthenticationForm
from user.models import Complaint
from .forms import ComplaintStatusForm
from django.contrib import messages
from django.core.mail import send_mail

def login_view(request):
    if request.method == "POST":
        form = StyledAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("department:dashboard")
    else:
        form = StyledAuthenticationForm()
    return render(request, 'department/login.html', {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("user:index")

def dashboard(request): 
    departments = Complaint.objects.values('complaint_type').distinct()
    return render(request, 'department/dashboard.html', {'departments':departments})

def department_complaints(request, department_name):
    complaints = Complaint.objects.filter(complaint_type=department_name)
    return render(request, 'department/complaints.html', {'complaints': complaints, 'department_name': department_name})

# update status
# def update_complaint_status(request, complaint_id):
#     complaint = get_object_or_404(Complaint, id=complaint_id)
#     if request.method == 'POST':
#         form = ComplaintStatusForm(request.POST, instance=complaint)
#         if form.is_valid():
#             form.save()
#             return redirect('department:dashboard')  # Redirect back to department dashboard
#     else:
#         form = ComplaintStatusForm(instance=complaint)

#     return render(request, 'department/update_status.html', {'form': form, 'complaint': complaint})
def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    
    if request.method == 'POST':
        form = ComplaintStatusForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            
            # Check if status is updated to "Resolved"
            if complaint.status == 'Resolved':
                subject = "Update on Your Complaint Status"
                message = f"Dear {complaint.name},\n\nWe are writing to inform you about the status of your complaint regarding '{complaint.details}' submitted to the Municipal Corporation.\n\nAfter reviewing your concerns, we have taken the necessary actions, and we are pleased to inform you that your complaint has been successfully resolved.\n\nThank you for bringing this issue to our attention and for your patience throughout the process. \n\nHave a great day!\n\nBest Regards,\nMunicipal Corporation Team"
                recipient_email = complaint.email  # Get email from the complaint form

                try:
                    send_mail(subject, message, 'abisharam2003@gmail.com', [recipient_email])
                    messages.success(request, "Status updated and email sent successfully", extra_tags="update_status")
                    return redirect('department:update_status', complaint_id=complaint_id)
                except Exception as e:
                    messages.error(request, f'Error sending email: {e}')
            elif complaint.status == 'In Progress':
                messages.success(request, "Status updated to In Progress", extra_tags="update_status")

            elif complaint.status == 'Pending':
                messages.success(request, "Status updated Pending", extra_tags="update_status")
            elif complaint.status == 'Rejected':
                subject = "Update on Your Complaint Status"
                message = f"Dear {complaint.name},\n\nWe have reviewed your complaint regarding '{complaint.details}' submitted to the Municipal Corporation, and found it to be invalid or not applicable. As a result, it has been rejected.\n\nIf you believe this was done in error or have additional details to provide, please contact us.Thank you for your understanding. \n\nBest Regards,\nMunicipal Corporation Team"
                recipient_email = complaint.email  # Get email from the complaint form

                try:
                    send_mail(subject, message, 'abisharam2003@gmail.com', [recipient_email])
                    messages.success(request, "Complaint Rejected", extra_tags="update_status")
                    return redirect('department:update_status', complaint_id=complaint_id)
                except Exception as e:
                    messages.error(request, f'Error sending email: {e}')




                # messages.success(request, "Complaint Rejected", extra_tags="update_status")


            
            
    
    else:
        form = ComplaintStatusForm(instance=complaint)

    return render(request, 'department/update_status.html', {'form': form, 'complaint': complaint})