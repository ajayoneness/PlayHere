from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.main, name ="main"),
    path('account/',include('account.urls')),
    path('quiz/',include('quiz.urls')),
    path('ch/',include('challenge.urls')),
    path('feedback/',include('feedback.urls')),
    path('result/',include('result.urls')),
    path('certificate/',include('Certificate.urls')),
    path('contactus/',include('contactus.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
