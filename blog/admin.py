from django.contrib import admin
from .models import Post, Category, Contact, Comment, Newsletter


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'subject']


@admin.register(Newsletter)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['email']
