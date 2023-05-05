from django.db import models
from django.contrib.auth.models import User


class certificateStatic(models.Model):
    c_name = models.CharField(max_length=100,null=True,blank=True)
    c_bg = models.FileField(upload_to='certificateApi/bg/',blank=True,null=True)
    c_main_logo = models.FileField(upload_to='certificateApi/mainlogo/',blank=True,null=True)
    c_logo = models.FileField(upload_to='certificateApi/logo/',blank=True,null=True)
    c_font_1 = models.FileField(upload_to='certificateApi/font1/')
    c_font_2 = models.FileField(upload_to='certificateApi/font2/')
    c_ceo_name = models.CharField(max_length=100,null=True,blank=True)
    c_cto_name = models.CharField(max_length=100,null=True,blank=True)


class certificateDynamic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    topic = models.CharField(max_length=250,null=True,blank=True)
    exm_date = models.DateField(null=True,blank=True)
    created_dateTime  = models.DateTimeField(auto_now_add=True)
    output_certificate = models.FileField(upload_to='certificateApi/outputCertificate/',blank=True,null=True)



