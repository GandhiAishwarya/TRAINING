
#watermak image with image only
from PIL import Image 
def watermark_photo(input_image, output_image, watermark_image, position):
    transparent = Image.open(input_image)
    watermark = Image.open(watermark_image)
    
    #base_image.paste(watermark, position, mask=watermark)
    #base_image.show()
    #base_image.save(output_image)
    width, height = transparent.size
 
    transparent.paste(transparent, (0,0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.show()
    transparent.save(output_image)
 
 
if __name__ == '__main__':
    img = input("original:")
    img_water = input("watermark:")
    watermark_photo(img, 'output.jpg', img_water, position=(0,0))
    
    


#watermark image using text
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
 
def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)
 
    # make the image editable
    drawing = ImageDraw.Draw(photo)
 
    black = (10, 10, 12)
    font = ImageFont.truetype("arial.ttf", 90)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)
 
 
if __name__ == '__main__':
    img = input("original:")
    watermark_text(img, 'watermarked.jpg',
                   text='First_Text_Watermark',
                   pos=(0, 0))















