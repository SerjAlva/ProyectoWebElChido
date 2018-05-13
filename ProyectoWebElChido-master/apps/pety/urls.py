from django.conf.urls import include, url
from apps.pety.views import index
urlpatterns = [
     url(r'^$', index),
]
