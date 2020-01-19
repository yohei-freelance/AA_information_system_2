#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 22:25:24 2018

@author: yohei
"""
#以下では#を消せば関数を呼び出すことができる.
#words.txtを読み込む.
words = []
fin = open('words.txt')
for line in fin:
    words.append(line.strip())
fin.close

#文字数の多い単語、上位10個は? --> listを利用する.

def top_letters():
    toplist = words[:10]
    toplist.sort(key=lambda x: len(x))
    for i in range(10,len(words)):
        if len(words[i]) > len(toplist[0]):
            toplist[0] = words[i]
            toplist.sort(key=lambda x: len(x))
    return (toplist)
# top_letters()
toplist = top_letters()
        
#何文字の単語が最も多いか？ --> dictを利用する.
def top_letters():
    letters = dict()
    for i in range(len(toplist[9])):
        letters[i+1] = 0
    for i in words:
        letters[len(i)] += 1
    print(max(letters, key=(lambda x: letters[x])))
# top_letters()

#各アルファベット文字の出現回数は？　--> dictを利用する.
alphabets = "abcdefghijklmnopqrstuvwxyz"

def top_alphabets():
    alpha_numbers = dict()
    for i in alphabets:
        alpha_numbers[i] = 0
    for i in words:
        for j in i:
            alpha_numbers[j] += 1  
    print(alpha_numbers)
# top_alphabets()

#同じ文字を二個以上含まない単語の中で最も文字数が多いのは？
def single_longs():
    longest = words[0]
    for i in words:
        simple_manage = dict()
        for j in alphabets:
            simple_manage[j] = 0
        for j in i:
            simple_manage[j] += 1
        temp_list = simple_manage.values()
        if max(temp_list) < 2:
            if len(i) > len(longest):
                longest = i
    print(longest)
#single_longs()