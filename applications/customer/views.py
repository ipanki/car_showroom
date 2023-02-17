from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from applications.car_showroom_app.models import Location
from applications.customer.models import Customer, Offer
from applications.customer.serializers import (CreateCustomerSerializer,
                                               LocationSerializer,
                                               OfferSerializer,
                                               ReportSerializer)
from applications.customer.services import get_summary_report
from applications.extensions.mixins import GetCreateMixin


class CustomerViewSet(GetCreateMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateCustomerSerializer
    queryset = Customer.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LocationViewSet(GetCreateMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class CreateOfferViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class ReportsViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def summary(self, request, customer_pk):
        report = get_summary_report(customer_pk)
        return Response(status=status.HTTP_200_OK, data=ReportSerializer(
            {"report": report}).data)
