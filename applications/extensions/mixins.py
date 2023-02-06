from rest_framework import mixins, viewsets


class GetCreateMixin(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass
