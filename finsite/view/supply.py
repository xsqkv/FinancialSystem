from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from finsite.serializer import SupplySerializer
from finsite.models import Supply
import django_filters.rest_framework

from finsite.service.analytics.supply_count_by_year import supply_count_by_year



class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
    #permission_classes = [permissions.IsAuthenticated]
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['name', 'surname', 'patronymic', 'email', 'date_birth', 'gender']

    @action(detail=False, methods=['get'], url_path='analytics/supply_count_by_year')
    def supply_count_by_year(self, request, pk=None, *args, **kwargs):
        return Response(
            {"supply_count": supply_count_by_year(request.GET.get('year', '2023'))},
            status=status.HTTP_200_OK
        )