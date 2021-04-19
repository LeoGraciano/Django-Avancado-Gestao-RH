from django.urls import path, include
from . import views
from rest_framework import routers
from core.api.views import UserViewSet, GroupViewSet

app_name = 'core'


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', views.home, name='index'),


    # API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    # celery
    path('celery/', views.celery, name='celery')
]
