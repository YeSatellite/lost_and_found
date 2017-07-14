from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from post.views import LostViewSet

router = DefaultRouter()
router.register(r'lost', LostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
