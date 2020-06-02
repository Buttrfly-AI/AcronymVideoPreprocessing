import shutil
import os

base_dir = '/home/jupyter/Acronym/video_processing/acronym_errolson'


acronym_256_test = base_dir + '/acronym_256_test/' 
acronym_256_train = base_dir + '/acronym_256_train/' 


data_test_dir = '/home/jupyter/Acronym/video_processing/first_order_model/data/acronym/test'

data_train_dir = '/home/jupyter/Acronym/video_processing/first_order_model/data/acronym/train'

test_entries = os.listdir(acronym_256_test)
train_entries = os.listdir(acronym_256_train)

print(len(train_entries))



for file in test_entries:
    file = '{}/{}'.format(acronym_256_test,file)
    shutil.move(file,data_test_dir)
    
    
for file in train_entries:
    file = '{}/{}'.format(acronym_256_train,file)
    shutil.move(file,data_train_dir)