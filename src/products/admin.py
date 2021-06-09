from django.contrib import admin
from django.contrib.admin.decorators import register

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
admin.site.register(CarModel)




# If want to register the model with decorator
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name", "car_type", "owner", "model")
    list_display_links = ("name",)


class InLineOwner(admin.TabularInline):
    model = Owner
    extra = 1
    max_num = 1


class InLineCarMake(admin.TabularInline):
    model = CarMake
    extra = 1


@admin.register(Residence)
class ResidenceAdmin(admin.ModelAdmin):
    inlines = [InLineOwner]
    list_display = ("city", "country")


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    inlines = [InLineCarMake]
    list_display = ("first_name", "last_name", "residence")


# To register custom admin model without decorator, 
# we need to put the cutomAdmin as an extra arg in register()

# admin.site.register(CarMake, CarMakeAdmin)
# admin.site.register(Owner, OwnerAdmin)
# admin.site.register(Residence, ResidenceAdmin)