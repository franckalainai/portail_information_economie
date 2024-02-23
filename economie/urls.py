from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('actualites/', include('actualite.urls')),
    path('publications/', include('publication.urls')),
    path('summernote/', include('django_summernote.urls')), 
    path('admin/', admin.site.urls), 
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
