from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('list/', views.DocumentListView.as_view(), name='list'),
    path('new/', views.DocumentCreateView.as_view(), name='new'),
    path('update/<str:pk>', views.DocumentUpdateView.as_view(), name='update'),
    path('delete/<str:pk>', views.DocumentDeleteView.as_view(), name='delete'),
]
