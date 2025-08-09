from django.contrib import admin
from .models import Menuitem

class MenuItemAdmin(admin.ModelAdmin):
    list_display=('name','price')
    search_fields=('name',)





# Register your models here.
admin.site.register(MenuItem,MenuItemAdmin))