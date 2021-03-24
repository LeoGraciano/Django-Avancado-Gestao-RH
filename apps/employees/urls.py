from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('list/', views.EmployeeListView.as_view(), name='list'),
    path('new/', views.EmployeeCreateView.as_view(), name='new'),
    path('update/<str:pk>', views.EmployeeUpdateView.as_view(), name='update'),
    path('delete/<str:pk>', views.EmployeeDeleteView.as_view(), name='delete'),
]
