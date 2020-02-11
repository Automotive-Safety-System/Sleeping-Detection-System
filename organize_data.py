import os
import time
import shutil

eyestate_index = 16
print('place the file near the mrlEyes_2018_01 folder')
print('You are currently in: ' + os.getcwd())

root_folder = os.getcwd()

if('mrlEyes_2018_01' in os.listdir()):
    print('Success, folder found!')
    try:
        os.mkdir('closed')
        os.mkdir('open')
        print('directories made!')
    except:
        print('Failed making directories')
else:
    print('failed, place the file in the same folder with the test/train folders and try again')
    time.sleep(5)
    exit()
open_dir = root_folder + '\open'
closed_dir = root_folder + '\closed'

os.chdir(root_folder + '\mrlEyes_2018_01')
folders = os.listdir()
print(folders)

# move the data
for folder in folders:
    os.chdir(root_folder + '\mrlEyes_2018_01/' + folder)
    images = os.listdir()
    for image in images:
        if(image[eyestate_index] == '0'):
            shutil.move(image, closed_dir)
        else:
            shutil.move(image, open_dir)
else:
    print('sorting data done!')