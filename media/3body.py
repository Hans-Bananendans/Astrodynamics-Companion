"""
A simple 2D 3-body problem propagator that can make static plots and 
animations. Used 

Created on Wed Sep  1 13:54:24 2021

@author: Johan Monster
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#%% Configuration
G = 1

# Time span
t0 = 0.0        # [s]
tend = 100.0    # [s]
tspan = [t0, tend]
steps = 10000

# Animation
frametime = 25  # [ms] Time that each frame is displayed for
scale = 0.1

# Masses
m1 = 1.0
m2 = 1.0
m3 = 1.0

# Initial positions and velocities
#       x_init  y_init  vx_init  vy_init
Yi1 = [   1.0,   -1.0,     0.0,      0.1]
Yi2 = [   1.0,    3.0,     0.0,      0.0]
Yi3 = [  -2.0,   -1.0,     0.0,      0.0]

# Figure 8: x_init       y_init       vx_init       vy_init
# Yi1 = [-0.97000436,  0.24308753, 0.4662036850, 0.4323657300]
# Yi2 = [        0.0,         0.0,  -0.93240737,  -0.86473146]
# Yi3 = [ 0.97000436, -0.24308753, 0.4662036850, 0.4323657300]

# # Lagrange Triangle
# Yi1 = [ 1,  3, 0, 0]
# Yi2 = [-2, -1, 0, 0]
# Yi3 = [ 1, -1, 0, 0]


#%% Computation
Yi = [Yi1[0], Yi1[1], 
      Yi2[0], Yi2[1], 
      Yi3[0], Yi3[1],
      Yi1[2], Yi1[3], 
      Yi2[2], Yi2[3], 
      Yi3[2], Yi3[3]]

m = [m1, m2, m3]

def f(t, Y, m, G=1):
    
    dYdt = [0]*12
    
    m1, m2, m3 = m
    
    x1, y1 = Y[0], Y[1]
    x2, y2 = Y[2], Y[3]
    x3, y3 = Y[4], Y[5]
    
    r12 = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    r13 = np.sqrt((x3-x1)**2 + (y3-y1)**2)
    r23 = np.sqrt((x3-x2)**2 + (y3-y2)**2)
    
    dYdt[0:6] = Y[6:12]
    dYdt[6]  = G*(m2*(x2-x1)/r12**3 + m3*(x3-x1)/r13**3)
    dYdt[7]  = G*(m2*(y2-y1)/r12**3 + m3*(y3-y1)/r13**3)
    dYdt[8]  = G*(m1*(x1-x2)/r12**3 + m3*(x3-x2)/r23**3)
    dYdt[9]  = G*(m1*(y1-y2)/r12**3 + m3*(y3-y2)/r23**3)
    dYdt[10] = G*(m1*(x1-x3)/r13**3 + m2*(x2-x3)/r23**3)
    dYdt[11] = G*(m1*(y1-y3)/r13**3 + m2*(y2-y3)/r23**3)

    return dYdt

# sol = solve_ivp(f, t_span=tspan, y0=Yi, t_eval=np.linspace(t0,tend,steps), args=(m,G,), method="RK45")
sol = solve_ivp(f, t_span=tspan, y0=Yi, t_eval=np.linspace(t0,tend,steps), args=(m,G,), method='DOP853')

tsol = sol.t
Ysol = sol.y

#%% Compute Centre of Mass of body system as a check
#    (point should have constant or zero velocity)
tsol2 = tsol[0:len(tsol):10]
Ysol2 = Ysol[:,0:len(Ysol[0,:]):10]


xcom = []
ycom = []
for i in range(len(Ysol2[0,:])):
    xcom.append((Ysol2[0,i]*m1 + Ysol2[2,i]*m2 + Ysol2[4,i]*m3) / (m1+m2+m3))
    ycom.append((Ysol2[1,i]*m1 + Ysol2[3,i]*m2 + Ysol2[5,i]*m3) / (m1+m2+m3))

com = np.array([xcom, ycom])


#%% Plotting

def makeplot(t, Y):
    # Static plot
    
    fig, ax = plt.subplots()
    ax.set_xlim(-100,100)
    ax.set_ylim(-100,100)
    ax.set_facecolor("black")
    ax.grid(True, alpha=0.2)
    ax.set_aspect('equal')
    
    fig.set_facecolor("black")
    
    line1, = ax.plot(Y[0,:], Y[1,:], dashes=[6,2], label='Body 1')
    line2, = ax.plot(Y[2,:], Y[3,:], dashes=[6,2], label='Body 2')
    line3, = ax.plot(Y[4,:], Y[5,:], dashes=[6,2], label='Body 3')
    # line1, = ax.plot(x, y, dashes=[6,2], label='Body 1')
    
    ax.legend()
    plt.show()


def makeplot2(t, Y, com, frametime=50, scale=1):
    # Animated plot
    
    steps = len(Y[0,:])
    
    fig, ax = plt.subplots(figsize=(8,8), dpi=100)
    ax.set_xlim(-100*scale,100*scale)
    ax.set_ylim(-100*scale,100*scale)
    ax.set_facecolor("black")
    ax.grid(True, alpha=0.2)
    ax.set_aspect('equal')
    # ax.get_yaxis().set_visible(False)
    
    fig.set_facecolor("black")
    
    dotcom, = ax.plot([], [], color='#AAAAAA', marker='x', markersize=10, linestyle='')
    
    dot1, =  ax.plot([], [], color='cyan', marker='o', markersize=10, linestyle='')
    dot2, =  ax.plot([], [], color='magenta', marker='o', markersize=10, linestyle='')
    dot3, =  ax.plot([], [], color='yellow', marker='o', markersize=10, linestyle='')
    
    line1, = ax.plot([], [], color='cyan', linewidth=1, label='Body 1', alpha=0.25)
    line2, = ax.plot([], [], color='magenta', linewidth=1, label='Body 2', alpha=0.25)
    line3, = ax.plot([], [], color='yellow', linewidth=1, label='Body 3', alpha=0.25)
    
    lx1, ly1 = [], []
    lx2, ly2 = [], []
    lx3, ly3 = [], []
    
    # line2, = ax.plot(y[2,:], y[3,:], dashes=[6,2], label='Body 2')
    # line3, = ax.plot(y[4,:], y[5,:], dashes=[6,2], label='Body 3')

    def init():
        dotcom.set_data(com[0,0], com[1,0])
        
        dot1.set_data(Y[0,0], Y[1,0])
        dot2.set_data(Y[2,0], Y[3,0])
        dot3.set_data(Y[4,0], Y[5,0])
        
        line1.set_data(Y[0,0], Y[1,0])
        line2.set_data(Y[2,0], Y[3,0])
        line3.set_data(Y[4,0], Y[5,0])
        
        return dotcom,dot1,dot2,dot3,line1,line2,line3
    
    def update(i):
        dotcom.set_data(com[0,i], com[1,i])
        
        dot1.set_data(Y[0,i], Y[1,i])
        dot2.set_data(Y[2,i], Y[3,i])
        dot3.set_data(Y[4,i], Y[5,i])
        
        lx1.append(Y[0,i])
        ly1.append(Y[1,i])
        line1.set_data(lx1, ly1)
        lx2.append(Y[2,i])
        ly2.append(Y[3,i])
        line2.set_data(lx2, ly2)
        lx3.append(Y[4,i])
        ly3.append(Y[5,i])
        line3.set_data(lx3, ly3)
        
        return dotcom,dot1,dot2,dot3,line1,line2,line3

    ani = animation.FuncAnimation(fig=fig, func=update, frames=steps, 
                                  init_func=init, interval=frametime,
                                  blit=True, repeat=False)
    
    ax.legend()
    plt.show()
    return ani
        

ani = makeplot2(tsol2,Ysol2,com,frametime=frametime, scale=scale)