from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'media', views.MediaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('frames/', views.MediaFramesView.as_view()),
]