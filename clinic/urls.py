
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('clinic/', include('Clinic.urls'))
]
