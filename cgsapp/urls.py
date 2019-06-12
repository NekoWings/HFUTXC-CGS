from django.urls import path, include 
from . import views

urlpatterns = [
    path('add_book', views.add_book, ),
    path('show_books', views.show_books, ),
    path('get_blank_map',views.get_blank_map, ),
    path('get_start',views.get_start, ),
    path('get_end',views.get_end, ),
    path('get_route',views.get_route, ),
    path('get_map',views.get_map, ),
    path('img_test', views.img_test, ),
]