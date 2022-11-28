import os
import shutil

folder = r"./data/flower_data/flower_data/train"
subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]

for sub in subfolders:
    print("sub ", sub)
    for f in os.listdir(sub):
        src = os.path.join(sub, f)
        dst = os.path.join(folder, f)
        shutil.move(src, dst)
