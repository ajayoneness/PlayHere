from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.downloadApp, name="downloadapp"),
    path('d/', views.download_file, name='download_file'),

]
