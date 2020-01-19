#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:21:50 2018

@author: yohei
"""

#考える微分方程式は,x::+0.6x:+x=0

import matplotlib.pylab as plt

f1 = 1 #f1は求めたい関数
g1 = 1 #g1は求めたい関数の導関数
dt = 0.01 #dtはオイラー法による近似の微小分割幅
n = 0
ts = [] #初期値をおく #0から20まで0.01刻みの配列を生成
y1 = [] #近似解を置くための配列

plt.xlabel("t")
plt.ylabel("f(t)")

while n <= 2000:
    t = n * dt
    f2 = f1 + dt * g1
    g2 = g1 + dt * (-2*0.3*g1 - 1.0*f1)
    ts.append(t)
    y1.append(f2)
    f1 = f2
    g1 = g2
    n = n+1
    
plt.scatter(ts,y1)
plt.show()
