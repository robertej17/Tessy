import time
import datetime
import os

pic_filename = "question_picture1.png"



now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

bad_picname = "Question_Misread_"+now+".png"
print(bad_picname)

os.rename(pic_filename, bad_picname)

