from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def error404(request, exception):
    return render(request, '404.html', status=404)

urlpatterns = [
    path('alpha-user/', admin.site.urls),
    path('', include('blog.urls')),
    path('users/', include('user.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error404