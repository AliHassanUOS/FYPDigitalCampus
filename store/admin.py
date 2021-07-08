from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
from .models import Order

admin.site.site_header = "Digital Campus"
admin.site.site_title = "Digital Campus"
admin.site.index_title = "Welcome to Digital Campus"

class AdminProduct(admin.ModelAdmin):
	list_display = ['id', 'name','price','category', 'date','Teacher','department']
	list_filter = ['id', 'name','Teacher','price']
	search_fields = ["name"]

class AdminCategory(admin.ModelAdmin):
	list_display = ['id','name']
	list_filter = ['id', 'name']
	search_fields = ["name"]



class AdminCustomer(admin.ModelAdmin):
	list_display = ["id","name", "email", "phone"]
	list_filter = ["id","name","phone", "email"]
	search_fields = ["name"]

class AdminOrder(admin.ModelAdmin):
	list_display = ["id","product", "customer", "price",'phone','completed','date']
	list_filter = ["id","product","price", "date"]
	search_fields = ["product"]





admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrder)
