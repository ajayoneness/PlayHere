from django.db import models



class feedback(models.Model):
    uname = models.TextField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    mes = models.TextField()

