import torch
import numpy as np

from torchvision import datasets, transforms


def get_mean_std(dataset, transform):
  paths = []
  for path, target in dataset.imgs:
    paths.append(path)
  paths = np.array(paths)
  np.random.shuffle(paths)
  paths = paths[:300]
  print(paths.shape)

  data = [transform(dataset.loader(path)) for path in paths]
  data = torch.stack(data)
  print(data.shape)
  mean = np.round(data.mean(axis=(0,2,3)),4)
  std = np.round(data.std(axis=(0,2,3)),4)
  print(mean.shape, std.shape)
  print(f"mean: {mean}\nstd: {std}")