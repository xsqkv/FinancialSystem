from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from finsite.serializer import CustomerSerializer
from finsite.models import Employee
import django_filters.rest_framework

from finsite.service.analytics.employee_salaries import get_employee_salaries


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = CustomerSerializer
    #permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'surname', 'patronymic', 'email', 'date_birth', 'gender']

    @action(detail=False, methods=['get'], url_path='analytics/employee_salaries')
    def employee_salaries(self, request, pk=None, *args, **kwargs):
        return Response(
            {"employee_salaries": get_employee_salaries()},
            status=status.HTTP_200_OK
        )