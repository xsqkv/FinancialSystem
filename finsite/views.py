from django.http import JsonResponse
from .models import *
from rest_framework import permissions, viewsets
from .serializers import *
from .service.find_product_by_id import FindProductById


def index(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)
