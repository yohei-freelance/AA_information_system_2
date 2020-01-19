# 減衰振動の状微分方程式の数値解法
# 以下の方法を比較
# (1) Euler 法 (1次近似)
# (2) 4次のRunge-Kutta 法 (4次近似)
# (3) 解析解から得られる漸化式による方法

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
Xrk = zeros((N,2)) #Runge-Kutta法用
Xtr = zeros((N,2)) #解析解用

# 初期状態
Xtr[0,:] = Xrk[0,:] =Xeu[0,:] =[1.0, 1.0]

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
    # 4次 Runge-Kutta
    K1 = dot(A,Xrk[n,:])
    K2 = dot(A,Xrk[n,:]+0.5*dlt*K1)
    K3 = dot(A,Xrk[n,:]+0.5*dlt*K2)
    K4 = dot(A,Xrk[n,:]+dlt*K3)
    Xrk[n+1,:] = Xrk[n,:] + dlt/6*(K1+2*K2+2*K3+K4)

# Plot by matplotlib
plot(T,Xeu[:,0])
plot(T,Xrk[:,0])
plot(T,Xtr[:,0])
legend(['Euler','Runge-Kutta','Analytical'])
xlabel('Time')
ylabel('x')