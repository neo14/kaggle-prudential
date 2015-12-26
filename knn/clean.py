#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


path = 'D:/dataset/ucloud/race_data/test/'
file_list = os.listdir(path)

date_list = ['20151128', '20151129', '20151130']

data = []
for l in file_list:
    if os.path.isfile(path+l):
        print('open file: ' + l)
        file = open(path+l, mode='r', encoding='utf8')
        for line in file.readlines():
            splits = line.strip().split(sep='\t')
            if splits[1] in date_list:
                write = open(path+splits[1]+'.txt', 'a+', encoding='utf8')
                write.write(line)

