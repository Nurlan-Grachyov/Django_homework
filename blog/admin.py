from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "viewing")
    list_filter = ("name",)
    search_fields = ("name", "description")