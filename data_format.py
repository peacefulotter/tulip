
import os
import numpy as np
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True, choices=["train", "valid"])
args = parser.parse_args()
folder = args.f

flowers_name = None
with open("cat_to_name.json") as file:
    flowers_name = json.load(file)

data_folder = r"./flower_data/" + folder
subfolders = [f.path for f in os.scandir(data_folder) if f.is_dir()]

data = {
    "size": [00 for i in range(len(flowers_name))],
    "name": ["" for i in range(len(flowers_name))]
}

for sub in subfolders:
    size = len( os.listdir(sub) )
    i = sub.split("/")[-1]
    name = flowers_name[i]
    print(f"number: {i}, size: {size}, name: {name}")
    data["name"][int(i)-1] = name
    data["size"][int(i)-1] = size

def write_json(arr, file):
    json_ = json.dumps(arr, indent=4)
    with open(file, "w") as outfile:
        outfile.write(json_)

write_json(data, f"./classes_{folder}.json")
