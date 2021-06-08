from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=240)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
        
        

class Color(models.Model):
    name = models.CharField(max_length=50)
    car_makes = models.ManyToManyField("CarMake")

    def __str__(self):
        return self.name


class CarMake(models.Model):
    CHOICES = (
        ("Estate", "estate"),
        ("Coupe", "coupe"),
        ("Sedan", "sedan"),
        ("Hachback", "hachback"),
    )

    name = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50, choices=CHOICES)
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE)
    model = models.OneToOneField(
        "CarModel",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class CarModel(models.Model):
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.model


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    residence = models.ForeignKey("Residence", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Residence(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.country}"
