from django.contrib import admin
from .models import Item, Cat
# Register your models here.

# class CatItemInline(admin.TabularInline): 
#     model = Item.cat.through
#     extra = 0
    
# class CatAdmin(admin.ModelAdmin):
#     inlines = [CatItemInline,]
#     model = Cat

admin.site.register(Item)
admin.site.register(Cat)