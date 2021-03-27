from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('list/', views.DocumentListView.as_view(), name='list'),
    path('new/<str:pk>', views.DocumentCreateView.as_view(), name='new'),
    path('delete/<str:pk>', views.DocumentDeleteView.as_view(), name='delete'),
]
