# pip install -r requirements.txt
# eigenfaces vs eigenvector
# pylab
# https://medium0.com/m/global-identity?redirectUrl=https%3A%2F%2Ftowardsdatascience.com%2Fbuilding-a-facial-recognition-model-using-pca-svm-algorithms-c81d870add16
# pip install Pillow

# Refs: https://git-disl.github.io/GTDLBench/datasets/att_face_dataset/
# https://github.com/mohamed-elsayed-mohamed/Face-Recognition
# https://github.com/harveyslash/Facial-Similarity-with-Siamese-Networks-in-Pytorch/blob/master/Siamese-networks-medium.ipynb

# https://github.com/yuzhounh/2DPCAL1-S

import tensorflow as tf
import time
import math
import os
from PIL import Image, ImageDraw, ImageFont
# import scipy.misc
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

training_dir = 'AT&T'
# testing_dir = 'AT&T'
imageSize = 92*112
imageWidth = 92
imageHeight = 112

def LoadTrainingData(Dir, Img_Shape):
    (Images, Lbls, Labels, ID, NClasses) = ([], [], [], 0, 0)
    for(_, Dirs, _) in os.walk(Dir):
        Dirs = sorted(Dirs)
        for SubDir in Dirs:
            SubjectPath = os.path.join(Dir, SubDir)
            for FileName in os.listdir(SubjectPath):
                path = SubjectPath + "/" + FileName
                Img = plt.imread(path) #mode = 'L'
                #print Img.shape
                (height, width) = Img.shape
                if(width != Img_Shape[0] or height != Img_Shape[1]):
                    Img = Img.resize((Img_Shape[0], Img_Shape[1]))

                Images.append(Img)
                Lbls.append(int(ID))
            NClasses += 1
            ID += 1

    Images, Lbls = shuffle(Images, Lbls)
    Images = np.asarray(Images, dtype='float32').reshape([-1, Img_Shape[0], Img_Shape[1], 1]) /255
    for label in Lbls:
        Labels.append(Categorical([label], NClasses)[0])

    return (Images, np.asarray(Labels))

def Categorical(y, NClasses):
    y = np.asarray(y, dtype='int32')
    if not NClasses:
        NClasses = np.max(y)+1
    Y = np.zeros((len(y), NClasses))
    for i in range(len(y)):
        Y[i, y[i]] = 1.
    return Y

X, Y= LoadTrainingData(training_dir, (imageWidth, imageHeight))
print(Y[0])