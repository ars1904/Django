from django.contrib import admin
from .models import Articles, Tag, Category


admin.site.register(Category)


def clear_rating(modeladmin, request, queryset):
    queryset.update(rating=1)


clear_rating.short_description = "Выставить рейтинг = 1"


def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'has_image', 'rating', 'is_active']
    actions = [clear_rating, set_active]


admin.site.register(Articles, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    #list_display = ['name', 'is_active']
    actions = [set_active]


admin.site.register(Tag, TagAdmin)
