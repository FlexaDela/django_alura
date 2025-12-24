from django.urls import path, include
from .views import login, cadastro, logout
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('login/', login, name='login'),
   path('cadastro/', cadastro, name='cadastro'),
   path('logout/', logout, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
