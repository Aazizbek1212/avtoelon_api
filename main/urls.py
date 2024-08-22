from django.urls import path

from main.views import BrandDetailView, BrandListView, CardetailView, CarsView


urlpatterns = [
    path('brand/', BrandListView.as_view(), name='brand'),
    path('cars/', CarsView.as_view(), name='car'),
    path('brands/<int:pk>/',BrandDetailView.as_view(), name='cars'),
    path('car/<int:pk>/', CardetailView.as_view(), name='car_detail'),
]
