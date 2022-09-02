from django.contrib import admin
from django.urls import path, include

from wcartista.urls import router_artistas
from wclogon.urls import router_usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name='index'),
    path('logon/', include('django.contrib.auth.urls')),
    path('staff/', include('wcstaff.urls')),
    path('cifras/', include('wccifras.urls')),
    path('artistas/', include('wcartista.urls')),
    # path('ministerio/', include('wcministerio.urls')),

    # DRF
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router_usuarios.urls)),
    path('api/v1/', include(router_artistas.urls)),

]
