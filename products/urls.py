from django.urls import path, re_path
from products.views import ProductList, ProductDetail, ProductGetByCondition, add_to_profile

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetail.as_view(), name='detailcreate'),
    path('', ProductList.as_view(), name='listcreate'),
    re_path(r'^add-to-profile/(?P<username>\w{0,50})/$', add_to_profile, name='add_to_profile'),
    re_path(r'^purchases/(?P<username>\w{0,50})/$', ProductGetByCondition.as_view())
]