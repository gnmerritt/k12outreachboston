from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from . import views
from .sitemaps import maps

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': maps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('programs/', views.ProgramList.as_view(), name='programs'),
    path('program/<int:pk>/', views.program_redirector),
    re_path(r'^program\/(\w+\-)+p(?P<pk>\d+)\/?$',
            views.ProgramView.as_view(), name='program'),
    path('search/', views.SearchList.as_view(), name='search'),
    path('terms', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    path('', views.Index.as_view(), name='index'),
]
