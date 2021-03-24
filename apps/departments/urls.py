from django.urls import path
from . import views

app_name = 'departments'

urlpatterns = [

    path('list', views.DepartmentListView.as_view(), name='list'),
    path('new/', views.DepartmentCreateView.as_view(), name='new'),
    path('update/<str:pk>', views.DepartmentUpdateView.as_view(), name='update'),
    path('delete/<str:pk>', views.DepartmentDeleteView.as_view(), name='delete'),
]
