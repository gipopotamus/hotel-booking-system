from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
app_name = 'guest'

urlpatterns = [
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
