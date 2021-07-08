from django.contrib import admin
from .models import Room, Message

# Register your models here.
admin.site.site_header = "Digital Campus"
admin.site.site_title = "Digital Campus"
admin.site.index_title = "Welcome to Digital Campus"








class AdminRoom(admin.ModelAdmin):
	list_display = ["id","name"]
	list_filter = ["id","name"]
	search_fields = ["name"]

class AdminMessage(admin.ModelAdmin):
	list_display = ["id","value"]
	list_filter = ["id","value","user"]
	search_fields = ["value"]



admin.site.register(Room,AdminRoom)
admin.site.register(Message,AdminMessage)