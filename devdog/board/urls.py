from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
    path('',views.main, name='boardmain'),
    path('article/',views.home, name='articleview'),
    path('article/new/',views.new, name='new'),
    path('article/create/', views.create, name='create'),
    # path('article/base/', views.base, name='base'),
]