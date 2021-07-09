from django.contrib import admin
from .models import Ordering

# Register your models here.




admin.site.site_header= 'Gomadevi Sweater Uudhyog'

admin.site.site_title= 'Gomadevi Sweater Uudhyog'
admin.site.index_title= 'Admin Dashboard'

class Orderingadmin(admin.ModelAdmin):
    list_display = ('username','colour', 'size','quantity','Total','ordered_date', 'delivered_date','verified','delivered')

admin.site.register(Ordering,Orderingadmin)
