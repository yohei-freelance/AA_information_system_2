#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 21:52:43 2018

@author: yohei
"""

import pickle
import os

dest = os.path.join('movieclassifier', 'pkl_objects')
if not os.path.exists(dest):
    os.makedirs(dest)
    pickle.dump(stop,
                open(os.path.join(dest, 'stopwords.pkl'),'wb'),
                protocol = 4)
    pickle.dump(c1f,
                open(os.path.join(dest, 'classifier.pkl'), 'wb'),
                protocol=4)

import pickle
import re
import os
from vectorizer import vect

clf = pickle.load(open(os.path.join('pkl_objects', 'classifier.pkl'), 'rb'))