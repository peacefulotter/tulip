# TODO: Use Flowers102 dataset
import json
import torch
import torch.nn as nn
import numpy as np

from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from PIL import Image


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

data_folder = r"./data/flower_data/flower_data/" + folder
subfolders = [f.path for f in os.scandir(data_folder) if f.is_dir()]

for sub in subfolders:
  i = sub.split("\\")[-1]
  name = flowers_name[i]
  print(sub, name)
  rename = data_folder + "/" + name
  os.rename(sub, rename)



class FlowerDataset(datasets.ImageFolder):
    def __init__(self, root, class_file, transform=None, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.sizes, self.names = self._get_classes(class_file)
        
    def _get_classes(self, class_file: str):
        with open(class_file) as file:
            arr = json.load(file)
            sort_indices = np.argsort(arr["name"])
            return np.array(arr["size"])[sort_indices], np.array(arr["name"])[sort_indices]

    def label_name(self, target):
      return self.names[target]

base_folder = "./data/flower_data/flower_data/"
batch_size = 16

def get_dataset(train):
  subfolder = "train" if train else "valid"
  root = base_folder + subfolder
  class_file = f'classes_{subfolder}.json'

  transform = transforms.Compose( [
      transforms.ToTensor(), 
      # transforms.Normalize((mean,), (std,))
  ] )
  dataset = FlowerDataset(
      root=root, 
      transform=transform,
      class_file=class_file
  )

  print(dataset)
  print(dir(dataset))
  data = np.array([transform(dataset.loader(path)) for path, target in dataset.imgs])
  mean = np.round(data.mean(axis=(0,1,2))/255,4)
  std = np.round(data.std(axis=(0,1,2))/255,4)
  print(f"mean: {mean}\nstd: {std}")

  loader = torch.utils.data.DataLoader(
      dataset, 
      batch_size=batch_size, 
      pin_memory=torch.cuda.is_available(),
      shuffle=train,
      num_workers=2 if train else 1,
    )
  return dataset, loader

tr_dataset, tr_loader = get_dataset(train=True)
