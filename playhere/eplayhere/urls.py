from django.urls import path
from . import views


urlpatterns = [
    path('', views.eplayhere, name="eplayhere"),

]
