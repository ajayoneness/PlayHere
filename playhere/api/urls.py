from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("user/",views.userapi, name='userapi'),
    path("feedbackapi/",views.feedbackapi, name='feedbackapi'),
    path("profileapi/",views.profileapi, name='profileapi'),
    path("pointsapi/",views.pointsapi, name='pointsapi'),
    path("test/",views.test,name="test"),
    path('codeajgptapi/', views.codeajgptAPI.as_view(), name='codeajgptapi'),
    path('certificateapi/', views.certificateAPI.as_view(), name='certificateapi'),
]

