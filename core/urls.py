from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name="dashboard" ),
    path('registration', views.registration_view, name="register" ),
    path('validation/', views.validation_view, name="validation"),
    path('admin_dashboard/', views.admin_dashboard, name='admin'),
    path('admin-login', views.admin_login, name="admin_login")
]
