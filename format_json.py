
import os
import numpy as np
import json

flowers_name = None
with open("cat_to_name.json") as file:
    flowers_name = json.load(file)

print(flowers_name)

folder = r"./data/flower_data/flower_data/train"
subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]

data = {
    "size": [00 for i in range(len(flowers_name))],
    "name": ["" for i in range(len(flowers_name))]
}

for sub in subfolders:
    size = len( os.listdir(sub) )
    i = sub.split("\\")[-1]
    name = flowers_name[i]
    print(i, sub, size, name)
    data["name"][int(i)-1] = name
    data["size"][int(i)-1] = size

print(data)

def write_json(arr, file):
    json_ = json.dumps(arr, indent=4)
    with open(file, "w") as outfile:
        outfile.write(json_)

write_json(data, "classes.json")
