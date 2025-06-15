from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .api import TaskViewSet

router = DefaultRouter()
router.register(r'api/tasks',TaskViewSet)

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('',include(router.urls)),
]
