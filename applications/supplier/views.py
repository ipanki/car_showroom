from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from applications.extensions.mixins import GetCreateMixin
from applications.supplier.models import CarSupplier, Supplier, SupplierSale
from applications.supplier.serializers import (CreateSupplierSerializer,
                                               GetSupplierCarSerializer,
                                               ReportSerializer,
                                               SetSupplierSaleSerializer)
from applications.supplier.services import get_summary_report


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


class ReportsViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def summary(self, request, supplier_pk):
        report = get_summary_report(supplier_pk)
        return Response(status=status.HTTP_200_OK, data=ReportSerializer(
            {"report": report}).data)
