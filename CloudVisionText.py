
import argparse
from enum import Enum
import io

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
from group_word import*

import base64
import enchant


space_x = 10
space_y = 10

def annotate_text(filein):
	client = vision.ImageAnnotatorClient()

	with open(str(filein), "rb") as imageFile:
		content = imageFile.read()

	image = vision.types.Image(content = content)
	resp = client.text_detection(image = image)
	
	output = []

	for d in resp.text_annotations[1:]:
		word = Group_Word(d.description, d.bounding_poly.vertices[0].x, d.bounding_poly.vertices[0].y, d.bounding_poly.vertices[2].x - d.bounding_poly.vertices[0].x, d.bounding_poly.vertices[2].y - d.bounding_poly.vertices[0].y, 0)

		output.append(word)

	return output

def determine_math(word_array):
	dict = enchant.Dict("en_US")
	

	for word in word_array:

		word_dictionary_description = word.get_description().translate({ord(c): None for c in '.?,;:!`()%'}).lower()

		if (word_dictionary_description != '' and dict.check(word_dictionary_description)):
			if (verify_helper(word_dictionary_description)):
				word.set_math(1)
		else: 
			word.set_math(1)

def verify_helper(string):
	if string in {"n", "x", "y", "z", "k", "p", "q", "b", "c", "e", "f", "g", "m"} or string.isnumeric():
		return True
	else:
		return False

def make_lines(word_array, img_width, img_height):
	return_val = [[word_array[0]]]
	for i in range(len(word_array) - 2):
		word = word_array[i]
		next_word = word_array[i + 1]

		valid_merge = word.should_merge_lines(next_word, space_y, img_height)
		#print (word.toString(), next_word.toString(), valid_merge)

		if valid_merge[1] == False: #on different lines
			return_val.append([next_word])
		else: #math or text match, 
			return_val[-1].append(next_word)
	return return_val

	# for line in return_val:
	# 	print ("[")
	# 	for line_word in line:
	# 		print(line_word.toString())
	# 	print("]")

def condense_lines (word_array, img_height):

	return_val = [word_array[0][0]]

	for line in word_array:
		if (len(line) <= 1):
			return_val.append(line[0])
		else:
			for i in range(len(line) - 2):
				next_word = line[i+1]
				if line[i].should_merge_lines(next_word, space_y, img_height)[0] == True: #line characters all same
					return_val[-1] = return_val[-1].merge(next_word)
				else if line[i].should_merge_lines(next_word, space_y, img_height)[0] == False and line[i].should_merge_lines(next_word, space_y, img_height)[1] == True:
					
				else:
				 	return_val.append(next_word)
	for line in return_val:
		print(line.toString())
	print("END")

def make_paragraph():
	return 0




if __name__ == '__main__':
    # [START vision_document_text_tutorial_run_application]
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    parser.add_argument('-out_file', help='Optional output file', default=0)
    args = parser.parse_args()

    parser = argparse.ArgumentParser()
    image_to_process = args.detect_file

    word_array = annotate_text(image_to_process)
    determine_math(word_array)

    width, height = Image.open(image_to_process).size

    lines_array = make_lines(word_array, width, height)
    condense_lines(lines_array, height)

    '''for d in word_array:
    	print(d.toString())'''


    # [END vision_document_text_tutorial_run_application]
# [END vision_document_text_tutorial]







	