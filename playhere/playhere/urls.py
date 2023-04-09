from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.main, name ="main"),
    path('accounts/',include('account.urls')),
    path('quiz/',include('quiz.urls')),
    path('ch/',include('challenge.urls')),
    path('feedback/',include('feedback.urls')),
    path('result/',include('result.urls')),
    path('certificate/',include('Certificate.urls')),
    path('contactus/',include('contactus.urls')),
    path('api/',include('api.urls')),
    path('downloadapp/',include('downloadapp.urls')),
    path('points/',include('points.urls')),
    path('add/',include('addquestion.urls')),
    path('adminview/',include('adminview.urls')),
    path('codeajgpt/',include('codeAjGPT.urls')),
    path('eplayhere/',include('eplayhere.urls')),

]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()