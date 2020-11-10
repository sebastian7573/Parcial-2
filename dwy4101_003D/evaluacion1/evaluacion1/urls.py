from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('gestorDeJuegos.urls')),


] 
#127.0.0.1:8000/


#PA LAS FOTOS BRO
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)