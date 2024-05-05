from django.contrib import admin
from .models import Post

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ("__str__", "author")
    list_filter = ("author",)