from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.profile1, name ="profile"),
    path("category/",views.cate, name ="category"),
    path('ques/<int:idd>',views.ques,name="question"),
    path('result/<int:slis>',views.result,name='result'),
    path('certification/',views.certificate, name='certificate'),
    path('loaddata/',views.loaddata, name='loaddata')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
