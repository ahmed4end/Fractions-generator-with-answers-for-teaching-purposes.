from PIL import Image , ImageDraw , ImageFont
import os 
import random
from fractions import Fraction
import os

rands = [i for i in range(1, 9)] + [i for i in range(1, 5)] 

size = (2480, 3508)
#---------------------------------------------------------------


image = Image.new(mode = 'RGB' , size = size , color = "white")    
Draw = ImageDraw.Draw(image)
fnt = ImageFont.truetype(os.path.join(os.getcwd()+ "\\ar.ttf") , 130)


#---------------------------------------------------------------

position = (size[0]-250,100)
axisX = position[0]
axisY = position[1]


Dsign = "__"
DsignSize = Draw.textsize(text=Dsign, font= fnt)

translations = {48: '۰', 49: '۱', 50: '۲', 51: '۳', 52: '٤', 53: '٥', 54: '٦', 55: '٧', 56: '۸', 57: '۹'}
re_translations = {ord(i):chr(j) for j,i in translations.items()}

#---------------------------------------------------------------

def nd(p, ds, n, d, padding= 20):
	"""
	p: position of the original target "devision sign position"
	ds: devision sign
	n: numerator text number
	d: denominator text number
	"""
	nSize, dSize = Draw.textsize(text=n, font=fnt), Draw.textsize(text=d, font=fnt)
	numerator  = (p[0]+ds[0]//2-nSize[0]//2, p[1]+ds[1]-nSize[1] - padding)
	denominator = (p[0]+ds[0]//2-dSize[0]//2, p[1]+2*ds[1]-dSize[1] - padding)
	return [numerator, denominator, n, d]


def add(dict, key, value):
	if key in dict:
		dict[key] = dict[key] + value
	else:
		dict[key] = value

#---------------------------------------------------------------

dict = {}

t= 2  #t represents how many  fractions you wanna it to exist per one question.

QNubmer = 1
for j in range(3):

	if j == 1:
		axisX = axisX // 2 + 240
		position = (axisX, axisY)

	if j == 2:
		axisX = 540
		position = (axisX, axisY)


	for h in range(15):          #Number of Questions per column.
		for i in range(t):
			
			
			n, d = str(random.choice(rands)), str(random.choice(rands))
			#n, d = str(random.randint(1,10)), str(random.randint(1,9))
			add(dict, QNubmer, Fraction(int(n), int(d)))

			n, d = n.translate(translations), d.translate(translations)

			a = nd(position, DsignSize, n, d)
			s = Draw.textsize(text="__", font=fnt)
			Draw.text( position, text="__", fill="black", font = fnt )
			Draw.text( a[0], text=a[2], fill="black", font = fnt )
			Draw.text( a[1], text=a[3], fill="black", font = fnt )
			if i == 0:
				Draw.text( (position[0]+150, position[1]+64), text=f"({QNubmer})".translate(translations), fill=(85,85,85,1), font = ImageFont.truetype("G:/ar.ttf" , 75) )
			if i < t-1:
				Draw.text( (position[0]-75 , position[1] + 32), text= "+", fill="black", font = fnt )
				Draw.text( a[0], text=a[2], fill="black", font = fnt )
				Draw.text( a[1], text=a[3], fill="black", font = fnt )
			elif i == t-1:
				Draw.text( (position[0]-75 , position[1] + 32), text= "=", fill="black", font = fnt )
				Draw.text( a[0], text=a[2], fill="black", font = fnt )
				Draw.text( a[1], text=a[3], fill="black", font = fnt )
			position = (position[0]-110-s[0], position[1])
		
		position = (axisX, position[1]+200)

		QNubmer += 1


Draw.text( (0, 3050) , text="__"*100, fill="black", font = fnt )




##---------------------------------------------------------------
#For auto preview after finishing the job.


image = image.transpose(Image.ROTATE_270)
Draw = ImageDraw.Draw(image)


j, i = 30, 0

for k,v in dict.items():
	Draw.text( (j, i) , text=f"({k})={v}".translate(translations), fill="black", font = ImageFont.truetype("G:/ar.ttf" , 75) )
	i += 55

image = image.transpose(Image.ROTATE_90)



save_name = image.save(f"FractionsQuestionsGenrator.png")
#os.system(f"FractionsQuestionsGenrator.png")




#print(dict)
