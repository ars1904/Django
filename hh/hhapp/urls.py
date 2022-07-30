from django.urls import path
from hhapp import views



appname = 'hhapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('create/', views.create_post, name='create'),
    path('post/<int:id>/', views.post, name='post'),
]

