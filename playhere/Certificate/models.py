from django.db import models


class CeriF(models.Model):
    user_name = models.TextField(max_length=254, unique=True, db_index=True, primary_key=True)
    upload_chart = models.FileField(upload_to="certificate/", max_length=250, null=True, default=None)

class certificate(models.Model):
    bg = models.FileField(upload_to="certificatefiles/")
    mainlogo = models.FileField(upload_to="certificatefiles/")
    namefont = models.FileField(upload_to="certificatefiles/")
    ph = models.FileField(upload_to="certificatefiles/")
    phlogo = models.FileField(upload_to="certificatefiles/")
    textfont = models.FileField(upload_to="certificatefiles/")
    output = models.FileField(upload_to="certificatefiles/")