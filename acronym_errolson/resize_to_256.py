from PIL import Image
import os


import shutil

base_dir = '/home/jupyter/Acronym/video_processing/acronym_errolson'
acronym_raw_test = base_dir + '/acro_test/test' 
acronym_raw_train = base_dir + '/acro_test/train' 

acronym_256_test = base_dir + '/acro_test_256/test/' 
acronym_256_train = base_dir + '/acro_test_256/train/' 


test_entries = os.listdir(acronym_raw_test)
train_entries = os.listdir(acronym_raw_train)


print(len(test_entries))
print(len(train_entries))



for item in test_entries:
    try:
        image = Image.open('{}/{}'.format(acronym_raw_test,item)) 
        image = image.resize((256,256))
        image.save('{}/{}'.format(acronym_256_test,item))
    except:
        pass


for item in train_entries:
    try:
        image = Image.open('{}/{}'.format(acronym_raw_train,item)) 
        image = image.resize((256,256))
        image.save('{}/{}'.format(acronym_256_train,item))
    except:
        pass