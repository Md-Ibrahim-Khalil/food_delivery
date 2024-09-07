from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'price')  
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Item, ItemAdmin)