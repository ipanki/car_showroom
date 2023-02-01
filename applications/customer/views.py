from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from applications.car_showroom_app.models import Location
from applications.customer.models import Customer, Offer
from applications.customer.serializers import (CreateCustomerSerializer,
                                               LocationSerializer,
                                               OfferSerializer)


class CustomerViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateCustomerSerializer
    queryset = Customer.objects

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LocationViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    queryset = Location.objects


class CreateOfferViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OfferSerializer
    queryset = Offer.objects
