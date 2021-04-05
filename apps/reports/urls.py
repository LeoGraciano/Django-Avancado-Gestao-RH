from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [

    path('pdf-report-lab', views.pdf_report_lab, name='pdf_report_lab'),
]
