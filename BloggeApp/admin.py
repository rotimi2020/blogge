from django.contrib import admin

from .models import Contact, Blog_Post

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at','is_clicked']
    list_filter = ['created_at']

@admin.register(Blog_Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'category', 'is_top_post', 'is_trending', 'created_at'] 
    list_filter = ['created_at', 'author' , 'is_top_post', 'is_trending'] 
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    