import random

import os

import shutil


entries = os.listdir('./_frames/')

test_amount = (round((len(entries) -1) * 0.2))
tests = random.sample(entries, k=test_amount)

train = [item for item in entries if item not in tests]

print(len(train))



for file in tests:
    print
    source="/home/jupyter/Acronym/video_processing/acronym_errolson/_frames/{}".format(file)
    destination ="/home/jupyter/Acronym/video_processing/acronym_errolson/test/{}".format(file)
    try:
        shutil.move(source, destination)
    except:
        pass


for file in train:
    print
    source="/home/jupyter/Acronym/video_processing/acronym_errolson/_frames/{}".format(file)
    destination ="/home/jupyter/Acronym/video_processing/acronym_errolson/train/{}".format(file)
    try:
        shutil.move(source, destination)
    except:
        pass