# Sleeping-Detection-System

## Prerequisites
`` pip install face_recognition ``

you will also need to have [PyTorch](https://pytorch.org/get-started/locally/) installed


## Dataset
http://mrl.cs.vsb.cz/eyedataset

### Preprocessing the data:
1- Unzip the file

2- Place the `organize_data.py` and the `run_script.bat` in the same directory near `mrlEyes_2018_01` directory

3- Run the `run_script.bat` file

The data will now be separated into `closed` & `open` directories indicating the state of the eyes.

## Models
|     Model     |    Accuracy   |     Time      |
| ------------- | ------------- | ------------- |
|   RESNET18    |      99%      |      80ms     |
