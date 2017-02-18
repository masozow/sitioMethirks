from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('pagina.urls'))
] + static(settings.MEDIA_URL, docment_root=settings.MEDIA_ROOT) #comentar esto cuando Debug=False
