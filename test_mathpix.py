import sys
import base64
import requests
import json

# put desired file path here



def printLatex(filepath, top_x = None, top_y = None, width = None, height = None):
        file_path = '/Users/shriyanadgauda/Documents/GitHub/api-examples/images/physics.jpg'
        image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode("utf-8")
        if(top_x != None):
                r = requests.post("https://api.mathpix.com/v3/latex",
                data=json.dumps({'src': image_uri}),
                headers={"app_id": "snadgauda_g_hmc_edu", "app_key": "9cb6ed9da767ecbd1748",
                        "Content-type": "application/json", "region": "top_left_x: " + str(top_x) + ", top_left_y: " + str(top_y) + 
                        ", width: " + str(width) + ", height: " + str(height)})
        else:
                r = requests.post("https://api.mathpix.com/v3/latex", 
                data=json.dumps({'src': image_uri}),
                headers={"app_id": "snadgauda_g_hmc_edu",  "app_key": "9cb6ed9da767ecbd1748", "Content-type": "application/json"})
        dic = json.loads(r.text)
        latex = dic["latex"]
        position = dic["position"]
        width = position["width"]
        height = position["height"]
        top_left_x = position["top_left_x"]
        top_left_y = position["top_left_y"]
        return([latex, width,height,top_left_x,top_left_y])


 
    

