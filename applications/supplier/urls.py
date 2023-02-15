from django.urls import include, path
from rest_framework_nested import routers

from applications.supplier import views

router = routers.DefaultRouter()
router.register('supplier', views.SupplierViewSet, 'supplier')
domain_router = routers.NestedSimpleRouter(
    router, 'supplier', lookup='supplier')
domain_router.register('cars', views.GetSupplierCarViewSet, 'supplier_cars')
domain_router.register(
    'set_discount', views.SetSupplierSaleViewSet, 'set_discount')
domain_router.register('report', views.ReportsViewSet, 'report')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(domain_router.urls)),

]
