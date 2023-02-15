from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from applications.car_showroom_app.models import (CarShowroomSale,
                                                  CarsShowroom, Showroom)
from applications.car_showroom_app.serializers import (
    CreateShowroomSerializer, GetShowroomCarSerializer, ReportSerializer,
    SetShowroomSaleSerializer)
from applications.car_showroom_app.services import get_summary_report
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


class ReportsViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def summary(self, request, showroom_pk):
        incomes, expenses = get_summary_report(showroom_pk)
        return Response(status=status.HTTP_200_OK, data=ReportSerializer(
            {"incomes": incomes,
             "expenses": expenses
             }).data)
