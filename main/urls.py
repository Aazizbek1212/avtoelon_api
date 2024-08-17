from django.urls import path

from main.views import BrandDetailView, BrandListView


urlpatterns = [
    path('brand/', BrandListView.as_view(), name='brand'),
    path('brands/<int:pk>/',BrandDetailView.as_view(), name='cars'),
]
