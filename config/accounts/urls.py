from django.urls import path
from . import views

from django.contrib.auth.views import (
    LoginView,
    LogoutView
)

urlpatterns = [
    path('login/', LoginView.as_view(template_name="base.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="base.html"), name='logout'),
    path('register/', views.register, name='register'),
    path('setup-mfa/<int:device_id>/', views.setup_mfa, name='setup_mfa'),
    path('verify-token/', views.verify_token, name='verify_token'),


]