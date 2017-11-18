#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:30:06 2017

@author: diego
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split


def load_data(data):
    dataset = pd.read_csv(data)
    x = dataset.iloc[:,2:].values
    y = dataset.iloc[:,0].values
    #partitions = [0.5, 0.7, 0.8]

    sc = MinMaxScaler()
    x = sc.fit_transform(x)
    
    return x,y


# Apply K-Fold Cross Validation Split
def kfold(x,num):
    kf = KFold(n_splits=num,shuffle=True)
    return kf.split(x)


#Apply Random Split
def split(x,y,ratio):
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1-ratio)
    return x_train,x_test,y_train,y_test


