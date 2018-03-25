from PIL import Image

"""img = Image.open('LOOKATTHIS.png').convert('LA')
img.save('gre.png')

image_file = Image.open("gre.png") # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('result.png')

from skimage import io
img = io.imread('LOOKATTHIS.png', as_grey=True)
img.save("dome.png")"""


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Pixels higher than this will be 1. Otherwise 0.
THRESHOLD_VALUE = 220

#Load image and convert to greyscale
img = Image.open("LOOKATTHIS.png")
img = img.convert("L")

imgData = np.asarray(img)
thresholdedData = (imgData > THRESHOLD_VALUE) * 1.0

plt.imshow(thresholdedData)
plt.axis('off')
#plt.show()
#plt.savefig("testing.png",bbox_inches='tight',pad_inches=0)
plt.imsave("foo.png",thresholdedData, format="png")
