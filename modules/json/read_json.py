import json 
import os 

def read_json(filename: str) -> dict:
    file_path = os.path.abspath(__file__ + "/../../../static/json/" + filename)
    with open(file_path, 'r') as file:
        return json.load(file)
    