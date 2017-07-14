from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from customauth.views import UserViewSet

router = DefaultRouter()
router.register(r'auth', UserViewSet, base_name='auth')

urlpatterns = [
    url(r'^', include(router.urls)),
]
