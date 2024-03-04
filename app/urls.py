from django.urls import path
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('menu/', TemplateView.as_view(
        template_name='index.html',
        extra_context={'title': 'Menu'},
    ), name='index'),
]
