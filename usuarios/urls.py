from django.urls import path, include

urlpatterns = [
   #path(),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
