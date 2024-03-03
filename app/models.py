from django.db import models


# Create your models here.
class TreeMenu(models.Model):
    name = models.CharField(max_length=50)
    url = models.TextField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        app_label = 'app'
        ordering = ('parent', 'name')
        verbose_name = 'TreeMenu'
        verbose_name_plural = 'TreeMenus'

    def __str__(self):
        return self.name
