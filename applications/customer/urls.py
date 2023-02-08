from django.urls import include, path
from rest_framework_nested import routers

from applications.customer import views

router = routers.DefaultRouter()
router.register('customer', views.CustomerViewSet, 'customer')
router.register('location', views.LocationViewSet, 'location')
domain_router = routers.NestedSimpleRouter(
    router, 'customer', lookup='customer')
domain_router.register('offer', views.CreateOfferViewSet, 'offer')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(domain_router.urls)),
]
