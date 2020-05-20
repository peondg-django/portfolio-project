from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
