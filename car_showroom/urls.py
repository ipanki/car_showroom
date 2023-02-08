from django.contrib import admin
from django.urls import include, path

v1_urls = [path('', include('applications.customer.urls')),
           path('', include('applications.supplier.urls')),
           path('', include('applications.car_showroom_app.urls')),
           path('', include('applications.authentication.urls')),
           ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1_urls)),
]
