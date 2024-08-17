from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, RetrieveAPIView

from main.models import Car, CarBrand
from main.serializers import BrandSerializer, CarBrandSingleSerializer, CarSerializer



class BrandListView(ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = BrandSerializer


# @api_view(['GET'])
# def brand_view(request, pk):
#     item = CarBrand.objects.get(id=pk)
#     brand = item.cars
#     serializers = CarSerializer(brand , many=True)
#     return Response(serializers.data)


class BrandDetailView(RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSingleSerializer