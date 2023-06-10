from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import articleviewset

router = DefaultRouter()
router.register('api',articleviewset)

urlpatterns = [

    path('',include(router.urls))
]