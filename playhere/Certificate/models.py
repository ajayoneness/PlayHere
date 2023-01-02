from django.db import models


class CeriF(models.Model):
    user_name = models.TextField(max_length=254, unique=True, db_index=True, primary_key=True)
    upload_chart = models.FileField(upload_to="certificate/", max_length=250, null=True, default=None)
