# 減衰振動の状微分方程式の数値解法
# 以下の方法を比較
# (1) Euler 法 (1次近似)
# (2) 修正Euler 法 (2次近似)
# (3) Heun 法 (2次近似)
# (4) 解析解から得られる漸化式による方法

from numpy import *
from pylab import *
import scipy.linalg as scla

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
Xeu = zeros((N,2)) #Euler法用
Xmo = zeros((N,2)) #修正Euler法用
Xhe = zeros((N,2)) #Heun法用
Xtr = zeros((N,2)) #解析解用

# 初期状態
Xtr[0,:] = Xhe[0,:] = Xmo[0,:] =Xeu[0,:] =[1.0, 1.0]

# 行列A
A = array([[0.0,1.0],[-ome2,-2.0*gam]])

# dlt*A の指数関数行列
expdltA = scla.expm(dlt*A)

# Loop
for n in range(N-1):
    # 解析解
    Xtr[n+1,:] = dot(expdltA,Xtr[n,:])
    # Euler法
    Xeu[n+1,:] = Xeu[n,:] + dlt * dot(A,Xeu[n,:])
    # 修正Euler
    K1 = dot(A,Xmo[n,:])
    K2 = dot(A,Xmo[n,:]+0.5*dlt*K1)
    Xmo[n+1,:] = Xmo[n,:] + dlt * K2
    #Heun 法
    K1 = dot(A,Xhe[n,:])
    K2 = dot(A,Xhe[n,:]+dlt*K1)
    Xhe[n+1,:] = Xhe[n,:] + 0.5*dlt*(K1+K2)

# Plot by matplotlib
plot(T,Xeu[:,0])
plot(T,Xmo[:,0])
plot(T,Xhe[:,0])
plot(T,Xtr[:,0])
legend(['Euler','Modified','Heun','Analytical'])
xlabel('Time')
ylabel('x')