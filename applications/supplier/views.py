from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from applications.supplier.models import CarSupplier, Supplier, SupplierSale
from applications.supplier.serializers import (CreateSupplierSerializer,
                                               GetSupplierCarSerializer,
                                               SetSupplierSaleSerializer)


class SupplierViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateSupplierSerializer
    queryset = Supplier.objects

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GetSupplierCarViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetSupplierCarSerializer
    queryset = CarSupplier.objects


class SetSupplierSaleViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SetSupplierSaleSerializer
    queryset = SupplierSale.objects
