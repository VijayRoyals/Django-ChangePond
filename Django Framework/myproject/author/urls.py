
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
<<<<<<< HEAD
=======
    path('<int:id>', views.Author_details_id,name='author-detail'),
>>>>>>> c16875dff18e17c347d271cfc7f665766114d9df
    path('<slug:slug>', views.Author_details_slug),
    path('<str:author>', views.Author_details,name='author-detail'),
]
