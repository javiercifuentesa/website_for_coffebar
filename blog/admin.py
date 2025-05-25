from django.contrib import admin
from .models import Post, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'published', 'author', 'post_categories')
    list_filter = ('published', 'author__username', 'categories__name')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    # prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published'
    ordering = ['-published']

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)