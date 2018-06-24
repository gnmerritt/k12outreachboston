from django.urls import path, re_path

from . import views

urlpatterns = [
    path('programs/', views.ProgramList.as_view(), name='programs'),
    path('program/<int:pk>/', views.program_redirector),
    re_path(r'^program\/(\w+\-)+p(?P<pk>\d+)\/?$',
            views.ProgramView.as_view(), name='program'),
    path('search/', views.SearchList.as_view(), name='search'),
    path('', views.Index.as_view(), name='index'),
]
