import sys
import base64
import requests
import json

from group_word import *
# put desired file path here



def printLatex(file_path, input_math):
        image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode("utf-8")

        r = requests.post("https://api.mathpix.com/v3/latex",
        data=json.dumps({'src': image_uri}),
        headers={"app_id": "snadgauda_g_hmc_edu", "app_key": "9cb6ed9da767ecbd1748",
                "Content-type": "application/json", "region": "top_left_x: " + str(input_math.get_x()) + ", top_left_y: " + str(input_math.get_y()) + 
                ", width: " + str(input_math.get_width()) + ", height: " + str(input_math.get_height())})

        dic = json.loads(r.text)
        latex = dic["latex"]

        # position = dic["position"]
        # width = position["width"]
        # height = position["height"]
        # top_left_x = position["top_left_x"]
        # top_left_y = position["top_left_y"]
        output_math = input_math
        output_math.set_description(str(latex))
        print (json.dumps(dic, indent = 4, sort_keys = True))
        return(output_math)


 
    

