from django.contrib import admin
from app import models


# Register your models here.
class TreeAdmin(admin.ModelAdmin):
    list_fields = ('name', 'url', 'parent')
    list_filter = ('name', 'parent')
    search_fields = ('name', 'parent')


admin.site.register(models.TreeMenu, TreeAdmin)
