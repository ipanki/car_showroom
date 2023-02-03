import debug_toolbar

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('applications.customer.urls')),
    path('api/v1/', include('applications.supplier.urls')),
    path('api/v1/', include('applications.car_showroom_app.urls')),
    path('api/v1/', include('applications.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
