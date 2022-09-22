#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cr3bp_potential.py

@author: Johan Monster
"""

import numpy as np
import matplotlib.pyplot as plt

#%% ===== INPUTS =====

h = 400 # [km] Height of target orbit

x0 = 0          # [m] initial x-position
y0 = -5000      # [m] initial y-position
z0 = 0          # [m] initial z-position
xdot0 = 0       # [m] initial x-velocity
ydot0 = -0.3    # [m] initial y-velocity
zdot0 = 0       # [m] initial z-velocity

fx = 0          # [N] Force in x-direction
fy = 0          # [N] Force in y-direction
fz = 0          # [N] Force in z-direction

dt = 100        # [s] Simulation timestep
tsim = 4.42E3   # [s] Simulation time

# ====================

#%% Constants 
GM_earth = 3.986*10**14

a = (6.378+0.4)*10**6     # [m] Semi-major axis of target orbit
n = np.sqrt(GM_earth/a**3) # [1/s] Orbital period of target

N = int(np.ceil(tsim/dt))+1 # Length of data


#%% Infrastructure for iteration loop

f0 = [fx, fy, fz]   # Constantly applied forces

SV0 = [x0, y0, z0, xdot0, ydot0, zdot0] # State vector at t=0

# Implementation of CW equations to calculate state vector at time t
def applyCW(SV, f, n, t):
    
    # Unpack state vector and force vector
    [x, y, z, xdot, ydot, zdot] = SV
    [fx, fy, fz] = f
    
    # Pre-calculating sinusoidal terms to save time (and space)
    snt = np.sin(n*t)
    cnt = np.cos(n*t)
    
    # Clohessy-Wiltshire equations
    x_out = x*(4-3*cnt) + xdot/n*snt + 2*ydot/n*(1-cnt) \
             - fx/n**2*(1-cnt) + 2*fy/n**2*(n*t-snt)
    y_out = y - ydot/n*(3*n*t-4*snt) - 6*x*(n*t - snt) - 2*xdot/n*(1-cnt) \
             - 2*fx/n**2*(n*t-snt) + 2*fy/n**2*(2-3/4*n**2*t**2 - 2*cnt)
    z_out = z*cnt + zdot/n*snt + fz/n**2*(1-cnt)
    
    # Derivatives of Clohessy-Wiltshire equations
    xdot_out = 3*x*n*snt + xdot*cnt + 2*ydot*snt \
                + fx/n*snt + 2*fy/n*(1-cnt)
    ydot_out = -ydot*(3-4*cnt) - 6*x*n*(1-cnt) - 2*xdot*snt \
                - 2*fx/n*(1-cnt) - 2*fy/n*(3/2*n*t - 2*snt)
    zdot_out = -z*n*snt + zdot*cnt + fz/n*snt
    
    # Assembling output state vector
    SV_out = [x_out, y_out, z_out, xdot_out, ydot_out, zdot_out]
    
    return SV_out


#%% Compute output

# Define time domain
t = np.linspace(0,tsim,int(tsim/dt+1))

# State vector (units: m, m/s)
SVs = []

# Plotting vectors (units: km)
x = []
y = []
z = []

for tim in t:
    SVs_t = applyCW(SV0, f0, n, tim)
    SVs.append(SVs_t)
    for i, item in enumerate([x, y, z]):
        item.append(SVs_t[i]/1000) # Note the conversion to km
    
    
#%% Plotting simple lines for verification
        
#plt.plot(t,x)
#plt.plot(t,y)
#plt.plot(y,x)
        
#%%  ======= More advanced plot ==========
        
# Set up the figure
plt.style.use("dark_background") # SPAAAACE

fig = plt.figure(figsize=(11,8))
ax = fig.add_subplot(projection='3d')

ax.set_title(f"Initial conditions: \n [{x0/1000}, {y0/1000}, {z0/1000}]  km \n   [{xdot0}, {ydot0}, {zdot0}]  m/s ") # The fixed code length people will have a meltdown here.

xscale = 5 # How many km from target to edge of figure in x-direction 
            #   Note: this is the Y-direction in the CW frame (along track)
yscale = 5 # How many km from target to edge of figure in x-direction
            #   Note: this is the Z-direction in the CW frame (cross-track)
zscale = 3 # How many km from target to edge of figure in x-direction
            #   Note: this is the X-direction in the CW frame (altitude)

# Applying this scaling
ax.set_xlim3d(-xscale,xscale)
ax.set_ylim3d(-yscale,yscale)
ax.set_zlim3d(-zscale,zscale)

# Decorating the plot:

# Gray title
ax.title.set_color('#CCCCCC')
                   
# Gray (and translucent) panes
ax.w_xaxis.set_pane_color((0.5, 0.5, 0.5, 0.15)) 
ax.w_yaxis.set_pane_color((0.5, 0.5, 0.5, 0.15))
ax.w_zaxis.set_pane_color((0.5, 0.5, 0.5, 0.15))

# Gray axes labels
ax.xaxis.label.set_color('gray') 
ax.yaxis.label.set_color('gray')
ax.zaxis.label.set_color('gray')

# Gray axes ticks
ax.tick_params(axis='x',colors='gray') 
ax.tick_params(axis='y',colors='gray')
ax.tick_params(axis='z',colors='gray')

# Hide the grid
ax.grid(False)


#%% Plot an "Earth" surface below

Nimg = 5 # Level of detail (lower value = less detail)
ximg, yimg = np.meshgrid(np.linspace(-xscale,xscale,Nimg), 
                         np.linspace(-yscale,yscale,Nimg))
zimg = np.zeros(ximg.shape)

for i in range(zimg.shape[0]):
    for j in range(zimg.shape[1]):
        zimg[i][j] = np.random.rand()

ax.contourf(ximg, yimg, zimg, zdir='z', 
            offset=-zscale-1, 
            cmap=plt.cm.Blues, 
            alpha=0.3
            )


#%% Plot axes quiver
quiveralpha = 0.8 # Set to 0 to hide axes quiver
quiverlength = xscale/4 # Length of the quiver (as function of xscale)

# CW X-axis
ax.quiver(0,0,0,0,0,quiverlength, 
          arrow_length_ratio=0.15, color='red', alpha=quiveralpha)
# CW Y-axis
ax.quiver(0,0,0,quiverlength,0,0, 
          arrow_length_ratio=0.15, color='green', alpha=quiveralpha)
# CW Z-axis
ax.quiver(0,0,0,0,quiverlength,0, 
          arrow_length_ratio=0.15, color='#2E64FE', alpha=quiveralpha)


#%% Plot misc items

# Plot target
ax.scatter(0,0,0, c="#2E64FE", s=36)

# Plot chaser initial
ax.scatter(y[0],z[0],x[0], c="#FF8000", s=24, alpha=0.3)
# Plot chaser final
ax.scatter(y[-1],z[-1],x[-1], c="#FF8000", s=24, alpha=1.0)

# Initial dV vector
dvs = 8 # dV arrow scaling factor
ax.quiver(y[0], z[0], x[0], dvs*ydot0, dvs*zdot0, dvs*xdot0, 
          arrow_length_ratio=0.15, color="#FF8000", alpha=0.8)

# Orbital paths
extend = 1 # Set >1 to make orbital paths extend beyond bounding box
# Orbital path aft
ax.plot([0,-yscale*extend], [0,0], [0,0], c="#2E64FE", dashes=[1,1], alpha=0.7)
# Orbital path ahead
ax.plot([0, yscale*extend], [0,0], [0,0], c="#2E64FE", dashes=[1,5], alpha=0.3)


#%% Plot chaser path based on Clohessy-Wiltshire equations
for i in range(1,N):
    ax.plot(y[i-1:i+1], z[i-1:i+1], x[i-1:i+1], 
            c="#FF8000",                # Orange colour
            alpha=(0.1+0.9*(i/N)**3))   # Cubic line fade

plt.show()
