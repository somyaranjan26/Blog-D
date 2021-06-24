from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish', 'slug', 'status', 'category')
    list_editable = ['status']
    list_filter = ('category', 'status')
    search_fields = ('title', 'slug')
    prepopulated_fields = {
        "slug": ("title",),
    }

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "email", "publish", "status")
    list_filter = ("status", "publish")
    search_fields = ('name', 'email', 'content')