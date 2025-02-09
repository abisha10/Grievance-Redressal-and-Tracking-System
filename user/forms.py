from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Complaint

class StyledUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(StyledUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Bootstrap styling
            field.widget.attrs['placeholder'] = f"Enter {field.label}"

class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(StyledAuthenticationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f"Enter {field.label}"

# complaint form
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'mobile_number', 'email', 'location', 'complaint_type', 'details', 'image']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'location': 'Complaint Location',
            'complaint_type': 'Type of Complaint',
            'details': 'Complaint Details',
            'image': 'Upload Photo (Optional)'

        }
        widgets = {
            'complaint_type': forms.Select(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'location': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
        }
