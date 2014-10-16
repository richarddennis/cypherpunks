import Image
import os
import re
import io
import numpy
from itertools import izip_longest
from itertools import chain
import sys

def reading_ppm(file_name):
	f = open (file_name)
	setting = f.readline().splitlines()
	comment = f.readline().splitlines()
	size_x, size_y = f.readline().split()
	pixel_max = f.readline().splitlines()
	orig_data = f.read().split()		
	return size_x,size_y,pixel_max, orig_data

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)	

def hidding_data_to_image(text_to_be_hidden_binary, data):
	print "test"
	#Not bothering converting the RGB to binary, as the addition of 1 to 200 etc  = 201 same as binary, quicker this way
	#Green is 20 200 20
	x = 0
	for i,v in enumerate(data) :
		if x < len(text_to_be_hidden_binary):
			if v==20 or v==200 :
				data[i]+= int(text_to_be_hidden_binary[x])
				x = x + 1																			
	return data


def writting_ppm(ppm_file,size_x,size_y,maxval,data):
    colour = 'P3'

    # leave data as a list
    maxval =  max(maxval) # use max to get the max int in a list
    with open(ppm_file, "w") as text_file:
        text_file.write(colour + "\n" + "\n" +str(size_x) + " " + str(size_y) + "\n" + str(maxval) +"\n")
        for each in data:
            text_file.write(str(each)+'\n')


#Text to be hidden within the image 
text_to_be_hidden = "this is a test for example i want to see how much data can be added and it seems like a lot can be for example cypherwy2vflxo3qdotonion "
#Converts text to binary (NO spaces)
text_to_be_hidden_binary = ''.join(format(ord(x), 'b') for x in text_to_be_hidden)

L = list(text_to_be_hidden_binary)

print type(text_to_be_hidden_binary)
print text_to_be_hidden_binary

ppm_file = "portsmouth_origtext.ppm"

size_x,size_y,pixel_max, orig_data = reading_ppm(ppm_file)

data = map(int, orig_data)

assert len(data)/3 == (int(size_x) * int(size_y)) #Checks all values have been extracted
# value_check_editted(data)

hidding_data_to_image(text_to_be_hidden_binary, data)

writting_ppm("portsmouth_steg.ppm",size_x,size_y,pixel_max, data)