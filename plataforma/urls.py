
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('employees/', include('apps.employees.urls', namespace='employees')),
    path('companies/', include('apps.companies.urls', namespace='companies')),
    path('departments/', include('apps.departments.urls', namespace='departments')),
    path('documents/', include('apps.documents.urls', namespace='documents')),
    path('overtime/', include('apps.overtime.urls', namespace='overtime')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
