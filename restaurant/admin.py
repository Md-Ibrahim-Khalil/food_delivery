from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Restaurant, RestaurantAdmin)
