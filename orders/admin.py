from django.contrib import admin
from.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display=('id','customer','total_amount','status','created_at')
    list_filter=('status',)
    search_fields=('customer__username',)
admin.site.register(Order,OrderAdmin)

# Register your models here.
