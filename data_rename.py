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

for sub in subfolders:
  i = sub.split("/")[-1]
  name = flowers_name[i]
  print(sub, name)
  rename = data_folder + "/" + name
  os.rename(sub, rename)


# 
