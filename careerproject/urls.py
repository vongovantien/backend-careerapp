from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from careerapp.admin import admin_site

admin.site.site_header = "HỆ THỐNG QUẢN LÍ TRANG TUYỂN DỤNG"
admin.site.site_title = "Admin"
admin.site.index_title = "CareerApp"

urlpatterns = [
                  path('admin/', admin_site.urls),
                  path('', include('careerapp.urls')),
                  path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
