
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('vijay',views.vijay),
    path('<int:month>', views.monthly_details_num),
    path('<str:month>', views.monthly_details,name='month-detail'),
]
