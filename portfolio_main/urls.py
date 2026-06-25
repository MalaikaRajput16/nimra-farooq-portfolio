from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path('', views.home, name='home'),  # ADD THIS LINE!
    path('admin/', admin.site.urls),
    # Add your app URLs here if needed
    # path('', include('bio.urls')),
]

# Add this at the very bottom of the file
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)