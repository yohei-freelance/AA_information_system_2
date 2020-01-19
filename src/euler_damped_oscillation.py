# 減衰振動の状微分方程式の数値解法
# Euler法 と 解析解(から得られる漸化式)、2次近似解を比較
from numpy import *
from pylab import *

# 減衰振動のパラメータ
gam = 0.3
ome2 = 1.0

# 時間の刻み幅
dlt = 0.1

# 時刻列 (0.0から10.0までdlt間隔で)
T = arange(0.0,10.0,dlt)
# 時刻列の長さ len(T) でも求められる
N = T.shape[0]
# 各時刻の計算結果を保存するための行列
X = zeros((N,2))
# 初期状態 (変位と速度)
X[0,:] = [1.0, 1.0]

# 行列A
A = array([[0.0,1.0],[-ome2,-2.0*gam]])

# ループ
for n in range(N-1):
    X[n+1,:] = X[n,:] + dlt * dot(A,X[n,])

# Plot by matplotlib
plot(T,X[:,0])
plot(T,X[:,1])
legend(['x','x dot'])
title('Solution by Euler method')
#show()

# 解析解（の漸化式）との比較
import scipy.linalg as scla
expdtA = scla.expm(dlt*A)
Xtr = zeros((N,2))
Xtr[0,:] = [1.0, 1.0]
for n in range(N-1):
    Xtr[n+1,:] = dot(expdtA,Xtr[n,])
figure()
plot(T,X[:,0])
plot(T,Xtr[:,0])
legend(['Euler','Analytical'])

# 2次近似 (テイラー級数3項法) との近似
P = eye(2)+dlt*A+0.5*dlt**2*dot(A,A)
Xsc = zeros((N,2))
Xsc[0,:] = [1.0, 1.0]
for n in range(N-1):
    Xsc[n+1,:] = dot(P,Xsc[n,])
figure()
plot(T,X[:,0])
plot(T,Xtr[:,0])
plot(T,Xsc[:,0])
legend(['Euler','Analytical','Second'])


