import sklearn
import os
import numpy as np
import glob
import random

import shutil
data = np.array(os.listdir('/home/jupyter/Acronym/video_processing/acronym_errolson/phonemes'))



data = data.reshape((data.shape[0],1))

test_pics_num = round(len(data)*.20)

tests =[data[random.randint(0,len(data)-1)] for x in range(test_pics_num)]


train = [x for x in data if x not in tests]


print(len(data))

print(len(train))

print(len(tests))


# for file in tests:
#     print(file)
#     source="/home/jupyter/Acronym/video_processing/scripts/Errolson_256/{}".format(file[0])
#     destination ="/home/jupyter/Acronym/video_processing/scripts/Errolson_test/{}".format(file[0])
#     try:
#         shutil.move(source, destination)
#     except:
#         pass
        