from django.urls import path

from . import views

urlpatterns = [
    path('programs/', views.ProgramList.as_view(), name='programs'),
    path('program/<int:pk>/', views.ProgramView.as_view(), name='program'),  # TODO: name into Url
    path('search/', views.SearchList.as_view(), name='search'),
    path('', views.Index.as_view(), name='index'),
]
