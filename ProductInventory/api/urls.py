from django.urls import path
from .views import (
    NewProductView,
    ProductListView,
    AvailableProductListView,
    UnavailableProductListView,
    ProductStatusUpdateView,
)


urlpatterns = [
    path('products/new', NewProductView.as_view(), name='new-product'),
    path('products', ProductListView.as_view(), name='products'),
    path('products/available', AvailableProductListView.as_view(), name='available-products'),
    path('products/unavailable', UnavailableProductListView.as_view(), name='unavailable-products'),
    path('products/status/<int:product_id>', ProductStatusUpdateView.as_view(), name='product-status-update'),
]
