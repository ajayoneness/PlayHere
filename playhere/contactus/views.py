from django.shortcuts import render,redirect,HttpResponse
from .models import contactUs
import smtplib
from django.core.mail import send_mail

def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        subject = "PlayHere ContactUs"
        message = f'''
            Name : {name}
            Phone no : {phone}
            email : {email}
            message : {message}
        '''
        from_email = "playherequiz@gmail.com"
        to_list = ["playherequiz@gmail.com",'ajayoneness123@gmail.com']

        send_mail(subject,
                  message,
                  from_email,
                  to_list,
                  fail_silently=False,
                  )
        svdata = contactUs(name=name,phone=phone,email=email,message=message)
        svdata.save()

    return render(request,'contactus.html')

