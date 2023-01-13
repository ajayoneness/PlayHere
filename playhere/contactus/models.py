from django.db import models


class contactUs(models.Model):
    name = models.TextField(max_length=20)
    phone = models.TextField(max_length=16)
    email = models.EmailField(max_length=250)
    message = models.TextField()
