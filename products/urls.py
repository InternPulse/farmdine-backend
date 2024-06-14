from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view({'get': 'list'}), name='list_product'),
    path('create', ProductCreateView.as_view({'post': 'create'}), name='add_product'),
    path('details/<int:product_id>', ProductDetailView.as_view(), name='product_details'),
    path('update/<int:product_id>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:product_id>', ProductDeleteView.as_view(), name='delete_product'),
]
