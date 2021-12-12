
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('accounts/', include('allauth.urls')),
    path('myclub/', include('myclub.urls')),
    path(
        "loaderio-575bf839274838b537e06b3c64230c9e.txt",
        TemplateView.as_view(template_name="loaderio-575bf839274838b537e06b3c64230c9e.txt", content_type="text/plain"),
    ),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)