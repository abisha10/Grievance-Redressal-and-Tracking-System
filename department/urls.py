from django.urls import path
from . import views

app_name = 'department'

urlpatterns = [
    path('department-login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('department-dashboard/', views.dashboard, name="dashboard"),
    path('department/<str:department_name>/', views.department_complaints, name='department-complaints'),
    path('update-status/<int:complaint_id>/', views.update_complaint_status, name='update_complaint_status'),

]