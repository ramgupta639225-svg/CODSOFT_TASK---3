from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IssuedBookViewSet

router = DefaultRouter()
router.register(r'issuedbooks', IssuedBookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]