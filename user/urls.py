from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.Index, name='index'),
    path('user-home/', views.UserHome ,name='user-home'),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('file-complaint/', views.file_complaint, name='file-complaint'),
    path('status/', views.track_status, name='track-status'),
]
