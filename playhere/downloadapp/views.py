from pathlib import Path
import os
from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse

def downloadApp(request):

    return render(request,'downloadapp.html')



def download_file(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_path = os.path.join(BASE_DIR, 'media', 'app', 'app-release.apk')
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_path)
    return response
