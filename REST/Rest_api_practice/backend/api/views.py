import json
from xml.etree.ElementInclude import include
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View for Home Page"""
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
