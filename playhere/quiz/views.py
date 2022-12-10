from django.shortcuts import render,redirect
from .models import profile,cat,questions,addmore
import random
from django.core.files.storage import FileSystemStorage
from .helper import Data

def fileHandel():
    def read_file(file_name):
        file = open(file_name, 'r')
        for each in file:
            print(each)

    def create_write(file_name, txt):
        file = open(file_name, 'w')
        file.write(txt)
        file.close()

    def append_text_in_file(file_name, txt):
        file = open(file_name, 'a')
        file.write(txt)
        file.close()


def profile1(request):
    count = 0
    # request.session['lis']=0
    # request.session['tlis']=0
    # request.session['count']=0

    print(type(request.session['lis']))
    print(request.session['lis'])
    # lis.clear()
    # tlis.clear()
    rank = 0
    pobj = profile.objects.filter(p_username=request.user.username).order_by("-id")
    code = profile.objects.filter(category = 'coding' , p_username=request.user.username).count()
    com = profile.objects.filter(category='communication', p_username=request.user.username).count()
    apti = profile.objects.filter(category='aptitude', p_username=request.user.username).count()
    # Total Rank
    for i in pobj:
        rank += i.score

    request.session['rank'] = rank

    try:
        obj = pobj[0]
    except:
        obj = 0

    mostplayed = {'coding':code,'communication':com,'aptitude':apti}

    if mostplayed['coding'] == 0 and mostplayed['communication']==0 and mostplayed['aptitude'] == 0 :
        mosplay = 0
    else:
        mosplay = max(mostplayed, key=mostplayed.get)

    request.session['mostplay'] = mosplay

    try:
        aobj = addmore.objects.filter(user=request.user).order_by("-id")
        print(aobj[0].profile_picture)
    except:
        aobj ="ajay"

    return render(request,'profile.html',{'pobj':obj,"pobjcount":pobj.count(),'mostplay':mosplay,'rank':round(rank,2),'aobj':aobj})


def cate(request):
    request.session['lis'] = 0
    request.session['tlis'] = 0
    request.session['count'] = 1
    request.session['countt'] = 0
    print("cat list : ",request.session['lis'])
    #request.session['lis'] = request.session['lis']+1

    try:
        aobj = addmore.objects.filter(user=request.user).order_by("-id")
        print(aobj[0].profile_picture)
    except:
        aobj ="ajay"

    # lis = []
    # tlis = []
    #countt[0] = 0
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
    print("list : ",request.session['lis'])
    print('count session : ', request.session['count'])
    countt =0
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
            ti = request.POST['sec']
            print("time taken : ", ti)
            select = request.POST['o']
        except:
            select =''
            ti = 0
        print(select)

        uniquekey = {
            0: '345vcfhgjvgdfgh43564578',
            1: '4356guyhgcxfdft56787',
            2: '567ghvhmbkj678vgvbjgh',
            3: '678yhjmbjhbjn7yigvhj78',
            4: '65778uhbnuyfjgy78uyt7ugfvy7',
            5: '567ytfhgnhbvhnhyut6u567',
            6: '67yyujhnbhnhj78uuhbnb',
            7: '657uhjmbjknbhg78u',
            8: '54657uyughjnbvnjnhbn',
            9: 'gyjukhbvghjbvg6757676j',
            10:'6457678uygjkhg687yh',
        }


        if select != '':

            if int(total_cat[q_number].answer) == int(select):
                try:
                    if int(ti)<100:
                        request.session['tlis'] +=int(ti)
                        #request.session['tlis'].append(int(ti))
                    else:
                        request.session['tlis'] += 99
                except:
                    request.session['tlis'] += "Error at line no 138"

                request.session['lis'] += 1
                print('mark count : ', request.session['lis'])


                print('correct answer')
                if request.session['count'] >= 10:
                    request.session['ttime'] = request.session['tlis']
                    print(request.session['tlis'])
                    print(request.session['ttime'])
                    #-------------------------------
                    sumlis = request.session['lis']
                    print(sumlis)
                    request.session['lis'] = 0
                    request.session['tlis'] = 0
                    print(uniquekey[sumlis])
                    return redirect(f'/quiz/result/{sumlis}')

                request.session['count'] += 1

                return redirect(f'/quiz/ques/{random.randint(0,count)}')

            else:
                try:
                    if int(ti) < 100:
                        request.session['tlis'] += (int(ti))
                    else:
                        request.session['tlis'] += 99
                except:
                    request.session['tlis'] += 0

                request.session['lis'] += 0
                print('mark count : ',request.session['lis'])
                print('incorrect Answer')
                if request.session['count'] >= 10:
                    request.session['ttime'] = request.session['tlis']
                    print(request.session['tlis'])
                    print("tlis session : ",request.session['ttime'])
                    sumlis = request.session['lis']
                    print("lis session : ",sumlis)
                    request.session['lis'] = 0
                    # print(uniquekey[sumlis])
                    return redirect(f'/quiz/result/{sumlis}')
                request.session['count'] += 1
                return redirect(f'/quiz/ques/{random.randint(0, count)}')
        else :
            pass
    print('end point of count session : ',request.session['count'])
    dis = {'r1': R1, 'r2': R2, 'g1': G1, 'g2': G2, 'b1': B1, 'b2': B2, 'q_obj': qn,'count':request.session['count']}

    return render(request,'index.html',dis)



