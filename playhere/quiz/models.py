from django.db import models
from django_userforeignkey.models.fields import UserForeignKey





class profile(models.Model):
    user_id = UserForeignKey(auto_user_add=True)
    p_username = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    category = models.TextField()
    score = models.IntegerField()
    timetkaen = models.IntegerField(blank=True)



class cat(models.Model):
    cat = models.TextField()
    c_bio = models.TextField()
    bg_image = models.TextField(blank=True)


class questions(models.Model):
    question = models.TextField(max_length=1000)
    option1 = models.TextField(max_length=500)
    option2 = models.TextField(max_length=500)
    option3 = models.TextField(max_length=500)
    option4 = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    category = models.TextField(max_length=200)
    topic = models.TextField(max_length=250)




