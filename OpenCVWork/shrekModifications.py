# All our imports
import cv2
import imutils
from PIL import Image
import numpy as np
import os.path
import random
import sys

# With this it doesn't require the user
# to edit the pathways everytime (user friendly :) ) 
homedir = os.path.expanduser("~")

# Imports Haar cascades to recognize the faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Default image is the class
if len(sys.argv) < 2:
	imageGettingShreked = 'Class.jpg'

# However, if you want to shrek your own
# image you just add the name of the jpg
# file as an argument. Make sure it is in
# this directory though
else:
	IMAGEIMAGEIMAGE = sys.argv[1]
	imageGettingShreked = IMAGEIMAGEIMAGE

# Reads in the image and turns it to grayscale
img = cv2.imread(homedir + '/FinalProject-ATJunior-Year/' + imageGettingShreked)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Opens the image you imported that is layered upon later
first_image = Image.open(homedir + '/FinalProject-ATJunior-Year/' + imageGettingShreked)

# Identifies all the faces (not insanely accurate)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Itterates over said faces
for (x,y,width,height) in faces:

	# Pretty redundant, but this is what would draw the bounding
	# boxes. I'm just keeping it here for later when I use
	# this as the base of my code for my summer project
	img = cv2.rectangle(img,(x,y),(x+width,y+height),(255,0,0),2)
	roi_gray = gray[y:y+height, x:x+width]
	roi_color = img[y:y+height, x:x+width]

	# Just a random number generator to get one of three
	# possible Shrek faces
	ranNum = random.randint(1,4)

	# Grabs corresponding image of Shrek
	shrekImage = homedir + '/FinalProject-ATJunior-Year/Shrek' + str(ranNum) + '.jpg'

	# Layers images here, and using .thumbnail crops it
	# Weirdly the hardest part of the entire project, but
	# maybe that's just indicitive of how easy of a project
	# I chose
	second_image = Image.open(shrekImage)
	second_image.thumbnail((width*1.1, height*1.1))
	first_image.paste(second_image, (x,y))

# Title for the image opened
title = "Get Shreked"

# Displays the image (title stuff doesn't really work)
first_image.show(title='Get Shreked',command=None)