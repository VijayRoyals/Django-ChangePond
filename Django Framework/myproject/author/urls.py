
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('<int:id>', views.Author_details_id,name='author-detail'),

    path('<slug:slug>', views.Author_details_slug),
    path('<str:author>', views.Author_details,name='author-detail'),
]
