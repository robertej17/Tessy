from googleapiclient.discovery import build
import pprint
import operator
import os
import argparse
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

#for l in myarray:
#	print(l)

#outfilename = "textoutput.txt"
#with open(outfilename, 'a+') as writefile:
#		writefile.write(tryme)



default_question = myarray[0]
default_a1 = myarray[1]
default_a2 = myarray[2]
default_a3 = myarray[3]






#default_question = 'what is the first letter of the english alphabet?'
#default_a1 = '''"a"'''
#default_a2 = '''"m"'''
#default_a3 = '''"x"'''
description_program = """ This python script sums all values in a 2 column histogram (sums second column)\n
			For use in analyzing NaI digitizer histograms, but can be generalized to other uses\n"""


parser = argparse.ArgumentParser(description=description_program)
parser.add_argument('-q','--question',default=default_question,help='Set input file name \n',required=False)
parser.add_argument('-1','--one',default=default_a1,help='Set output file name \n',required=False)
parser.add_argument('-2','--two',default=default_a2,help='Set time of run duration \n',required=False)
parser.add_argument('-3','--three',default=default_a3,help='Set time of run duration \n',required=False)


args = vars(parser.parse_args())

my_api_key = "AIzaSyCen7PGBCDkmGIFUujTAMdrE4PAzLL4eDM"
my_cse_id = "014077220477457727762:lho6q3-emq8"

question = args['question']
a1 = args['one']
a2 = args['two']
a3 = args['three']

answers = [a1,a2,a3] #site:en.wikipedia.org'

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    total_results = res['searchInformation']['totalResults']
    return total_results#res['items']


results = [0]*len(answers)
i = 0
#print(results[0])
while i < len(answers):
	#print(i)
	results[i] = google_search(question+"\""+answers[i]+"\"", my_api_key, my_cse_id, num=10)
	#print(answers[i]+results[i]+"\n\n")
	i = i +1


print(question+"\""+answers[1]+"\"")
q = [0]*len(answers)
i = 0
while i < len(answers):
	#print(i)
	q[i] = int(results[i])
	i = i +1
#for result in results:
#    pprint.pprint(result)

index, value = max(enumerate(q), key=operator.itemgetter(1))

col1 = 20
col2 = 20
print('\n\n\n'+question+'\n\n'+'Results:')
i = 0
while i < len(answers):
	print("{:{n}s} {:{p}s}".format(str(answers[i]),str(q[i]),n=col1,p=col2))
	i = i +1

print('\n'+"Answer is " + answers[index]+ '\n')












