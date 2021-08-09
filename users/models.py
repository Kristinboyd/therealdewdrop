from django.db import models
from django.contrib.auth.models import User

from products.models import Product

class Profile(models.Model):
    DRY = "DRYNESS"
    OIL = "OILY"
    ACNE = "ACNE"
    AGE = "AGING"
    ROSE = "ROSACEA"
    NONE = "NONE"

    CONDITION_TYPE = (
        ("DRY", "Dryness"),
        ("OIL", "Oily"),
        ("ACNE", "Acne"),
        ("AGE", "Aging"),
        ("ROSE", "Rosacea"),
        ("NONE", "None")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skin_concern = models.CharField(max_length=20, choices=CONDITION_TYPE, default="NONE") 
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'