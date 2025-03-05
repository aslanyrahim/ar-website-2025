# contact/urls.py
from django.urls import path
from .views import ContactFormView, contact_success

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact_form'),
    path('success/', contact_success, name='contact_success'),
]