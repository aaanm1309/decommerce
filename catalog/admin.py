from django.contrib import admin

# Register your models here.

from catalog.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    # fields = ['name', 'category', 'price']

    search_fields = ['name', 'slug']

    list_filter = ['name', 'created', 'modified']

    list_display = ['name', 'slug', 'created', 'modified']

    # list_editable = ['length']


class ProductAdmin(admin.ModelAdmin):
    # fields = ['name', 'category', 'price']

    search_fields = ['name', 'category', 'description']

    list_filter = ['category', 'price', 'created', 'modified']

    list_display = ['name', 'category', 'price']

    # list_editable = ['length']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)