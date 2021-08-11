from django.urls import path, re_path
from products.views import CreateProduct, ProductDetail, ProductGetByCondition, remove_from_profile, add_to_profile, ListProducts

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view(), name='detailcreate'),
    path('add-product', CreateProduct.as_view(), name='listcreate'),
    path('', ListProducts.as_view(), name='listproducts'),
    path('add_to_profile/', add_to_profile),
    path('remove_from_profile/', remove_from_profile),
    re_path('filter/(?P<username>\w{0,50})/$', ProductGetByCondition.as_view()),
]