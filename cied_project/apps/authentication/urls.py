from django.contrib import admin
from django.urls import path, include
from apps.authentication.views import LoginAPIView, RegisterView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]