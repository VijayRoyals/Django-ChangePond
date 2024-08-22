
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page,name='landing-page'),
    path('<int:id>', views.user_details_id,name='user-detail'),

    path('all-post', views.all_post,name='all-post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
