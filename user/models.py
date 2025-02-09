from django.db import models



# Define choices for complaint type
DEPARTMENT_CHOICES = [
    ('Roads', 'Roads'),
    ('Transportation', 'Transportation'),
    ('Sewage & Drainage', 'Sewage & Drainage'),
    ('Electricity & Street Lights', 'Electricity & Street Lights'),
    ('Solid Waste Management', 'Solid Waste Management'),
    ('Health & Sanitation', 'Health & Sanitation'),
    ('Parks & Public Places', 'Parks & Public Places'),
    ('Environment Concerns', 'Environment Concerns'),
    ('Others', 'Others (Legal & Complaints Cell)'),
]

status_choices = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Resolved', 'Resolved'),
    ('Rejected', 'Rejected')
]

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.TextField()
    complaint_type = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    details = models.TextField()
    image = models.ImageField(upload_to='complaint_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')

    def __str__(self):
        return f'{self.name} - {self.complaint_type}'
