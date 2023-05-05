from PIL import Image, ImageDraw, ImageFont


class Data():
    def __init__(self,name,date,course,collage,outimg):
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



    # def imagesize(self,height, weight,input_image,output_image):
    #     WIDTH = weight
    #     HEIGHT = height
    #     img = Image.open(input_image)
    #     resized_img = img.resize((WIDTH, HEIGHT))
    #     resized_img.save(output_image)



