from django.db import models


# Create your models here.
class TreeMenu(models.Model):
    name = models.CharField(max_length=50)
    url = models.SlugField(max_length=20)

    class Meta:
        app_label = 'app'
        ordering = ('name',)
        verbose_name = 'TreeMenu'
        verbose_name_plural = 'TreeMenus'

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    menu = models.ForeignKey(TreeMenu, on_delete=models.PROTECT, related_name='items')
    slug = models.SlugField(max_length=20)

    class Meta:
        app_label = 'app'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'