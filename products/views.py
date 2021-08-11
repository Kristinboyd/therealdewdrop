from typing import ContextManager
from rest_framework import generics
from products.models import Product
from django.views.generic import ListView
from users.models import Profile
from products.serializers import ProductSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ListProducts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'products/products.html'

    def get(self, request):
        queryset = Product.objects.all()
        return Response({'products': queryset})

class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pass


class ProductGetByCondition(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        tc = self.request.GET.get('treatment_type')
        return Product.objects.filter(treatment_type=tc)

@login_required()
def add_to_profile(request, **kwargs):
    # Get Profile given the logged in User
    print(str(request.user) + 'LOOK HERE')
    user = request.user;
    profile = Profile.objects.get(user=user)

    # Add Passed in Product to the Profile
    product_name = request.GET.get('product_name')
    print(product_name)
    product = Product.objects.get(name=product_name)

    # Save it to DB
    profile.products.add(product)
    profile.save()

    # TODO: Do not render about.html
    # return render(request, 'products/products.html')
    return redirect("profile:profile")
# kwargs are dict_keys([‘_auth_user_id’, ‘_auth_user_backend’, ‘_auth_user_hash’])