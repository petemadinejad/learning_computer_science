from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('title', 'content')
