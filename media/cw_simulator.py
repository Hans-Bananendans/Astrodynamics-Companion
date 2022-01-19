#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cr3bp_potential.py

@author: Johan Monster
"""

import numpy as np
import matplotlib.pyplot as plt


#%% ===== INPUTS =====

GM_earth = 3.986*10**14
a = (6.378+0.4)*10**6     # [m] 
n = np.sqrt(GM_earth/a**3)

T = 10          # [s] Orbital time
#n = 2*np.pi/T   # [1/s] Orbital period

x0 = 0          # [m] initial x-position
y0 = 0        # [m] initial y-position
z0 = 0          # [m] initial z-position
xdot0 = 0.5       # [m] initial x-velocity
ydot0 = 0.0       # [m] initial y-velocity
zdot0 = 0       # [m] initial z-velocity

fx = 0          # [N] Force in x-direction
fy = 0          # [N] Force in y-direction
fz = 0          # [N] Force in z-direction

dt = 100        # [s] Simulation timestep
tsim = 10**4        # [s] Simulation time


#%% Infrastructure for iteration loop
f0 = [fx, fy, fz]

SV0 = [x0, y0, z0, xdot0, ydot0, zdot0]

def applyCW(SV, f, n, t):
    [x, y, z, xdot, ydot, zdot] = SV
    [fx, fy, fz] = f
    
    snt = np.sin(n*t)
    cnt = np.cos(n*t)
    
    x_out = x*(4-3*cnt) + xdot/n*snt + 2*ydot/n*(1-cnt) \
             - fx/n**2*(1-cnt) + 2*fy/n**2*(n*t-snt)
    y_out = y - ydot/n*(3*n*t-4*snt) - 6*x*(n*t - snt) - 2*xdot/n*(1-cnt) \
             - 2*fx/n**2*(n*t-snt) + 2*fy/n**2*(2-3/4*n**2*t**2 - 2*cnt)
    z_out = z*cnt + zdot/n*snt + fz/n**2*(1-cnt)
    
    xdot_out = 3*x*n*snt + xdot*cnt + 2*ydot*snt \
                + fx/n*snt + 2*fy/n*(1-cnt)
    ydot_out = -ydot*(3-4*cnt) - 6*x*n*(1-cnt) - 2*xdot*snt \
                - 2*fx/n*(1-cnt) - 2*fy/n*(3/2*n*t - 2*snt)
    zdot_out = -z*n*snt + zdot*cnt + fz/n*snt
    
    SV_out = [x_out, y_out, z_out, xdot_out, ydot_out, zdot_out]
    
    return SV_out


#%% Compute output
    
t = np.linspace(0,tsim,int(tsim/dt+1))

SVs = []
x = []
y = []

for tim in t:
    SVs_t = applyCW(SV0, f0, n, tim)
    SVs.append(SVs_t)
    for i, item in enumerate([x, y]):
        item.append(SVs_t[i])
    
    
#%% Plotting code
plt.plot(t,x)
plt.plot(t,y)
plt.plot(y,x)