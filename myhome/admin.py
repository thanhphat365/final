from django.contrib import admin
from .models import Post,Comment
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title','description','create_at','category'
    ]

admin.site.register(Post, BlogAdmin)
admin.site.register(Comment)
# Register your models here.
