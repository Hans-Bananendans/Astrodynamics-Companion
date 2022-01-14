#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cr3bp_potential.py

@author: Johan Monster
"""

import numpy as np
import matplotlib.pyplot as plt

plot_gravitational_potential_U1 = True
plot_gravitational_potential_U2 = True
plot_centrifugal_potential = True

mu = 0.2 # You can set 0 < mu < 0.5

X, Y = np.mgrid[-2.5:2.5:64j, -2.5:2.5:64j]
Z = 0
U = np.zeros([len(X),len(Y)])
r1 = np.sqrt(  (mu+X)**2 + Y**2 + Z**2)
r2 = np.sqrt((1-mu-X)**2 + Y**2 + Z**2)

if plot_gravitational_potential_U1:
    U += (1-mu)/r1

if plot_gravitational_potential_U2:
    U += mu/r2

if plot_centrifugal_potential:
    U += 0.5*(X**2 + Y**2)

fig = plt.figure(figsize=(7,8))
ax = fig.add_subplot(111, projection="3d")
ax.set_zlim3d(-10,10)
ax.plot_surface(X, Y, U, cmap="gnuplot", linewidth=1, rstride=4, cstride=4, alpha=0.7)
ax.plot_wireframe(X, Y, U, color='k', linewidth=1, rstride=4, linestyle="solid", cstride=4, alpha=0.9)
ax.contour(X, Y, U, 64, linewidths=1, colors="k", linestyles="solid",alpha=0.7)

ax.contour(X, Y, U, 64, linewidths=1, cmap="gnuplot", linestyles="solid", offset=-10)
plt.show()