def result(request,slis):
    try:
        emoji ={
                0:['https://media3.giphy.com/media/IzcFv6WJ4310bDeGjo/giphy.gif?cid=ecf05e47k3nntc4i6h0dka9ewtqldv1j67d5m52kurajmtj1&rid=giphy.gif&ct=g','you need to practice more ', '345vcfhgjvgdfgh43564578'],
                1:['https://media3.giphy.com/media/IzcFv6WJ4310bDeGjo/giphy.gif?cid=ecf05e47k3nntc4i6h0dka9ewtqldv1j67d5m52kurajmtj1&rid=giphy.gif&ct=g','you need to practice more ','4356guyhgcxfdft56787'],
                2:['https://media0.giphy.com/media/h4OGa0npayrJX2NRPT/giphy.gif?cid=ecf05e47k3nntc4i6h0dka9ewtqldv1j67d5m52kurajmtj1&rid=giphy.gif&ct=g','ohh so sad','567ghvhmbkj678vgvbjgh'],
                3:['https://media0.giphy.com/media/kfS15Gnvf9UhkwafJn/giphy.gif?cid=ecf05e47la8y34pgr207jtpmr6k5q9q7g34sr6zm25oywgoe&rid=giphy.gif&ct=g','not bad','678yhjmbjhbjn7yigvhj78'],
                4:['https://media2.giphy.com/media/j4l0mCdcTFRyY4Bc5s/giphy.gif?cid=ecf05e47la8y34pgr207jtpmr6k5q9q7g34sr6zm25oywgoe&rid=giphy.gif&ct=g','nice','65778uhbnuyfjgy78uyt7ugfvy7'],
                5:['https://media0.giphy.com/media/USUIWSteF8DJoc5Snd/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','not bad','567ytfhgnhbvhnhyut6u567'],
                6:['https://media4.giphy.com/media/hp3dmEypS0FaoyzWLR/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','wow','67yyujhnbhnhj78uuhbnb'],
                7:['https://media1.giphy.com/media/hVlZnRT6QW1DeYj6We/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','suer','657uhjmbjknbhg78u'],
                8:['https://media4.giphy.com/media/UQDSBzfyiBKvgFcSTw/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','good','54657uyughjnbvnjnhbn'],
                9:['https://media2.giphy.com/media/LOnt6uqjD9OexmQJRB/giphy.gif?cid=ecf05e47xzour2hglinyz1ann7ex8ghg5tgw5i31et1sym2h&rid=giphy.gif&ct=g','sweet','gyjukhbvghjbvg6757676j'],
                10:['https://media3.giphy.com/media/lRXY41yFFi9RfNXyPN/giphy.gif?cid=ecf05e47mxr383ar6o6yxhzr5iaoa8j6iw17z3axmyc3dgau&rid=giphy.gif&ct=g','so, sweet','6457678uygjkhg687yh'],
        }

        ucategory = request.session['category']
        uscore = slis
        emo = emoji[uscore]
        #comming soon
        utimetaken = request.session['ttime']
        rank = ((uscore*100)-(utimetaken))/100

        if request.user.is_authenticated and request.session['countt'] == 0:
            request.session['countt'] = 1
            uname = request.user.username
            #make score field to float
            save_user_data = profile(p_username=uname, category=ucategory, score=round(rank,2), timetkaen=utimetaken )
            save_user_data.save()
            return render(request,'result.html',{'score':uscore,'emoji':emo,'timetaken':utimetaken,'rank':rank})

        elif request.session['countt'] == 0:
            request.session['countt'] = 1
            return render(request, 'result.html',{'score': uscore, 'emoji': emo, 'timetaken': utimetaken, 'rank': rank})



        else:
            #countt[0]=0
            # return render(request, 'result.html',{'score': uscore, 'emoji': emo, 'timetaken': utimetaken, 'rank': rank})
            return redirect('/')


    except:
        #countt[0] = 0
        return redirect('/')





def loaddata(request):

    #update some missing fields
    # for i in range(1,11):
    #     q= questions.objects.get(id=i)
    #     q.category = 'coding'
    #     q.topic  = "Python"
    #     q.save()
    #     print('done')

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        #uploaded_file_url = fs.url(filename)
        path = fs.path(filename)
        print("i am a path : "+path)

        import pandas as pd
        data = pd.read_excel(f"{path}")
        print(data)
        for i in range(0,len(data)):
            #uploadquestion = questions(question = data['question'][i],subquestion=data['subquestion'][i],option1=data['option1'][i],option2=data['option2'][i],option3=data['option3'][i],option4=data['option4'][i],answer = data['answer'][i],category = data['category'][i],topic = data['topic'][i])
            #uploadquestion.save()
            pass
        uc="upload completed"
        return render(request, 'loadquestion.html',{'mes':uc})


    return render(request,'loadquestion.html')







def certificate(request):
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


def AddMoreDetails(request):
    try:
        obj = addmore.objects.filter(user=request.user).order_by("-id")
        da = obj[0].date_of_birth
        #da = str(da).split('-')
        #da = f'{da[2]}-{da[0]}-{da[1]}'
        print("date : ",da)
    except:
        obj = "codeaj"
        da = ''
    try:
        if request.method == 'POST':
            # uname = request.user.username
            try:
                pimg = request.FILES['pimg']
            except:
                pimg = obj[0].profile_photo

            mobno = request.POST['mobno']
            dob = request.POST['dob']
            zip = request.POST['zipcode']
            address = request.POST['address']
            #site = request.POST['site']
            bio = request.POST['bio']
            print(pimg,mobno,dob,zip,address,bio)
            b=addmore(user=request.user,profile_photo=pimg, mobile_number=int(mobno), date_of_birth=dob, zip_code=zip, address=address, bio=bio)
            b.save()
            return redirect('/quiz/')
    except:
        pass

    return render(request,'addmore.html',{'obj':obj,'date':str(da)})

