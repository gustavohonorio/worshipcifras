from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name='index'),
    path('logon/', include('django.contrib.auth.urls')),
    path('staff/', include('wcstaff.urls')),
    path('cifras/', include('wccifras.urls')),
    path('artistas/', include('wcartista.urls')),
    path('ministerio/', include('wcministerio.urls')),

]
