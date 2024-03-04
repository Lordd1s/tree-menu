from django.contrib import admin
from app import models


# Register your models here.
class TreeAdmin(admin.ModelAdmin):
    list_fields = ('name', 'url')
    list_filter = ('name', )
    search_fields = ('name', )


admin.site.register(models.TreeMenu, TreeAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_fields = ('name', 'slug', 'parent')
    list_filter = ('name', 'parent')
    search_fields = ('name', 'parent')


admin.site.register(models.Item, ItemAdmin)
