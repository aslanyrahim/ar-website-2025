# services/urls.py
from django.urls import path
from .views import ServiceListView, ServiceDetailView

urlpatterns = [
    path('', ServiceListView.as_view(), name='service_list'),
    path('<slug:slug>/', ServiceDetailView.as_view(), name='service_detail'),
]