from django.contrib import admin

# Register your models here.
from .models import (
    Product,
    Color,
    CarMake,
    CarModel,
    Owner,
    Residence,
)


admin.site.register(Product)
admin.site.register(Color)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Owner)
admin.site.register(Residence)
