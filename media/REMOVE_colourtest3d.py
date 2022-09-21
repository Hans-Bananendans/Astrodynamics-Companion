#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:58:41 2022

@author: johan
"""

import numpy as np
import matplotlib.pyplot as plt

xdot0 = 0.5
ydot0 = 0
zdot0 = 0

N = 20 # number of points
x = np.arange(-N/2-1, N/2, dtype=float) # x,y,z = 1d arrays
y = 1 * x
z = 2*np.ones(len(x))


#%% Set up the figure
fig = plt.figure(figsize=(11,7))
ax = fig.add_subplot(projection='3d')

xscale = 20
yscale = 20
zscale = 15

ax.set_xlim3d(-xscale,xscale)
ax.set_ylim3d(-yscale,yscale)
ax.set_zlim3d(-zscale+1,zscale)
ax.invert_xaxis

#
ax.scatter(0,0,0, c="#0000FF", s=36)

#%% Plot a shitty "Earth" surface below
Nimg = 4
ximg, yimg = np.meshgrid(np.linspace(-xscale,xscale,Nimg), np.linspace(-yscale,yscale,Nimg))
zimg = np.ones(ximg.shape)
dimg= 0*zimg

for i in range(zimg.shape[0]):
    for j in range(zimg.shape[1]):
        dimg[i][j] = np.random.rand()

ax.contourf(ximg, yimg, dimg, zdir='z', offset=-16, cmap=plt.cm.Blues, alpha=0.3)


#%% plot axes quiver
quiveralpha = 1
quiverlength = xscale/4

# CW X-axis
ax.quiver(0,0,0,0,0,quiverlength, 
          arrow_length_ratio=0.15, color='red', alpha=quiveralpha)
# CW Y-axis (pointing "left" instead of "right"!)
ax.quiver(0,0,0,-quiverlength,0,0, 
          arrow_length_ratio=0.15, color='green', alpha=quiveralpha)
# CW Z-axis
ax.quiver(0,0,0,0,quiverlength,0, 
          arrow_length_ratio=0.15, color='blue', alpha=quiveralpha)

#%% Plot misc items

# Plot target
ax.scatter(0,0,0, c="#0000FF", s=36)

# Plot chaser initial
ax.scatter(y[0],z[0],x[0], c="#FF0000", s=24, alpha=0.3)
# Plot chaser final
ax.scatter(y[-1],z[-1],x[-1], c="#FF0000", s=24, alpha=1.0)

# Plot initial thrust vector
tvs = 10 # thrust vector scaling factor
ax.quiver(y[0], z[0], x[0], tvs*ydot0, tvs*zdot0, tvs*xdot0, 
          arrow_length_ratio=0.15, color='black', alpha=0.5)
           
ax.plot([0,yscale], [0,0], [0,0], c="blue", dashes=[1,1], alpha=0.6)
ax.plot([0,-yscale], [0,0], [0,0], c="blue", dashes=[1,5], alpha=0.2)

# you have to plot segments, its means your arguments
# have to be a slice of arrays like here: from x(i-1) to x(i) => x[i-1:i+1]
# to get color from colormap use index: 0 <= i <= 1
for i in range(1,N):
    ax.plot(y[i-1:i+1], z[i-1:i+1], x[i-1:i+1], c = plt.cm.Reds(1. * i / N), alpha=(1.*i/N))
    

plt.show()

