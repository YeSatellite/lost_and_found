from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('customauth.urls')),
    url(r'^post/', include('post.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
