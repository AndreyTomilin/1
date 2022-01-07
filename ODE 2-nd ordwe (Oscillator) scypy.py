# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint


#constants
omega = 0.5
beta = 0.2

def D(arg, t):
    y = arg[0]
    y1 = arg[1]
    return [y1, 1/omega**2 * (-y-beta*y1)]

#начальные условия
y0 = [0.7, 0.5]

t = np.linspace(0, 10, 50)

result = odeint(D, y0, t)

plt.subplot(211)
plt.plot(t,result[:,0],t,result[:,1])
plt.subplot(212)
plt.plot(result[:,0],result[:,1])


