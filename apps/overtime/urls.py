from apps.overtime.api.views import OverTimeViewSet
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'overtime'
router = routers.DefaultRouter()
router.register('users', OverTimeViewSet)

urlpatterns = [
    path('list/', views.OverTimeListView.as_view(), name='list'),
    path('new/', views.OverTimeCreateView.as_view(), name='new'),
    path('update/<str:pk>', views.OverTimeUpdateView.as_view(), name='update'),
    path('user-overtime/<str:pk>',
         views.UserOverTimeView.as_view(), name='user-overtime'),
    path('update-employee/<str:pk>', views.OverTimeEmployeeUpdateView.as_view(),
         name='update_return_employee'),
    path('delete/<str:pk>', views.OverTimeDeleteView.as_view(), name='delete'),

    path('api/', include(router.urls)),
]
