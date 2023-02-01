from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from applications.car_showroom_app.models import (CarShowroomSale,
                                                  CarsShowroom, Showroom)
from applications.car_showroom_app.serializers import (
    CreateShowroomSerializer, GetShowroomCarSerializer,
    SetShowroomSaleSerializer)


class ShowroomViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateShowroomSerializer
    queryset = Showroom.objects

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GetShowroomCarViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetShowroomCarSerializer
    queryset = CarsShowroom.objects


class SetShowroomSaleViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SetShowroomSaleSerializer
    queryset = CarShowroomSale.objects
