
from PIL import Image,ImageFont,ImageDraw,ImageOps
image=Image.new('RGB',(2106 ,900),(255,255,255))
draw=ImageDraw.Draw(image)
#font= ImageFont.truetype("arial.ttf",size=100)
#import random
import os
import datetime

os.system("CERTIFICATE generator ")
d_date=datetime.datetime.now()
reg_format_date=d_date.strftime(" %d-%m-%Y \t\t CERTIFICATE \t\t %I:%M:%S %p")
print(reg_format_date)
print('\n ALL FIELDS ARE NECESSARY ')
###First line

(x,y)=(340,100)
message=('CERTIFICATE OF COMPLETION')
color='rgb(0,0,0)'
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)


###adding border to image
border_image=ImageOps.expand(image,border=100)
#border_image.show()
 
###next line 



(x,y)=(550,270)
message=('This certificate is presented to')
color='rgb(233,150,122)'
font=ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)


 ##t#taking name as input
 
 
(x,y)=(700,350)
message=input("Enter your name: ")
color='rgb(238,44,44)'
font=ImageFont.truetype('arial.ttf',size=49)
draw.text((x,y),message,fill=color,font=font)
###next line


(x,y)=(500,450)
message=('For Successfully completeing training for ')
color='rgb(240,128,128)'
font=ImageFont.truetype('arial.ttf',size=80)
draw.text((x,y),message,fill=color,font=font)

###another line
(x,y)=(700,550)
message=('PYTHON BOOTCAMP.')
color='rgb(255,182,193)'
font=ImageFont.truetype('arial.ttf',size=40)
draw.text((x,y),message,fill=color,font=font)

###next
(x,y)=(1750,650)
message=('SIGNATURE')
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=35)
draw.text((x,y),message,fill=color,font=font)



image.save("certificate.jpg")
 ###adding signature to the image......
image = Image.open('certificate.jpg')
logo = Image.open('signature.png')
image_copy = image.copy()
image_copy.paste(logo, (1790,700))
#image_copy.show()
image_copy.save('pasted_image.jpg')

####adding logo/seal to yourr certificate

image=Image.open('pasted_image.jpg')
#seal=Image.open('seal2.jpg')
#image_seal=image.copy()
#image_seal.paste(seal,(100,600))
#image_seal.show()