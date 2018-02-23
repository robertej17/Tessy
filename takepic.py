import pyscreenshot as ImageGrab
# fullscreen
#im=ImageGrab.grab()
#im.show()

# part of the screen
im=ImageGrab.grab(bbox=(900,300,1500,700))
im.show()

# to file
im.save('sample1.png')
