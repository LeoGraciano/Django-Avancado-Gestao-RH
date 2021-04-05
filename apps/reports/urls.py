from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('pdf-report-lab-employees', views.report_employees, name='pdf_report_lab'),
    path('pdf-xhtml2pdf-employees', views.PDF.as_view(), name='pdf_html2pdf'),
]
