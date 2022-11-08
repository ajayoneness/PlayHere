from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from django.contrib.auth.models import User





class profile(models.Model):
    user_id = UserForeignKey(auto_user_add=True)
    p_username = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    category = models.TextField()
    score = models.FloatField()
    timetkaen = models.IntegerField(blank=True)


class addmore(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,blank=True)
    profile_photo = models.ImageField(upload_to='profile', null=True,blank=True)
    mobile_number = models.PositiveBigIntegerField(null=True,blank=True)
    date_of_birth = models.DateField(auto_now_add=False, auto_now=False,blank=True,null= True)
    zip_code = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=225, null=True,blank=True)
    #website = models.URLField(max_length=100, null=True,blank=True)
    bio = models.CharField(max_length=225, null=True,blank=True)



class cat(models.Model):
    cat = models.TextField()
    c_bio = models.TextField()
    bg_image = models.TextField(blank=True)


class questions(models.Model):
    question = models.TextField(max_length=1000)
    subquestion = models.TextField(blank=True, max_length=1000)
    option1 = models.TextField(max_length=500)
    option2 = models.TextField(max_length=500)
    option3 = models.TextField(max_length=500)
    option4 = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    category = models.TextField(max_length=200)
    topic = models.TextField(max_length=250)




