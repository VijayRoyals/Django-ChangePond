from django.urls import path
from . import views


urlpatterns = [
    path('<int:week>',views.week_details_num),
    path('<str:week>',views.week_Details,name='week_detail')
]