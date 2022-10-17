from django.shortcuts import render,redirect
from .models import profile,cat,questions
import random

lis = []


def profile1(request):
    rank = 0
    pobj = profile.objects.filter(p_username=request.user.username).order_by("-id")
    code = profile.objects.filter(category = 'coding' , p_username=request.user.username).count()
    com = profile.objects.filter(category='communication', p_username=request.user.username).count()
    apti = profile.objects.filter(category='aptitude', p_username=request.user.username).count()
    # Total Rank
    for i in pobj:
        rank += i.score

    try:
        obj = pobj[0]
    except:
        obj =0

    mostplayed = {'coding':code,'communication':com,'aptitude':apti}
    if mostplayed['coding'] == 0 or mostplayed['communication'] == 0 or mostplayed['aptitude'] == 0 :
        mosplay = 0
    else:
        mosplay = max(mostplayed, key=mostplayed.get)

    return render(request,'profile.html',{'pobj':obj,"pobjcount":pobj.count(),'mostplay':mosplay,'rank':rank})


def cate(request):
    catobj = cat.objects.all()

    if request.method == 'POST':
        c_val = request.POST['catbtn']
        request.session['category'] = c_val

        total_cat = questions.objects.filter(category=request.session['category'])
        count = total_cat.count() - 1
        if count > 0:
            q_number = random.randint(0, count)
        else:
            q_number = random.randint(0, 0)

        return redirect(f'/quiz/ques/{q_number}')

    return render(request,'category.html',{'category':catobj})


def ques(request,idd):
    R1=random.randint(20,200)
    R2 = random.randint(20,200)
    G1 = random.randint(20, 200)
    G2 = random.randint(20, 200)
    B1 = random.randint(20, 200)
    B2 = random.randint(20, 200)

    if 'category' in request.session :
        total_cat = questions.objects.filter(category=request.session['category'])
        count = total_cat.count()-1
        try:
            q_number = idd
            qn = total_cat[q_number]
        except:
            qn=''

    if request.method == 'POST':
        try:
            select = request.POST['o']
        except:
            select =''
        print(select)
        if select != '':
            if int(total_cat[q_number].answer) == int(select):
                lis.append(1)
                print('correct answer')
                if len(lis) == 10:
                    return redirect('/quiz/result')

                return redirect(f'/quiz/ques/{random.randint(0,count)}')

            else:
                lis.append(0)
                print('incorrect Answer')
                if len(lis) == 10:
                    return redirect('/quiz/result')

                return redirect(f'/quiz/ques/{random.randint(0, count)}')


        else :
            pass

    dis = {'r1': R1, 'r2': R2, 'g1': G1, 'g2': G2, 'b1': B1, 'b2': B2, 'q_obj': qn,'count':len(lis)+1}

    return render(request,'index.html',dis)


def result(request):
    # try:
    uname = request.user.username
    ucategory = request.session['category']
    uscore = sum(lis)
    #comming soon
    utimetaken = 0

    save_user_data = profile(p_username=uname, category=ucategory, score=uscore, timetkaen=utimetaken )
    save_user_data.save()
    pobj = profile.objects.all()
    lis = []
    return render(request,'result.html',{'pobj':pobj})
    # except:
    #     return redirect('/')
