from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Menu, MenuAdmin)