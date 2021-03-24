from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('new', views.CompanyCreateView.as_view(), name='new'),
]
