from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include # Para incluir las urls de otras apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('serviceRepairBackEnd.urls')) # Para incluir las urls de otras apps
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

