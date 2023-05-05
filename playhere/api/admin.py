from django.contrib import admin
from .models import certificateStatic,certificateDynamic



admin.site.register(certificateDynamic)
admin.site.register(certificateStatic)