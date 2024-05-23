from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from finsite.serializer import CategorySerializer
from finsite.models import Category
import django_filters.rest_framework

from finsite.service.analytics.category import category_order_count


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='analytics/category_order_count')
    def category_order_count(self, request, *args, **kwargs):
        return Response(
            {"category_total_order": category_order_count(kwargs["pk"])},
            status=status.HTTP_200_OK
        )
