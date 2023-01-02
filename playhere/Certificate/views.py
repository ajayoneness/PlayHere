from django.shortcuts import render

# Create your views here.
def certi(request):
    # obj = Data(f'{request.user.first_name} {request.user.last_name}',datetime.today(),request.session['mostplay'])
    # print(obj)
    # #obj.imagesize(150, 150,'C:/Users/ajayo/OneDrive/Desktop/PlayHere/playhere/media/playhere/playhere.png', '/media/playhere/playherelogo.png')
    # t = f'''" is hereby awardes this certificate of achievement for the successfully \n           getting 10,000 rank on 'codeaj.pythonanywhere.com' \n                          by playing {obj.course} on {obj.date} "'''
    # obj.imgCreate('C:/Users/ajayo/OneDrive/Desktop/PlayHere/playhere/media/playhere/bg.jpg', 'C:/Users/ajayo/OneDrive/Desktop/PlayHere/playhere/media/playhere/mainlogo.png', 50, obj.name, 34, 177, 76, 'C:/Users/ajayo/OneDrive/Desktop/PlayHere/playhere/media/namefont.ttf', 320, 200, 250,70)
    # obj.AddText(20, t, 225, 225, 225,'C:/Users/ajayo/OneDrive/Desktop/PlayHere/playhere/media/textfont.ttf', 150, 280)
    # obj.AddText(15, '    Ajay Pandit \n  CTO of codeaj', 225, 225, 225, 'C:/Users/ajayo/OneDrive/Desktop/PlayHere/playhere/media/namefont.ttf', 95, 493)
    # obj.AddText(15, 'Md Raza subhani \n  CTO of codeaj', 225, 225, 225, 'C:/Users/ajayo/OneDrive/Desktop/PlayHere/playhere/media/namefont.ttf', 680, 500)
    # obj.AddImage('C:/Users/ajayo/OneDrive/Desktop/PlayHere/playhere/media/playhere/playherelogo.png', 360, 400)
    # #obj.AddImage('cistlogo.jpg',480,450)
    # print(f"{obj.outimg} created !!")

    return render(request,'certification.html',{'rank' : request.session['rank']})