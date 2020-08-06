from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Placed_Order)
admin.site.register(Order_Item)
admin.site.register(Menu_Item)
admin.site.register(Category)
admin.site.register(Cart)
