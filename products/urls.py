from django.urls import path
from products.views import products_view, detail_view


urlpatterns = [
    path('products/', products_view),
    path('products/<int:id>/', detail_view)
]
