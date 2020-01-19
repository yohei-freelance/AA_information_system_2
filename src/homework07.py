#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:35:50 2018

@author: yohei
"""

# -*- coding: utf-8 -*-
from numpy import *
from pylab import *

delta = 0.1 #微小時間を定義
T = arange(0.0,10.0,delta) #各点としての時間を定義
N = T.shape[0] #計測回数をカウント
X = zeros((N,4)) #

# Initial state
X[0,:] = [pi/3,pi/3,0,0]



def Preparation_for_RungeKutta(a,b,c,d):
    A = array([[16/3,2*cos(a-b)],[2*cos(a-b),4/3]])
    t = array([-9.8 * 3 * sin(a) + 2 * sin(a-b) * (-d**2) , -9.8 * sin(b) + 2 * sin(a-b)*(c**2)])
    x = linalg.solve(A,t)
    f = array([c,d,x[0],x[1]])
    return f
    
for n in range(N-1):
    K1 = Preparation_for_RungeKutta(X[n,0],X[n,1],X[n,2],X[n,3])
    K2 = Preparation_for_RungeKutta((X[n,:]+0.5*delta*K1)[0],(X[n,:]+0.5*delta*K1)[1],(X[n,:]+0.5*delta*K1)[2],(X[n,:]+0.5*delta*K1)[3])
    K3 = Preparation_for_RungeKutta((X[n,:]+0.5*delta*K2)[0],(X[n,:]+0.5*delta*K2)[1],(X[n,:]+0.5*delta*K2)[2],(X[n,:]+0.5*delta*K2)[3])
    K4 = Preparation_for_RungeKutta((X[n,:]+delta*K3)[0],(X[n,:]+delta*K3)[1],(X[n,:]+delta*K3)[2],(X[n,:]+delta*K3)[3])
    X[n+1,:] = X[n,:]+delta/6*(K1+2*K2+2*K3+K4)

plot(T,X[:,0])
plot(T,X[:,1])
xlabel("Time[s]")
ylabel("Change")
show()