from django.contrib import admin

from .models import Category, Location, Post


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'is_published',
        'title',
        'description',
        'slug',
    )
    list_editable = (
        'is_published',
        'description',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'is_published',
        'title',
    )
    list_display_links = (
        'title',
        'slug',
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = (
        'name',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'is_published',
        'title',
        'author',
        'text',
        'pub_date',
        'location',
        'category',
        'created_at',
    )
    list_editable = (
        'is_published',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'category',
        'author',
        'location',
        'pub_date',
    )
    list_display_links = (
        'title',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.empty_value_display = 'Не задано'
