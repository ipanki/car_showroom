from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from applications.extensions.mixins import GetCreateMixin
from applications.supplier.models import CarSupplier, Supplier, SupplierSale
from applications.supplier.serializers import (CreateSupplierSerializer,
                                               GetSupplierCarSerializer,
                                               SetSupplierSaleSerializer)


class SupplierViewSet(GetCreateMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateSupplierSerializer
    queryset = Supplier.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GetSupplierCarViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetSupplierCarSerializer
    queryset = CarSupplier.objects.all()


class SetSupplierSaleViewSet(GetCreateMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = SetSupplierSaleSerializer
    queryset = SupplierSale.objects.all()
