from django.db import models

# Create your models here.
class Product(models.Model):

    TREATMENT_TYPE = (
        ("Dryness", "Dryness"),
        ("Oily", "Oily"),
        ("Acne", "Acne"),
        ("Aging", "Aging"),
        ("Rosacea", "Rosacea"),
        ("None", "None")
    )

    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    treatment_type = models.CharField(max_length=20, choices=TREATMENT_TYPE, default="NONE")
    link = models.URLField()

    def __str__(self):
        return self.name