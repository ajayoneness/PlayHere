from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("user/",views.userapi, name='userapi'),
    path("feedbackapi/",views.feedbackapi, name='feedbackapi'),
    path("profileapi/",views.profileapi, name='profileapi'),
    path("pointsapi/",views.pointsapi, name='pointsapi'),
    path("test/",views.test,name="test")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
