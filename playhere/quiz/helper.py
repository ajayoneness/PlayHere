from PIL import Image, ImageDraw, ImageFont
from django.contrib.staticfiles import finders
from django.templatetags.static import static



class Data():
    def __init__(self,name,date,course,collage='CIST',outimg=static('C:/Users/ajayo/OneDrive/Desktop/PlayHere/playhere/media/aj.png')):
        self.name=name
        self.date=date
        self.course=course
        self.collage=collage
        self.outimg=outimg

    def imgCreate(self,templates,logo,fontsize,text,color_R,color_G,color_B,font,pos_x,pos_y,img_pos_x=250,img_pos_y=70):
        img = Image.open(templates)
        img2=Image.open(logo)
        draw = ImageDraw.Draw(img)
        img.paste(img2, (img_pos_x, img_pos_y))
        font = ImageFont.truetype(font, fontsize)
        draw.text((pos_x,pos_y),text, fill=(color_R,color_G,color_B), font=font)
        img.save(f"{self.outimg}")


    def AddText(self,fontsize,text,color_R,color_G,color_B,font,pos_x,pos_y):
        img = Image.open(self.outimg)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font, fontsize)
        draw.text((pos_x,pos_y),text, fill=(color_R,color_G,color_B), font=font)
        img.save(f"{self.outimg}")


    def AddImage(self,logo,logopos_x,logopos_y):
        img = Image.open(self.outimg)
        img2 = Image.open(logo)
        img.paste(img2, (logopos_x, logopos_y))
        img.save(f"{self.outimg}")

    def imagesize(self,height, weight,input_image,output_image):
        WIDTH = weight
        HEIGHT = height
        img = Image.open(input_image)
        resized_img = img.resize((WIDTH, HEIGHT))
        resized_img.save(output_image)


obj = Data('Ajay Pandit','02/11/2022','Coding Quiz','PlayHere','aj.png')

# obj.imagesize(150,150,'playhere/playhere.png','playhere/playherelogo.png')
# t=f'''" is hereby awardes this certificate of achievement for the successfully \n           getting 10,000 rank on 'codeaj.pythonanywhere.com' \n                          by playing {obj.course} on {obj.date} "'''
# obj.imgCreate('playhere/bg.jpg','playhere/mainlogo.png',50,obj.name,34,177,76,'namefont.ttf',320,200,250,70)
# obj.AddText(20,t,225,225,225,'textfont.ttf',150,280)
# obj.AddText(15,'    Ajay Pandit \n  CTO of codeaj',225,225,225,'namefont.ttf',95,493)
# obj.AddText(15,'Md Raza subhani \n  CTO of codeaj',225,225,225,'namefont.ttf',680,500)
# obj.AddImage('playhere/playherelogo.png',360,400)
# #obj.AddImage('cistlogo.jpg',480,450)
# print(f"{obj.outimg} created !!")

