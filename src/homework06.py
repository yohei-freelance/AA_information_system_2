#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:22:32 2018

@author: yohei
"""

import numpy as np

T=[[1/3,1/4,0,1/4,0,0,0,0,0],
[1/3,1/4,1/3,0,1/5,0,0,0,0],
[0,1/4,1/3,0,0,1/4,0,0,0],
[1/3,0,0,1/4,1/5,0,1/3,0,0],
[0,1/4,0,1/4,1/5,1/4,0,1/4,0],
[0,0,1/3,0,1/5,1/4,0,0,1/3],
[0,0,0,1/4,0,0,1/3,1/4,0],
[0,0,0,0,1/5,0,1/3,1/4,1/3],
[0,0,0,0,0,1/4,0,1/4,1/3]]
    
#様々な解き方がある、とあるが基本的に2でやるのが楽そうなので今回はそれで解くことにする。
lmd,V = np.linalg.eig(T)
vector = np.zeros(9)

def markov_normal():
    for i in range(len(lmd)):
        if lmd[i] == 1:
            c = i
    for i in range(len(lmd)):
        vector[i] = V[i][c]
    norm = np.sum(vector)
    for i in range(len(lmd)):
        vector[i] = vector[i]/norm
    return (vector)

#print(markov_normal())

#以下、発展課題に取り組んでみる。
#対称性を考えて,3×3の行列を用いて定常確率分布を計算する。
#定常分布では、初期状態の影響が極めて希薄になるため、0,2,6,8と1,3,5,7と4の三つの状態に大別できるとわかる。

def markov_advanced1(a,b,c,d):
    U = [[a,1-b-d,0],
         [1-a,b,1-c],
         [0,d,c]]
    lmd2,W = np.linalg.eig(U)
    vector2 = np.zeros(3)
    vector3 = np.zeros(9)
    for i in range(len(lmd2)):
        if lmd2[i] == max(lmd2):
            e = i
    for i in range(len(lmd2)):
        vector2[i] = W[i][e]
    norm = np.sum(vector2)
    for i in range(len(lmd2)):
        vector2[i] = vector2[i]/norm
    return(vector2)
    
def advanced_answer():
    vector4 = markov_advanced1(1/3,1/4,1/5,1/4)
    comp1 = vector4[0]*(1/4)
    comp2 = vector4[1]*(1/4)
    vector5 = [comp1,comp2,comp1,comp2,vector4[2],comp2,comp1,comp2,comp1]
    return (vector5)

#print(advanced_answer())
#上二つは確かに回答が一致しているので正解しているとわかる。

#最後に、定常分布が一様分布になるようなことがあるか考える。
#対称性を考えれば、行列Tを使うのではなくUを使う表現で十分であることが予想できる。
#そのために、markov_advanced1関数の行列Uにおける各数を微小変化させ当てはまるものが存在するか探す。
#本当は計算リソースを節約するために勾配法のような工夫ができるといいのだが、できなかった。

ideal_answer=[4/9,4/9,1/9]

def markov_advanced2():
    delta = 0.0001
    a,b,c,d = 0,0,0,0
    normlist = []
    while a < 1:
        while b < 1:
            while c < 1:
                while d < 1:
                    absolute = np.subtract(ideal_answer,markov_advanced1(a,b,c,d))
                    normlist.append(np.linalg.norm(absolute))
                    d = d + delta
                absolute = np.subtract(ideal_answer,markov_advanced1(a,b,c,d))
                normlist.append(np.linalg.norm(absolute))
                c = c + delta
            absolute = np.subtract(ideal_answer,markov_advanced1(a,b,c,d))
            normlist.append(np.linalg.norm(absolute))
            b = b + delta
        absolute = np.subtract(ideal_answer,markov_advanced1(a,b,c,d))
        normlist.append(np.linalg.norm(absolute))
        a = a + delta
    return(min(normlist))
    
print(markov_advanced2())
#deltaを微小変化させても、答えはデルタのオーダーほど小さくならない。
#しかし、オーダー的に浮動小数点によって収束しないだろうことは容易に予想される。
#おそらく一様になるような解は存在するが(もしくは極めてそれに近い近似解は存在するが)、確実に確かめることはできなかった。
