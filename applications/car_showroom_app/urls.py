from django.urls import include, path
from rest_framework_nested import routers

from applications.car_showroom_app import views

router = routers.DefaultRouter()
router.register('showroom', views.ShowroomViewSet, 'showroom')

domain_router = routers.NestedSimpleRouter(
    router, 'showroom', lookup='showroom')
domain_router.register('cars', views.GetShowroomCarViewSet, 'showroom_cars')
domain_router.register(
    'set_discount', views.SetShowroomSaleViewSet, 'set_discount')
domain_router.register('report', views.ReportsViewSet, 'report')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(domain_router.urls)),
]
