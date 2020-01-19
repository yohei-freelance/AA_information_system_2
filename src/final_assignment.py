#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:50:11 2018

@author: yohei
"""

import pyprind
import pandas as pd
import os
from collections import Counter
import re
from sklearn.feature_extraction.text import CountVectorizer as CV
from nltk.stem.porter import PorterStemmer as PS
from nltk.corpus import stopwords

count = CV()
porter = PS()
stop = stopwords.words('english')

class Final_Assignment:
    
    def tokenizer_porter(self, text):
        return [porter.stem(word) for word in text.split()]
    
    def merge_dict_add_values(self, d1, d2):
        return dict(Counter(d1) + Counter(d2))

    def making_csv(self):
        basepath = 'aclImdb'
        labels = {'pos':1, 'neg':1}
        pbar = pyprind.ProgBar(50000)
        df = pd.DataFrame()
        merged1 = {}
        merged2 = {}
        for s in ('test', 'train'):
            for l in ('pos', 'neg'):
                path = os.path.join(basepath, s, l)
                for file in os.listdir(path):
                    with open(os.path.join(path, file), 'r', encoding='utf-8') as infile:
                        txt = infile.read()
                        txt = re.sub('<[^>]*>.?,/', '', txt)
                        temporal_list = [w for w in tokenizer_porter(txt)[-10:]
                        if w not in stop]
                        c = Counter(temporal_list)
                        if l == 'pos':
                            merged1 = merge_dict_add_values(merged1, c)
                            merged_1 = sorted(merged1.items(), key=lambda x: -x[1])
                            if len(merged1) > 310:
                                merged_1 = merged_1[:310]
                            merged1 = dict(merged_1)
                        else:
                            merged2 = merge_dict_add_values(merged2, c)
                            merged_2 = sorted(merged2.items(), key=lambda x: -x[1])
                            if len(merged_2) > 310:
                                merged_2 = merged_2[:310]
                            merged2 = dict(merged_2)
                    df = df.append([[temporal_list, labels[l]]], ignore_index=True)
                    pbar.update()
        df.columns = ['review', 'sentiment']
        merged_1 = sorted(merged1.items(), key=lambda x: -x[1])
        merged_2 = sorted(merged2.items(), key=lambda x: -x[1])
        merged_1 = merged_1[10:]
        merged_2 = merged_2[10:]
        with open('merged1.csv', 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(merged_1)
        with open('merged2.csv', 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(merged_2)
        #print(merged1)
        #print(merged2)
        #print(df)
    
    def analysis(self, text):
        text = text.lower()
        text = text.replace(',', '')
        text = text.replace('.', '')
        print(text)
        txtlist = tokenizer_porter(text)
        positive = 0
        negative = 0
        with open('merged1.csv', 'r') as f:
            dataReader = csv.reader(f, lineterminator='\n')
            for row in dataReader:
                for word in txtlist:
                    for l in row: 
                        if word == l:
                            positive += 1
        with open('merged2.csv', 'r') as f:
            dataReader = csv.reader(f, lineterminator='\n')
            for row in dataReader:
                for word in txtlist:
                    for l in row: 
                        if word == l:
                            negative += 1
        if (positive != 0) and (negative != 0):
            if positive >= negative:
                prediction = (100*positive)/(positive + negative)
                prediction = str(prediction)
                print ("今日のあなたは" + prediction +"%の良い一日でした！")
            else:
                prediction = (100*negative)/(positive + negative)
                prediction = str(prediction)
                print ("今日のあなたは" + prediction +"%のちょっぴり災難な一日でした..")
        else:
            print("測定不能でした...。ごめんなさい！")

final = Final_Assignment()
#final.making_csv()
final.analysis('I ate sushi today. it was delicious.')