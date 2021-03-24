from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('new', views.CompanyCreateView.as_view(), name='new'),
    path('edit/<str:pk>', views.CompanyUpdateView.as_view(), name='edit'),
]
