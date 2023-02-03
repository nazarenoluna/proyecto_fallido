
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from viajeros.views import inicio


urlpatterns = [
    path('', inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('plataforma/', include('viajeros.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)