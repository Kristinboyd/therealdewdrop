from django.db import models

# Create your models here.
class Product(models.Model):

    DRY = "DRYNESS"
    OIL = "OILY"
    ACNE = "ACNE"
    AGE = "AGING"
    ROSE = "ROSACEA"
    NONE = "NONE"

    TREATMENT_TYPE = (
        ("DRY", "Dryness"),
        ("OIL", "Oily"),
        ("ACNE", "Acne"),
        ("AGE", "Aging"),
        ("ROSE", "Rosacea"),
        ("NONE", "None")
    )

    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    treatment_type = models.CharField(max_length=20, choices=TREATMENT_TYPE, default="NONE")
    link = models.URLField()

    def __str__(self):
        return self.name