from PIL import Image
import pytesseract
import pyscreenshot as ImageGrab
import codecs

## Grab screenshot of image (put on rig  ht side of screen!)
#im=ImageGrab.grab(bbox=(900,300,1500,700)) # for hq trivia
im=ImageGrab.grab(bbox=(1000,300,1400,700))# special
#im.show() #Uncomment this if you want to see image

# save to file
im.save('question_picture1.png')

im = Image.open("question_picture1.png")

text = pytesseract.image_to_string(im, lang = 'eng')

### Write out to text file
#print(type(text))

tryme = text.encode('utf-8')
#print(tryme)
myarray = tryme.split("\n\n")
splitters = []
i = 0
#for line in myarray:
    #print(line)
#	splitters[i] = line
#	i = i + 1
    #print("Next Line")
i = 0
for l in myarray:
	myarray[i] = myarray[i].replace("\n"," ")
	i = i + 1
	#print(i)
	#print(l)
	#print(str(l))

#print(myarray)

print(myarray[2])

outfilename = "textoutput.txt"
with open(outfilename, 'a+') as writefile:
		writefile.write(tryme)

####
#Write question and variables to listing
#### 

#google search them
