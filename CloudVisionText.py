
import argparse
from enum import Enum
import io

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
from group_word import*

import base64
import enchant
from mathpix import*


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

		word_dictionary_description = word.get_description().translate({ord(c): None for c in '.\\?,;:!`()%/'}).lower()

		if (word_dictionary_description != '' and dict.check(word_dictionary_description)):
			if (verify_helper(word_dictionary_description)):
				word.set_math(1)
		else: 
			word.set_math(1)

def verify_helper(string):
	if string in {"n", "x", "y", "z", "k", "p", "q", "b", "c", "e", "f", "g", "m"}:
		return True
	else:
		return False

def make_lines(word_array, img_width, img_height):
	return_val = [[word_array[0]]]
	for i in range(len(word_array) - 1):
		word = word_array[i]
		next_word = word_array[i + 1]

		valid_merge = word.should_merge_lines(next_word, space_y, img_height)
		#print (word.toString(), next_word.toString(), valid_merge)

		if valid_merge[1] == False: #on different lines
			return_val.append([next_word])
		else: #math or text match, 
			return_val[-1].append(next_word)

	# for line in return_val:
	# 	for line_word in line:
	# 		print(line_word.toString())
	return return_val

	
def condense_lines (word_array, img_height, file_path):

	return_val = [Group_Word()]

	for word_list in word_array:
		for word in word_list:

			if (return_val[-1].get_math() == word.get_math()):
				return_val[-1] = return_val[-1].merge(word)
			else:
				return_val += [word]


	return_val2 = []
	for word in return_val:
		if word.get_math():
			return_val2 += [printLatex(file_path, word)]
		else:
			return_val2 += [word]		

	for line in return_val2:
		print(line.toString())
		print("=========================")
				
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
    condense_lines(lines_array, height, image_to_process)

    '''for d in word_array:
    	print(d.toString())'''


    # [END vision_document_text_tutorial_run_application]
# [END vision_document_text_tutorial]







	