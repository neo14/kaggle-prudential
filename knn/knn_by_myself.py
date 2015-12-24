#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@filename: knn_by_myself.py
@author: yew1eb
@site: http://blog.yew1eb.net
@contact: yew1eb@gmail.com
@time: 2015/12/24 下午 9:59
'''
import numpy as np
import time

def load_data():
    dataset_size = 1000
    train_data = np.loadtxt('d:/dataset/digits/train.csv', dtype=np.uint8,delimiter=',', skiprows=1)
    test_data = np.loadtxt('d:/dataset/digits/test.csv', dtype=np.uint8,delimiter=',', skiprows=1)
    label = train_data[:,:1]
    data  = np.where(train_data[:, 1:]!=0, 1, 0)# 数据归一化
    test  = np.where(test_data !=0, 1, 0)
    return data[:dataset_size], label[:dataset_size].T, test[:dataset_size]

def test_knn(test_data, test_label, train_data, train_label):
    start = time.clock()
    error = 0
    m = len(test_data)
    labels = []

    for i in range(m):
        calc_label = classify(test_data[i], train_data, train_label, 3)
        labels.append(calc_label)
        error = error +(calc_label != test_label[i])

    print('error: ', error)
    print('error percent: %f' % (float(error)/m))
    print('time cost: %f s' % (time.clock() - start))
    return labels

def classify(inx, train_data, train_label, k):
    sz = train_data.shape[0]
    inx_temp = np.tile(inx, (sz,1)) - train_data
    sq_inx_temp = inx_temp ** 2
    sq_distance = sq_inx_temp.sum(axis=1)
    distance = sq_distance ** 0.5
    sort_dist = distance.argsort()
    class_set = {}
    for i in range(k):
        print(sort_dist[i])
        print(train_label[:,245])
        label = train_label[0][sort_dist[i]]
        class_set[label] = class_set.get(label, 0) + 1
    sorted_class_set = sorted(class_set.iteritems(), key=lambda d:d[1], reverse=True) # 按字典中的从大到小排序
    return sorted_class_set[0][0]














