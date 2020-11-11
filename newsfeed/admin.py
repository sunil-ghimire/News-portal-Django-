from django.contrib import admin
from .models import News, Category, Customer, Comment


class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'body', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')


# Register your models here.
admin.site.register(News, AdminNews)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
