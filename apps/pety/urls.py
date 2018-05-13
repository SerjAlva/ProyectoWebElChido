from django.conf.urls import include, url

from apps.pety import views
from apps.pety.views import index, servicios, login, contacto, registrarse
urlpatterns = [
     url(r'^$', index, name="pety"),
     url(r'^servicios/$', servicios, name="servicios"),
     url(r'^login/$', login, name="login"),
     url(r'^contacto/$', contacto, name="contacto"),
     url(r'^registrarse/', registrarse, name="registrarse"),
]
