from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('programs/', views.ProgramList.as_view(), name='programs'),
    path('program/<int:pk>/', views.Program.as_view(), name='program'),  # TODO: name into Url
    path('', views.Index.as_view(), name='index'),
]
