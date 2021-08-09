from rest_framework import generics
from products.models import Product
from users.models import Profile
from products.serializers import ProductSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pass


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
    user = request.user;
    profile = Profile.objects.get(user=user)

    # Add Passed in Product to the Profile
    product_name = request.GET.get('product_name')
    product = Product.objects.get(name=product_name)

    # Save it to DB
    profile.products.add(product)
    profile.save()

    # TODO: Do not render about.html
    return render(request, 'products/about.html')