import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from applications import urls

v1_urls = [
    path('', include('applications.customer.urls')),
    path('', include('applications.supplier.urls')),
    path('', include('applications.car_showroom_app.urls')),
    path('', include('authemail.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_urls)),
]

if settings.DEBUG:
    urlpatterns += [
        path('swagger(?P\.json|\.yaml)', urls.schema_view.without_ui(
            cache_timeout=0), name='schema-json'),
        path('swagger/', urls.schema_view.with_ui('swagger',
             cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', urls.schema_view.with_ui('redoc',
             cache_timeout=0), name='schema-redoc'),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
