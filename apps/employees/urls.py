from django.urls import path, include
from . import views
from rest_framework import routers
from apps.employees.api.views import EmployeeViewSet

app_name = 'employees'
router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)


urlpatterns = [
    path('list/', views.EmployeeListView.as_view(), name='list'),
    path('new/', views.EmployeeCreateView.as_view(), name='new'),
    path('update/<str:pk>', views.EmployeeUpdateView.as_view(), name='update'),
    path('delete/<str:pk>', views.EmployeeDeleteView.as_view(), name='delete'),

    path('api/', include(router.urls)),
]
