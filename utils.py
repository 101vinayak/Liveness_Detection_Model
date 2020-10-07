import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

import numpy as np 
import keras
from keras.models import model_from_json
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

def get_dataset():
    
    live_img = ["img-live/"+f for f in listdir("img-live/") if isfile(join("img-live/", f))]
    live_label = [0 for i in range(len(live_img))]

    not_live_img = ["img-not-live/" + f for f in listdir("img-not-live/") if isfile(join("img-not-live/", f))]
    not_live_label = [1 for i in range(len(not_live_img))]
    
    return (live_img, live_label, not_live_img, not_live_label)

def get_model():
    
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),
                    activation='relu',
                    input_shape=(100,100,3)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax'))

    return model