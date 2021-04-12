from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'core'


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', views.home, name='index'),


    # API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
