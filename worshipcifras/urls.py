from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name='index'),
    path('acesso/', include('core.urls')),  # acessando aplicação enquanto a pre alfa estiver ativa
    path('logon/', include('django.contrib.auth.urls')),
    path('artistas/', include('wcartista.urls')),
    path('cifras/', include('wccifras.urls')),
    path('staff/', include('wcstaff.urls')),

]
