from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('pdf-report-lab-employees', views.report_employees, name='pdf_report_lab'),
    path('pdf-xhtml2pdf-employees', views.PDF.as_view(), name='pdf_html2pdf'),
    path('export-csv/overtime', views.OverTimeExportCSV.as_view(),
         name='export_csv_overtime'),
    path('export-excel/overtime', views.OverTimeExportExcel.as_view(),
         name='export_excel_overtime'),
]
