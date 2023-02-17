from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from applications.car_showroom_app.models import (CarShowroomSale,
                                                  CarsShowroom, Showroom)
from applications.car_showroom_app.serializers import (
    CreateShowroomSerializer, GetShowroomCarSerializer,
    SetShowroomSaleSerializer)
from applications.extensions.mixins import GetCreateMixin


class ShowroomViewSet(GetCreateMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateShowroomSerializer
    queryset = Showroom.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GetShowroomCarViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetShowroomCarSerializer
    queryset = CarsShowroom.objects.all()


class SetShowroomSaleViewSet(GetCreateMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = SetShowroomSaleSerializer
    queryset = CarShowroomSale.objects.all()
