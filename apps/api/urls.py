from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'api'
router = routers.DefaultRouter()
router.register('employees', views.EmployeeViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
