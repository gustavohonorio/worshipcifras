from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name='index'),
    path('logon/', include('django.contrib.auth.urls')),
    path('staff/', include('wcstaff.urls')),
    path('cifras/', include('wccifras.urls')),
    path('artistas/', include('wcartista.urls')),
    # path('ministerio/', include('wcministerio.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
