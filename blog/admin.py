from django.contrib import admin
from .models import Post,Comment

# Register your models here.

admin.site.site_header = "Digital Campus"
admin.site.site_title = "Digital Campus"
admin.site.index_title = "Welcome to Digital Campus"
# admin.site.register(Post)

 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','created_on' )
    list_filter = ('title','author','content')
    


