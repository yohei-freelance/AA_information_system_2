from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

s = 10.0
b = 8.0/3.0
r = 28.0

# Compute the derivative of state vector
def deriv_lorenz(x):
    dx = s*(x[1]-x[0])
    dy = x[0]*(r-x[2])-x[1]
    dz = x[0]*x[1]-b*x[2]
    dxdydz = array([dx,dy,dz])
    return dxdydz

# Time step
dt = 0.01
# List of time points
T = arange(0.0,100.0,dt)
# Number of time steps
numt = T.shape[0]
# Array for state history
X = zeros((numt,3))
# Initial state
X[0,:] = array([10.0, -10.0, 20.0])

for i in range(numt-1):
    k1 = deriv_lorenz(X[i,:])
    k2 = deriv_lorenz(X[i,:]+0.5*dt*k1)
    k3 = deriv_lorenz(X[i,:]+0.5*dt*k2)
    k4 = deriv_lorenz(X[i,:]+dt*k3)
    X[i+1,:] = X[i,:] + dt/6 * (k1+2*k2+2*k3+k4)
    #X[i+1,:] = X[i,:] + dt * k1

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X[:,0], X[:,1], X[:,2])

plt.show()
