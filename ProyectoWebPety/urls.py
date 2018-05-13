from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ProyectoWebPety.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pety/', include('apps.pety.urls')),
    url(r'^login/', include('apps.pety.urls')),
    url(r'^contacto/', include('apps.pety.urls'))
]
