from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from customauth import views
from customauth.views import UserViewSet, AuthMethod

router = DefaultRouter()
router.register(r'user', UserViewSet, base_name='user')
router.register(r'auth', AuthMethod, base_name='auth')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^profile/$', views.ProfileView.as_view()),
]
