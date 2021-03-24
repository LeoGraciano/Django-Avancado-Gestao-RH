
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('employees', include('apps.employees.urls')),
    path('companies', include('apps.companies.urls')),
    path('departments', include('apps.departments.urls')),
    path('documents', include('apps.departments.urls')),
    path('overtime', include('apps.overtime.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
