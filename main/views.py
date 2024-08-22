from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView

from main.filters import CarFilter
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


class CarsView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['brand', 'price', 'name']
    filterset_class = CarFilter


class CardetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

