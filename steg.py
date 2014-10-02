#Richard Dennis Steg tool
import Image
import os
import re
import io
import numpy
from itertools import izip_longest
from itertools import chain

codes = (
	(146, 28, 135) #Purple
	)

def conversion_png_ppm(png_file):
	#Converts a png image to pgm 
	print "Taking image to be inputted, and converting it to ppm"
	im = Image.open(png_file)
	im = im.convert('RGB')
	im.save('Portsmouth.ppm')

	file_size_of_pgm = os.stat('Portsmouth.ppm').st_size #Gets the file size of the image in byte

	#Make sure we have enough space to add the data, if under 5mb ? then close
	if file_size_of_pgm < 5000000:
		print "PGM file size is too small exiting now"
		sys.exit("System exiting")

def reading_ppm(ppm_file):
	# Open the PPM file and process the 3 first lines (HEADER
	file_name = ppm_file
	f = open (file_name)
	color = f.readline().splitlines()
	size_x, size_y = f.readline().split()
	max = f.readline().splitlines()

	print "\nGrid size"
	print "x", size_x
	print "y", size_y

	#Makes sure it is a PPM image
	assert color == ['P6'] #P6 format of the same image will store each color component of each pixel with one byte (thus three bytes per pixel) in the order Red, Green then Blue

	#Reads the rest of the image
	data = f.read().split()

	# Making sure the data has all RGB and not corrupted
	# print len(data)
	# print len(data) / 3 

	return data, size_x, size_y

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)	

def value_check(pixels):
	if any(146 in p for p in pixels):
		print "Purple"
	else:
		print "no purple"


def value_check_editted(pixels):
	if any(147 in p for p in pixels):
		print "Purple has been changed"
	else:
		print "no purple"

#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

#Text to be hidden within the image 
text_to_be_hidden = "this is a test"

#Converts text to binary (NO spaces)
text_to_be_hidden_binary = ''.join(format(ord(x), 'b') for x in text_to_be_hidden)

#User info
print "text to be hidden:", text_to_be_hidden
print "text to be hidden in binary:", text_to_be_hidden_binary

conversion_png_ppm('Portsmouth.png')
data, x, y = reading_ppm ('Portsmouth.ppm') 

pixels = grouper(map(ord, data[0]), 3)

value_check(pixels)

#Pixel locations for last circle
start = 2148 #Start on X
end = 3505 #End on X
#Y not required ?

# print len(list(pixels))


pixels = list(pixels)
for pixel in pixels[2148:3505]:
  if pixel[0] == 146:
    pixel[0] + 1

value_check_editted(pixels)
