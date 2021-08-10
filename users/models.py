from django.db import models
from django.contrib.auth.models import User

from products.models import Product

class Profile(models.Model):

    CONDITION_TYPE = (
        ("Dryness", "Dryness"),
        ("Oily", "Oily"),
        ("Acne", "Acne"),
        ("Aging", "Aging"),
        ("Rosacea", "Rosacea"),
        ("None", "None")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skin_concern = models.CharField(max_length=20, choices=CONDITION_TYPE, default="None") 
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'