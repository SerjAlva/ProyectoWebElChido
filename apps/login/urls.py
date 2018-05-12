from django.conf.urls import include, url
from apps.login.views import login

urlpatterns = [
     url(r'^$', login),
]
