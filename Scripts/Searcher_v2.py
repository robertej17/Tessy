from googleapiclient.discovery import build
import pprint
import operator
import os
import argparse
from PIL import Image
import pytesseract
import pyscreenshot as ImageGrab
import codecs
import time
import datetime

#Second version of Searcher. Operating as of 3/24/18 #

## Grab screenshot of image (put on rig  ht side of screen!)
#im=ImageGrab.grab(bbox=(900,300,1500,700)) # for hq trivia
im=ImageGrab.grab(bbox=(1040,300,1400,670))# special
#im.show() #Uncomment this if you want to see image

# save to file

pic_filename = "question_picture1.png"

im.save(pic_filename)


pic_filename = "question_picture1.png"

im = Image.open(pic_filename)

text = pytesseract.image_to_string(im, lang = 'eng')

col1 = 20
col2 = 20


tryme = text.encode('utf-8')
#print(tryme)
myarray = tryme.split("\n\n")
#print("Old myarray:")
#print(myarray)
#print("ENDENDENDENDENDENDEND")
splitters = []

Q3 = (len(myarray))-1
Q2 = Q3-1
Q1 = Q2-1

print(Q3,Q2,Q1)

"""
ii = Q3
print(myarray[ii])
if myarray[ii].find("\n"):
	print("N HAS BEEN FOUND in 2-3")
	cars = myarray[ii].split("\n")
	print(cars)
	myarray[ii] = cars[0]
	myarray[ii+1] = cars[1]

ii = Q2
print(myarray[ii+1])
if myarray[ii].find("\n"):
	print("N HAS BEEN FOUND in 1-2")
	cars = myarray[ii].split("\n")
	myarray[ii+2] = myarray[ii+1]
	myarray[ii] = cars[0]
	myarray[ii+1] = cars[1]

	

print("CHECKRESULT")
print(myarray)
print("ENDCHECK")
"""

i = 0
for l in myarray:
	myarray[i] = myarray[i].replace("\n"," ")
	i = i + 1
"""i = 0
for l in myarray:
	myarray[i] = myarray[i].replace("\n"," ")
	i = i + 1
	'\n' in myarray[i]"""



i = 0
ques_str=""
while i < Q1:
	ques_str +=myarray[i]
	ques_str +=" "
	i = i +1



#print(ques_str)

print("New my array is: ")
print(myarray)
print("ENDIT")

default_question = ques_str
default_a1 = myarray[Q1]
default_a2 = myarray[Q2]
default_a3 = myarray[Q3]

print('question: '+default_question+'\n')
print('answer 1: '+default_a1+'\n')
print('answer 2: '+default_a2+'\n')
print('answer 3: '+default_a3+'\n')





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
"""


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


print('\n\n\n'+question+'\n\n'+'Results:')
i = 0
while i < len(answers):
	print("{:{n}s} {:{p}s}".format(str(answers[i]),str(q[i]),n=col1,p=col2))
	#print("HELP")
	i = i + 1

print('\n'+"Answer is " + answers[index]+ '\n')




###### Get right or wrong value ######


real_answer = raw_input("What was the answer? (Enter 1, 2, or 3)")
#real_answer = "a"

#Write to log ######

#write to file:
#date/time
#question
#answers
#right/wrong


now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

outfilename = 'Questions_Log'

me = os.path.basename(__file__)
cwd = os.getcwd()
filelocation = cwd + '/' + outfilename
if not os.path.exists(filelocation):
	with open(outfilename, 'w+') as writefile:
		writefile.write('This file was generated by ' + me + ' on ' + now + '\n \n')
		#writefile.write("{:{n}s} {:{p}s} {} \n\n".format('Histogram File Name','Total Counts','Approximate Rate',n=col1,p=col2))

Date_string = "Question generated at "+ now

r_i = int(real_answer)-1

with open(outfilename, 'a+') as writefile:
		writefile.write("\n\n\n{} \n".format(Date_string))
		writefile.write("\nRaw input from image recognition:\n {} \n".format(tryme))
		writefile.write("\nInterpreted question:\n {} \n".format(default_question))
		writefile.write("\nInterpreted answer 1: {} \n".format(default_a1))
		writefile.write("\nInterpreted answer 2: {} \n".format(default_a2))
		writefile.write("\nInterpreted answer 3: {} \n".format(default_a3))
		writefile.write("\nComputed Answer Was: {} \n".format(answers[index]))
		writefile.write("\nReal Answer Was: {} \n".format(answers[r_i]))
		
		if r_i == int(index):
			writefile.write("\nAnswers Match! \n")
			
"""
