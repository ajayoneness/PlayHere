from django.shortcuts import render,redirect
from .models import contactUs

def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        svdata = contactUs(name=name,phone=phone,email=email,message=message)
        svdata.save()

    return render(request,'contactus.html')