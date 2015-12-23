#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Filename: handwriting.py
@Author: yew1eb
@Date: 2015/12/23 0023
"""
# http://blog.csdn.net/u012162613/article/details/41978235#0-tsina-1-23162-397232819ff9a47a7b7e80a40613cfe1
# http://blog.csdn.net/u013691510/article/details/43195227
# https://www.kaggle.com/c/digit-recognizer/data
# https://github.com/MarcoGiancarli/DigitRecognizer/tree/master/gen
# https://github.com/dzhibas/kaggle-digit-recognizer/tree/master/py-knn
# https://github.com/Broham/DigitRecognizer/blob/master/DigitRecognizer.py
import pandas as pd
import numpy as np

# 归一化数据
def nomalizing(data):
    data = data.values.apply(lambda x:1 if x!=0 else 0)
    print(data)
    return data

def get_train_data():
    data = pd.read_csv('d:\\dataset\digits\\train.csv')
    train_data = data.iloc[:,1:]
    label = data['label']
    return nomalizing(train_data), label

def main():
    get_train_data()

if __name__ == '__main__':
    main()