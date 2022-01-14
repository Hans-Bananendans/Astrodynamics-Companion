# Tutorial: Programming a simple 3-body problem solver

In this tutorial, we will make a simple implementation of a 2D 3-body solver/propagator. This implementation will be done in [Python](https://www.python.org), but similar implementations can be easily made in other languages such as C/C++, Matlab, Java, Rust, Lua, or Julia.

```ad-warning
title: Warning!

When you are first learning about Astrodynamics, trying to implement this software by yourself is a really good exercise for your own development. Before you read this tutorial, I would personally recommend that you look at the mathematical description of the problem and try to make your own implementation. If after a few hours, you are still stuck, this tutorial is a good resource to help you along. 

But who am I kidding, [you're an adult](../media/adult.gif), you can do whatever you want, right?

```

___
## Index
1. [[Programming a simple 3-body problem solver#Mathematical description|Mathematical description]]
2. [[Programming a simple 3-body problem solver#State-space description|State-space description]]
3. [[Programming a simple 3-body problem solver#Python implementation|Python implementation]]
	1. [[Programming a simple 3-body problem solver#Step 1 Importing dependencies|Step 1: Importing dependencies]]
	2. [[Programming a simple 3-body problem solver#Step 2 Specifying initial conditions|Step 2: Specifying initial conditions]]
	3. [[Programming a simple 3-body problem solver#Step 3 Defining the mapping function bar f|Step 3: Defining the mapping function f]]
	4. [[Programming a simple 3-body problem solver#Step 4 Defining the state vector bar Y|Step 4: Defining the state vector Y]]
	5. [[Programming a simple 3-body problem solver#Step 5 Calling solve_ivp|Step 5: Calling solve_ivp()]]
	6. [[Programming a simple 3-body problem solver#Step 6 Plotting the results|Step 6: Plotting the results]]
	7. [[Programming a simple 3-body problem solver#Step 7 Plotting the results like a chad|Step 7: Plotting the results like a chad]]
	8. [[Programming a simple 3-body problem solver#Step 8 Plotting the barycentre|Step 8: Plotting the barycentre]]
	9. [[Programming a simple 3-body problem solver#Step 9 Fun stuff|Step 9: Fun stuff]]
4. [[Programming a simple 3-body problem solver#Complete code|Complete code]]

___
## Mathematical description
In the figure below, you can see a generic diagram that describes the various variables involved in a 3-body problem. We have three masses $m_1$, $m_2$, and $m_3$ and an inertial reference frame $XYZ$. Each mass is at a distance from the origin ($\bar{r}_1$, $\bar{r}_2$, and $\bar{r}_3$), and moves at a certain velocity with respect to the origin ($\dot{\bar{r}}_1$, $\dot{\bar{r}}_2$, and $\dot{\bar{r}}_3$). 
![[tut3body1.png]]

On the right side of the figure, you can see the relative positions that the three masses have with respect to one another ($\bar{r}_{12}$, $\bar{r}_{23}$, and $\bar{r}_{13}$). You can see that each mass experiences a gravitational force from each of the other masses (note: vectors are not to scale!).

For the 3-body problem, you generally have to solve $3 \cdot 3 = 9$ second-order differential equations: You have 3 masses, and they operate in 3D, so their positions will have three coordinates. If you instead were to move the problem to 2D, you are left with only 6 second-order differential equations. **In this tutorial, we will focus on the 2D case**. The reason for doing so is that it makes plots/animations that are easier for you to understand and visualize, which is the primary goal of this tutorial. The underlying principles and mathematics remain the same. 

So the 2D 3-body problem that we will be addressing looks like this:

![[tut3body2.png]]

For every single one of the masses in the figure, we can apply [[Newtonian Mechanics#Newton's second law|Newton's second law]], to arrive at:
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \tag{w2.3}$$


```ad-note
title: Full mathematical description for all particles
icon: paperclip
collapse: open
color: 180,180,180

To understand this a bit better, we can write this out for all three particles:

$$m_1 \dfrac{d^2 \bar{r}_1}{dt^2} = G \dfrac{m_1 m_2}{r^3_{12}} \bar{r}_{12} + G \dfrac{m_1 m_3}{r^3_{13}} \bar{r}_{13}$$

$$m_2 \dfrac{d^2 \bar{r}_2}{dt^2} = G \dfrac{m_2 m_1}{r^3_{21}} \bar{r}_{21} + G \dfrac{m_2 m_3}{r^3_{23}} \bar{r}_{23}$$

$$m_3 \dfrac{d^2 \bar{r}_3}{dt^2} = G \dfrac{m_3 m_1}{r^3_{31}} \bar{r}_{31} + G \dfrac{m_3 m_2}{r^3_{32}} \bar{r}_{32}$$

Also remember that
$$\bar{r}_{12} = \bar{r}_{2} - \bar{r}_{1} = -\bar{r}_{21}$$
$$\bar{r}_{13} = \bar{r}_{3} - \bar{r}_{1} = -\bar{r}_{31}$$
$$\bar{r}_{23} = \bar{r}_{3} - \bar{r}_{2} = -\bar{r}_{32}$$

```

___
## State-space description
To solve this, we are going to have to convince our computer to solve some second-order differential equations for us. The standard approach to do this is to rewrite the problem to a state-space description, which features only first-order differential equations:
$$\dfrac{d\bar{Y}}{dt} = \bar{f} \left(t, \bar{Y}\right)$$
We can do this if we note that a particle's acceleration is the derivative of the its velocity, and a particle's velocity is the derivative of its position. Instead of having to solve 6 second-order differential equations, we then have to solve 12 first-order equations, which is easier to do in code. As a result, we want to choose a state vector that includes the position and velocity of each particle, so that the derivative of the state vector contains the acceleration and the velocity of each particle:

$$\bar{Y} = 
\begin{bmatrix}
x_{1} \\ y_{1} \\
x_{2} \\ y_{2} \\
x_{3} \\ y_{3} \\
\dot{x}_{1} \\ \dot{y}_{1} \\
\dot{x}_{2} \\ \dot{y}_{2} \\
\dot{x}_{3} \\ \dot{y}_{3}
\end{bmatrix}
 =
\begin{bmatrix}
r_{x,1} \\ r_{y,1} \\
r_{x,2} \\ r_{y,2} \\
r_{x,3} \\ r_{y,3} \\
v_{x,1} \\ v_{y,1} \\
v_{x,2} \\ v_{y,2} \\
v_{x,3} \\ v_{y,3} 
\end{bmatrix}

\quad\quad ; \quad\quad

\dfrac{d\bar{Y}}{dt} = 
\dfrac{d}{dt} \left( \begin{bmatrix}
x_{1} \\ y_{1} \\
x_{2} \\ y_{2} \\
x_{3} \\ y_{3} \\
\dot{x}_{1} \\ \dot{y}_{1} \\
\dot{x}_{2} \\ \dot{y}_{2} \\
\dot{x}_{3} \\ \dot{y}_{3}
\end{bmatrix}\right)
= 
\begin{bmatrix}
\dot{x}_{1} \\ \dot{y}_{1} \\
\dot{x}_{2} \\ \dot{y}_{2} \\
\dot{x}_{3} \\ \dot{y}_{3}\\
\ddot{x}_{1} \\ \ddot{y}_{1} \\
\ddot{x}_{2} \\ \ddot{y}_{2} \\
\ddot{x}_{3} \\ \ddot{y}_{3}
\end{bmatrix}
 =
\begin{bmatrix}
v_{x,1} \\ v_{y,1} \\
v_{x,2} \\ v_{y,2} \\
v_{x,3} \\ v_{y,3} \\
a_{x,1} \\ a_{y,1} \\
a_{x,2} \\ a_{y,2} \\
a_{x,3} \\ a_{y,3} 
\end{bmatrix}
$$

If we look at the top six entries of the derivative of the state vector $d\bar{Y}/dt$, we see that they are the velocities of the particles, which are already present in the state vector itself. So that's fairly easy to implement:

$$\dfrac{d\bar{Y}}{dt}[1:6] = \bar{Y}[7:12]$$

Any mathematicians laying their eyes on this cursed formulation will probably cringe in abject horror, but I think it is clear what I mean: We can literally map the second half of the state vector onto the first half of the derivative of the state vector, because they are the same.

As for the accelerations, this is where we use equation $\text{w2.3}$ from above. We first rewrite it so that it only solves for the acceleration, by dividing both sides by the particle's mass:

$$\dfrac{d^2 \bar{r}_i}{dt^2} = \dfrac{1}{m_i}\sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} = \sum_{j \neq i} G \dfrac{m_j}{r^3_{ij}} \bar{r}_{ij}$$

So applying this to all the values in the second half of $d\bar{Y}/dt$, we can write down expressions for all of them (warning: more cursed use of math):
$$\dfrac{d\bar{Y}}{dt}[7:12] = 
\begin{bmatrix}
\ddot{x}_{1} \\ \ddot{y}_{1} \\
\ddot{x}_{2} \\ \ddot{y}_{2} \\
\ddot{x}_{3} \\ \ddot{y}_{3}
\end{bmatrix}
= 
\begin{bmatrix}
G \dfrac{m_2}{r^3_{12}}(x_2-x_1) + G \dfrac{m_3}{r^3_{13}}(x_3-x_1)\\ G \dfrac{m_2}{r^3_{12}}(y_2-y_1) + G \dfrac{m_3}{r^3_{13}}(y_3-y_1)\\
G \dfrac{m_1}{r^3_{12}}(x_1-x_2) + G \dfrac{m_3}{r^3_{32}}(x_3-x_2)\\
G \dfrac{m_1}{r^3_{12}}(x_1-x_2) + G \dfrac{m_3}{r^3_{32}}(x_3-x_2)\\
G \dfrac{m_1}{r^3_{13}}(x_1-x_3) + G \dfrac{m_2}{r^3_{23}}(x_2-x_3)\\
G \dfrac{m_1}{r^3_{13}}(x_1-x_3) + G \dfrac{m_2}{r^3_{23}}(x_2-x_3)
\end{bmatrix}
$$

This, together with the previous expressions, give us a complete description of how to find the derivative of the state vector $\bar{Y}$.

```ad-tip
title: Tip
icon: lightbulb

I recommend pausing here and trying to see if you can derive this last expression for yourself. It requires paying close attention to the direction in which each vector points, and managing your minus signs carefully.

Consult the earlier figure of the 2D case, and remember that the following relations apply:
$$\bar{r}_{12} = \bar{r}_{2} - \bar{r}_{1} = -\bar{r}_{21}$$
$$\bar{r}_{13} = \bar{r}_{3} - \bar{r}_{1} = -\bar{r}_{31}$$
$$\bar{r}_{23} = \bar{r}_{3} - \bar{r}_{2} = -\bar{r}_{32}$$

$$ r_{12} = r_{21} = |\bar{r}_{12}| = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2} $$
$$ r_{13} = r_{31} = |\bar{r}_{13}| = \sqrt{(x_3-x_1)^2 + (y_3-y_1)^2} $$
$$ r_{23} = r_{32} = |\bar{r}_{23}| = \sqrt{(x_3-x_2)^2 + (y_3-y_2)^2} $$
```

___
## Solving the state-space system
To solve this state-space system, we will use the function `solve_ivp()` from the Python library SciPy. If you're using Matlab, you can use analogous methods like `ode45()` to do solve the state-space system. 

The function `solve_ivp()` takes the function $\bar{f}$ that maps $\bar{Y}$ to $d\bar{Y}/dt$. It also takes the variable along which the propagation occurs (which for us is time), some initial conditions, and some other stuff like timestep. One nice thing about `solve_ivp()` is that it allows you to select a variety of built-in integration methods, such as your bog-standard Runge-Kutta methods (`RK23`, `RK45`, and `DOP853`), as well as more advanced schemes (such as `BDF`). For a full list, refer to the [SciPy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).

___
## Python implementation
We now begin the description of the Python implemenation. This will be done in separate steps. If you are just intested in viewing all the code at once, look [[3body_py|here]] instead.

___
### Step 1: Importing dependencies
Import the packages that you need. We will use:
- NumPy
- SciPy
- Matplotlib

We will do some animation [[Programming a simple 3-body problem solver#Step 7 Plotting the results like a chad|later on]], so we will also import the animation module of Matplotlib.
````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```
````

___
### Step 2: Specifying initial conditions
There are a number of constants and initial conditions that we will want to define.

For our universal gravitational constant $G$, we can actually choose anything we like. We can use the value that you would use for calculations in our universe, but remember that in this case, it is just a scaling factor for the forces. Since we can choose anything we like here, we will just set it to $1$. For the other quantities like mass, position, and velocity, we choose non-dimensional parameters. 

If this seems a little bit strange to you, feel free to use real units, like meters and kilograms. It does not really matter for the mathematics, although it may make the motion a little slow. Just make sure that you use your units consistently if you're going to do so.

````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
G = 1

# Masses
m1 = 1.0
m2 = 1.0
m3 = 1.0
m = [m1, m2, m3]

# Initial positions and velocities
#       x_init  y_init  vx_init  vy_init
Yi1 = [   1.0,   -1.0,     0.0,      0.1]
Yi2 = [   1.0,    3.0,     0.0,      0.0]
Yi3 = [  -2.0,   -1.0,     0.0,      0.0]
```
````

___
### Step 3: Defining the mapping function $\bar{f}$
Now we want to implement the function $\bar{f}$ that maps $\bar{Y}$ to $d\bar{Y}/dt$. We have already seen a full mathematical description of this, so it is just a matter of putting it into code. Note that we need to feed our implementation of $\bar{f}$ to our integrator function `solve_ivp()` as a Python function, so that it is why it is in a function called `f()`.

````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
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
```
````

```ad-note
title: For reference: Mathematical description
icon: paperclip
collapse: close
color: 180,180,180

$$\dfrac{d\bar{Y}}{dt} = \bar{f} \left(t, \bar{Y}\right)$$

$$\dfrac{d\bar{Y}}{dt}[1:6] = \bar{Y}[7:12]$$

$$\dfrac{d\bar{Y}}{dt}[7:12] = 
\begin{bmatrix}
\ddot{x}_{1} \\ \ddot{y}_{1} \\
\ddot{x}_{2} \\ \ddot{y}_{2} \\
\ddot{x}_{3} \\ \ddot{y}_{3}
\end{bmatrix}
= 
\begin{bmatrix}
G \dfrac{m_2}{r^3_{12}}(x_2-x_1) + G \dfrac{m_3}{r^3_{13}}(x_3-x_1)\\ G \dfrac{m_2}{r^3_{12}}(y_2-y_1) + G \dfrac{m_3}{r^3_{13}}(y_3-y_1)\\
G \dfrac{m_1}{r^3_{12}}(x_1-x_2) + G \dfrac{m_3}{r^3_{32}}(x_3-x_2)\\
G \dfrac{m_1}{r^3_{12}}(x_1-x_2) + G \dfrac{m_3}{r^3_{32}}(x_3-x_2)\\
G \dfrac{m_1}{r^3_{13}}(x_1-x_3) + G \dfrac{m_2}{r^3_{23}}(x_2-x_3)\\
G \dfrac{m_1}{r^3_{13}}(x_1-x_3) + G \dfrac{m_2}{r^3_{23}}(x_2-x_3)
\end{bmatrix}
$$

```

If you compare it to the mathematical description, this should not look too surprising. 
1. The first argument of function `f()` **must be** `t`, the variable along which `solve_ivp()` will propagate. Even though we will not use `t` directly in the function, this simply has to do with how `solve_ivp()` works internally. The other arguments are the state vector `Y`, for obvious reasons, and four constants: the three masses (which we've shoved into a list called `m`) and the gravitational constant `G`. 
2. First, we make a zero Python list called `dYdt` that we're going to fill up with the correct values.
3. We then unpack `m`, which is just a list with the three masses. 
4. Then we simply extract the first six values from the state vector, which correspond to the (x,y) positions of the three masses.
5. Now we calculate the relative distance between the three masses, because we will need that in a moment. Pythagoras smiles upon you.
6. Then we map the last six values of our state vector `Y` (the velocities) onto the first six values of the derivative of the state vector `dYdt`.
7. Finally we calculate the bottom half of `dYdt`, which looks almost exactly like the mathematical description. Do note that Python indexing starts at 0, not at 1, so our state vector `Y` goes from index 0 to 11.
8. Then we return the derivative of the state vector `dYdt`. This is also required to make `solve_ivp()` work correctly.

___
### Step 4: Defining the state vector  $\bar{Y}$	  
````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
Yi = [Yi1[0], Yi1[1], 
      Yi2[0], Yi2[1], 
      Yi3[0], Yi3[1],
      Yi1[2], Yi1[3], 
      Yi2[2], Yi2[3], 
      Yi3[2], Yi3[3]]
```
````
We added the subscript `i` here to denote that this is the state vector at any time, or for any timestep $i$.

___
### Step 5: Calling `solve_ivp()`
Now it is time to use the solver to propagate our system description. First we define how long the simulation should go on for, and how many steps it should include. If you instead wish to define a fixed timestep, you can also define that, and calculate the number of steps by dividing the simulation timespan by the desired timestep.

Then we call the `solve_ivp()` function, and input the arguments. Refer to the [SciPy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) for details on how to do this correctly. We decide to use the 8th order Runge-Kutta method `DOP853` as our integration method. 

After it has done its thing, we save the outputs as `tsol` and `Ysol`. If you're using a Python interpreter like Spyder, these will appear in your variable explorer, so you can inspect them. `tsol` is a 1-by-10000 Numpy array, whilst `Ysol` is a 12-by-10000 Numpy array. 

````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
# Time span
t0 = 0.0        # [s]
tend = 100.0    # [s]
tspan = [t0, tend]
steps = 10000

sol = solve_ivp(f, 
				t_span=tspan, 
				y0=Yi, 
				t_eval=np.linspace(t0,tend,steps), 
				args=(m,G,), 
				method='DOP853'
				)
tsol = sol.t
Ysol = sol.y
```
````

___
### Step 6: Plotting the results
Now we wish to plot the results. This is done in Matplotlib in a fairly standard way. The code details will not be explained here, but where needed you can refer to the excellent online [Matplotlib documentation](https://matplotlib.org/).
````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
def makeplot(t, Y, scale=1):
    # Static plot
    
    fig, ax = plt.subplots()
    ax.set_xlim(-scale*100,scale*100)
    ax.set_ylim(-scale*100,scale*100)
    ax.set_facecolor("black")
    ax.grid(True, alpha=0.2)
    ax.set_aspect('equal')
    
    fig.set_facecolor("black")
    
    line1, = ax.plot(Y[0,:], Y[1,:], dashes=[6,2], label='Body 1')
    line2, = ax.plot(Y[2,:], Y[3,:], dashes=[6,2], label='Body 2')
    line3, = ax.plot(Y[4,:], Y[5,:], dashes=[6,2], label='Body 3')
    
    ax.legend()
    plt.show()
```
````

This function can be called like so:

````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
makeplot(tsol, Ysol, scale=0.1)
```
````

It should return a plot with something along the lines of:
![[makeplot.png]]
If you were to attach a marker to each body, and then let them fly under their gravity, these are the lines they will make. Now you can go ahead and play with the initial conditions, and see how the outcome changes. You can really see the effect of the [[Newtonian Mechanics#Chaotic motion|chaotic]] nature of the 3-body problem: for small changes in initial condition, the plots will often look wildly different, especially if you run the simulation for a long time.

___
### Step 7: Plotting the results like a chad
However, there are limitations to the current plots. For example, we cannot really get a sense of the velocities involved, or the direction of the motion. So to improve our code, we can turn it into an animation so we can visualize those details a bit better.

````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
def makeplot2(t, Y, frametime=50, scale=1):
    # Animated plot
    
    steps = len(Y[0,:])
    
    fig, ax = plt.subplots(figsize=(8,8), dpi=100)
    ax.set_xlim(-100*scale,100*scale)
    ax.set_ylim(-100*scale,100*scale)
    ax.set_facecolor("black")
    ax.grid(True, alpha=0.2)
    ax.set_aspect('equal')
#    ax.get_xaxis().set_visible(False) # Hide the grids, if you want
#    ax.get_yaxis().set_visible(False) # Hide the grids, if you want
    
    fig.set_facecolor("black")
    
    
    dot1, =  ax.plot([], [], color='cyan', marker='o', 
					  markersize=10, linestyle='')
    dot2, =  ax.plot([], [], color='magenta', marker='o', 
		              markersize=10, linestyle='')
    dot3, =  ax.plot([], [], color='yellow', marker='o', 
					  markersize=10, linestyle='')
    
    line1, = ax.plot([], [], color='cyan', linewidth=1, 
		             label='Body 1', alpha=0.25)
    line2, = ax.plot([], [], color='magenta', linewidth=1, 
					 label='Body 2', alpha=0.25)
    line3, = ax.plot([], [], color='yellow', linewidth=1, 
					 label='Body 3', alpha=0.25)
    
    lx1, ly1 = [], []
    lx2, ly2 = [], []
    lx3, ly3 = [], []
    

    def init():        
        dot1.set_data(Y[0,0], Y[1,0])
        dot2.set_data(Y[2,0], Y[3,0])
        dot3.set_data(Y[4,0], Y[5,0])
        
        line1.set_data(Y[0,0], Y[1,0])
        line2.set_data(Y[2,0], Y[3,0])
        line3.set_data(Y[4,0], Y[5,0])
        
        return dot1,dot2,dot3,line1,line2,line3
    
    def update(i):        
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
        
        return dot1,dot2,dot3,line1,line2,line3

    ani = animation.FuncAnimation(fig=fig, func=update, frames=steps, 
                                  init_func=init, interval=frametime,
                                  blit=True, repeat=False)
    
    ax.legend()
    plt.show()
    return ani
```
````

We can run this code by calling:
````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
# Animation
frametime = 25  # [ms] Time that each frame is displayed for
scale = 0.1

ani = makeplot2(tsol2,Ysol2,frametime=frametime, scale=scale)
```
````

This should return a nice animation on which you can much better observe the motion that the masses make.

![[makeplot2.png]]

```ad-tip
title: Tip
icon: lightbulb

If you are using Spyder, and you are having trouble getting the animation to render correctly, try changing the graphics backend that Spyder uses. In the _Tools_ tab, go to _Preferences_ -> _IPython console_ -> _Graphics_ -> _Graphics backend_ and change the backend from inline/automatic to Qt4/Qt5.

```

___
### Step 8: Plotting the barycentre
A good way to verify that you have set up your code correctly is by checking the barycentre of the system. For any perfect n-body system, the barycentre (centre of mass) of the system should either remain in the same place, or move at a constant velocity. This is because any N-body system has [[N-body problem - Integrals of Motion#Derivation of constant linear momentum|constant linear momentum]]. You can verify this by calculating the coordinates of the barycentre for every calculated state vector.

````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
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
```
````

If you plot `xcom` versus `ycom`, you'll actually find that this is actually not a straight line. Have a think about what this could mean. Is code wrong? Or is this maybe a manifestation of the integration errors that `solve_ivp()` introduces? You could change the integration method and see what happens!

___
### Step 9: Fun stuff
For those of you eager for something a bit more interesting, we can test whether one of the stable solutions to the 3-body problem works. For example, to test whether we can get the stable "Figure-8" solution for 3 bodies, we can simply input the [right parameters](https://en.wikipedia.org/wiki/Three-body_problem#cite_note-11) and see if it will remain stable over time.

````ad-abstract
title: Code
icon: python
collapse: open
color: 45,215,60

```py
# Figure 8: x_init       y_init       vx_init       vy_init
Yi1 = [-0.97000436,  0.24308753, 0.4662036850, 0.4323657300]
Yi2 = [        0.0,         0.0,  -0.93240737,  -0.86473146]
Yi3 = [ 0.97000436, -0.24308753, 0.4662036850, 0.4323657300]
```
````

This gives you the "Figure 8" configuration, which in theory is slightly stable:
![[f8_DOP853.png]]
If you propagate it for a long time though, you'll see that it starts to deviate. This is most likely due to propagation errors that the integrator causes. You can switch to different integrators and compare the results. In the collapsed note below, you can see what happens. For this particular case, the `Radau` and `DOP853` integrators gave me the best results:
```ad-note
title: Figure 8 plot for different propagators.
collapse: closed
Integrator method: `bdf`
![[f8_BDF.png]]

Integrator method: `DOP853`
![[f8_DOP853.png]]

Integrator method: `LSODA`
![[f8_LSODA.png]]

Integrator method: `Radau`
![[f8_Radau.png]]

Integrator method: `RK23`
![[f8_RK23.png]]

Integrator method: `RK45`
![[f8_RK45.png]]
```

If you like what you see and you are feeling adventurous, you can try the following challenges:
- Besides verifying the code by checking the barycentre velocity, you can do the same by checking that the system also has [[N-body problem - Integrals of Motion#Derivation of constant angular momentum|constant angular momentum]] and [[N-body problem - Integrals of Motion#Derivation of constant mechanical energy|constant mechanical energy]].
- Plot the barycentre triangle, such as in [this Wikipedia graphic](https://en.wikipedia.org/wiki/Three-body_problem#/media/File:Three-body_Problem_Animation_with_COM.gif).
-  Adapt the plotting code so that the dot size of the masses is in proportion to their mass value.
 - Adapt the plotting code such that you can also plot the velocity vectors of each mass in the plot. This should be relatively straightforward, since you already get the different x,y components of the velocity from the state vector.
 - Try to reproduce other stable solutions for the 3-body problem, such as the Lagrange Triangle.
 - Adapt the code for 3D propagation, and use the 3D plotting modules of Matplotlib to plot and animate it.
 - Generalize the simulator to an n-body simulator, where the user can specify the number of bodies $n$ as an input variable. Consider using classes to nicely structure the code according to the [OOP paradigm](https://en.wikipedia.org/wiki/Object-oriented_programming).
 - Currently the masses are point masses and have zero radius. This means that they can get infinitely close to one another without colliding. Could you give the masses a finite radius (so that the point masses become uniform spherical bodies) and implement some code that detect collisions if they occur during the simulation?

Have fun!

___
## Complete code
Finally, this tutorial also includes the [[3body_py|complete code]] of the discussed implementation.
