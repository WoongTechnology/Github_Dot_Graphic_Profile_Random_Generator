# WoongTechnology @funright 2020
# Github_Dot_Graphic_Profile_Random_Generator  3GDPR.

from PIL import Image, ImageDraw
from random import randint

colour_combobox = [[214, 154, 226],[228, 216, 138], [120, 202, 98], [204, 157, 117], [217, 140, 183],[140, 195, 216],[202, 87, 125],[198, 116, 83]] 

def colour_random():
     temp_colour = randint(0,len(colour_combobox))
     return colour_combobox[temp_colour]
      

def shape_random():
    temp_shape = []
    for i in range(25):
        temp_shape.append(0)
    for i in range(5):
        for j in range(3):
            temp_shape[j+i*5] = randint(0,1)
            temp_shape[4-j+5*i] = temp_shape[j+5*i]
    return temp_shape

      
img_colour = tuple(colour_random())
img_shape = shape_random()

img = Image.new('RGB', (500, 500), color = (240, 240, 240))
draw = ImageDraw.Draw(img)

for i in range(0, 25):
      y, x = divmod(i, 5)
      if img_shape[i] == 1 :
            draw.rectangle([x * 100, y * 100, x * 100 + 100, y * 100 + 100 ], fill = img_colour)

img.save('github_profile.png')
