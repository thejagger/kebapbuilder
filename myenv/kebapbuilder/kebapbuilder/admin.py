from django.contrib import admin

# Register your models here.
from .models import Person, Additional, Type, MainType, Order

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['person']}),
    ]
    list_display = ('person', 'type', 'main_type', 'order_date')

class TypeAdmin(admin.ModelAdmin):
    fields = ['type_name', 'type_price']
    list_display = ('type_name', 'type_price')

class MainTypeAdmin(admin.ModelAdmin):
    fields = ['main_type_name', 'main_type_price']
    list_display = ('main_type_name', 'main_type_price')

class AdditionalAdmin(admin.ModelAdmin):
    fields = ['additional_name', 'additional_price']
    list_display = ('additional_name', 'additional_price')

admin.site.register(Order, OrderAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(MainType, MainTypeAdmin)
admin.site.register(Additional, AdditionalAdmin)