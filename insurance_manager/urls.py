from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path('', include(('insurance.urls', 'insurance'), namespace='insurance')),
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
]
