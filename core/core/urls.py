from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Blog-D Dashboard"
admin.site.site_header = "Blog-D"
admin.site.site_title = "Blog-D"

