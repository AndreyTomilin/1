# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

#constants
omega = 0.5
beta = 0.2

def D(y, y1):
    return [y1, 1/omega**2 * (-y-beta*y1)]

t0 = 0
T = 10
N = 200
dt = (T-t0) / N

#рассчетна сетка по времени
t = []
for i in range(N+1):
    t.append(t0+i*dt)

#пустые массивы
y = [0]*(N+1)
y1 = [0]*(N+1)
   
#начальное приближение
y[0], y1[0] = 0.7, 0.5

for i in range(0,N):
    y_r, y1_r = D(y[i], y1[i])
    y[i+1] = y[i] + dt*y_r
    y1[i+1] = y1[i] + dt*y1_r  

plt.subplot(211)
plt.plot(t,y,t,y1)
plt.subplot(212)
plt.plot(y,y1)


