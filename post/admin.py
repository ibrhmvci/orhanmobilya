from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']

    class Meta:
        model = Post
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)

# Register your models here.
