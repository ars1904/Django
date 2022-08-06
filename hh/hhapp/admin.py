from django.contrib import admin
from .models import Articles, Tag, Category


admin.site.register(Articles)
admin.site.register(Tag)
admin.site.register(Category)
