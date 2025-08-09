from django.contrib import admin
from .models import Menuitem
import models import menuitem

class MenuItemAdmin(admin.ModelAdmin):
    list_display=('name','price')
    search_fields=('name',)





# Register your models here.
admin.site.register(MenuItem,MenuItemAdmin))