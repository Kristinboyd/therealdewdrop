from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from users.models import Profile
from products.models import Product

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user;
    profile = Profile.objects.get(user=user)
    all_products = profile.products.all()

    return render(request, 'users/profile.html', {'products': all_products})

@login_required()
def remove_from_profile(request, **kwargs):
    # Get Profile given the logged in User
    print(str(request.user) + 'LOOK HERE')
    user = request.user;
    profile = Profile.objects.get(user=user)

    # Add Passed in Product to the Profile
    product_name = request.GET.get('product_name')
    print(product_name)
    product = Product.objects.get(name=product_name)

    # Save it to DB
    profile.products.remove(product)
    profile.save()

    # TODO: Do not render about.html
    # return render(request, 'products/products.html')
    return redirect("profile:profile")