from django.contrib import admin
from .models import Recipes, Category, Comments


class RecipesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'published']
    list_filter = ['author', 'published']
    search_fields = ['description']
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ['author']
    date_hierarchy = 'published'
    ordering = ['published']


admin.site.register(Recipes, RecipesAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(Category, CategoryAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'recipe', 'created', 'active']
    list_filter = ['created', 'updated', 'active']
    search_fields = ['body', 'email', 'name']


admin.site.register(Comments, CommentsAdmin)