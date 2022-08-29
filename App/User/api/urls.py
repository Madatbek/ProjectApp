from django.conf.urls import include
from django.urls import re_path
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
# router.register('week', WeekViewSet, basename='week')


urlpatterns = [
    re_path('', include(router.urls))
]