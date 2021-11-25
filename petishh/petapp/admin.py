from django.contrib import admin
from django.contrib.admin.options import ModelAdmin


# Register your models here.
from .models import Category, Product,Profileinfo, Users

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name', 'slug']
    prepopulated_fields={'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','author', 'slug', 'price','in_stock','created', 'updated']
    list_filter=['in_stock', 'is_active']
    list_editable=['price','in_stock']
    prepopulated_fields={'slug':('title',)}


@admin.register(Profileinfo)
class ProfileinfoAdmin(admin.ModelAdmin):
    list_display=['id','user',]

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display=['id','email','username','phone_no','last_login','is_staff','is_active','is_superuser',]
