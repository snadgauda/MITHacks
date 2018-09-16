
import argparse
from enum import Enum
import io

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
from group_word import*


import base64

def annotate_text(filein):

	client = vision.ImageAnnotatorClient()

	with open(str(filein), "rb") as imageFile:
		content = imageFile.read()

	image = vision.types.Image(content = content)
	resp = client.text_detection(image = image)
	
	for d in resp.text_annotations[1:]:
		word = Group_Word(d.description, d.bounding_poly.vertices[0].x, d.bounding_poly.vertices[0].y, d.bounding_poly.vertices[2].x - d.bounding_poly.vertices[0].x, d.bounding_poly.vertices[2].y - d.bounding_poly.vertices[0].y)

		print(word.toString())


if __name__ == '__main__':
    # [START vision_document_text_tutorial_run_application]
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    parser.add_argument('-out_file', help='Optional output file', default=0)
    args = parser.parse_args()

    parser = argparse.ArgumentParser()
    annotate_text(args.detect_file)
    # [END vision_document_text_tutorial_run_application]
# [END vision_document_text_tutorial]







	