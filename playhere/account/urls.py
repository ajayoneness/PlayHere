from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as av


urlpatterns = [
    # path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),

    #reset password urls
    path('password_reset/',av.PasswordResetView.as_view(),name="password_reset"),
    path('password_reset/done/',av.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',av.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset/done/',av.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]
