from django.contrib import admin
from .models import News, Category, Customer, BlogComment


class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'body', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(News, AdminNews)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(BlogComment)
