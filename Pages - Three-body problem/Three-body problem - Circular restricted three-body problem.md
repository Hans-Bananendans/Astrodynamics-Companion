# Three-body problem - Circular restricted three-body problem

> [!wip] ## ** !!! This section is still under construction !!! **

<!-- Wakker section 3.3 -->
___
## Sketch
Circular restricted three-body problem is a special case of three-body problem:
- **Restricted** -> One of the bodies has negligible mass ($m_3 >> m_1, m_2$)
- **Circular** -> Other two masses ($m_1, m_2$) move in circular orbits around barycentre (and therefore each other)

This simplification of General 3BP to CR3BP causes reduction of order from 18 to 6. The two more massive bodies also move in the same plane, which makes sense, because these bodies act as though it is a two-body system. Conservation of angular momentum and energy holds for these bodies, but **not** for the third (mass-less) body.

<Picture on page 56>
![[cr3bp_frames.png]]

We are only interested in describing the motion of $m_3$, since we know the motion of the other bodies. We're going to attach a rotating reference frame to the $m_1, m_2$ system, which will rotate around the $Z$-axis, and then describe the motion of $m_3$ in that. To convert between the frames, you have to apply a transformation according to:
$$\dfrac{d\bar{r}}{dt} = \dfrac{\delta \bar{r}}{\delta t} + \bar{\omega} \times \bar{r} \tag{w3.37}$$

Note that $\omega$ is the (constant) rotational speed with which the frame rotates around the $Z$-axis, so $\omega = \dot{\theta} = d\theta/dt$.

Lecturer says we use the Jacobi form of the EOMs, but equation w3.35 is clearly the Euler form -> What the fuck? -> Nope, setup is defined from barycentre, vector to P is pointing from barycentre of m1,m2, so indeed Jacobi

Now transform the system description into a form in terms of the rotating frame. From Jacobi form when $m_3 = 0$, we have:

$$\dfrac{d^2 \bar{r}}{dt^2} = -G \dfrac{m_1}{r_1^3} \bar{r}_1 -G \dfrac{m_2}{r_2^3} \bar{r}_2$$


Differentiate the definition of the transformation so it describes a second order derivative of $\bar{r}$, using the product rule:
$$\dfrac{d^2\bar{r}}{dt^2} = \dfrac{d}{dt} \left( \dfrac{\delta \bar{r}}{\delta t}\right) + \bar{\omega} \times \dfrac{d\bar{r}}{dt}$$

Equation $\text{w3.37}$ can be used e first term on the RHS can be further expanded by using the very same rule, but replacing $\bar{r}$ with $\delta \bar{r}/\delta t$:

$$\dfrac{d}{dt} \left( \dfrac{\delta \bar{r}}{\delta t}\right) = 
\dfrac{d\left( \dfrac{\delta \bar{r}}{\delta t}\right)}{dt} = 
\dfrac{\delta }{\delta t} \left( \dfrac{\delta \bar{r}}{\delta t}\right)+ \bar{\omega} \times \left( \dfrac{\delta \bar{r}}{\delta t}\right) = 
\dfrac{\delta^2 \bar{r}}{\delta t^2}+ \bar{\omega} \times \dfrac{\delta \bar{r}}{\delta t}$$

Taking cross product of $\bar{\omega}$ and the frame transformation equation:
$$\bar{\omega} \times \dfrac{d\bar{r}}{dt} = \bar{\omega} \times \dfrac{\delta \bar{r}}{\delta t} + \bar{\omega} \times (\bar{\omega} \times \bar{r} )$$


Substitute and you end up with:
$$\dfrac{d^2\bar{r}}{dt^2} = 
\dfrac{\delta^2 \bar{r}}{\delta t^2} + \bar{\omega} \times \dfrac{\delta \bar{r}}{\delta t} + 
\bar{\omega} \times \dfrac{\delta \bar{r}}{\delta t} + \bar{\omega} \times (\bar{\omega} \times \bar{r} )
=
\dfrac{\delta^2 \bar{r}}{\delta t^2} + 
2 \bar{\omega} \times \dfrac{\delta \bar{r}}{\delta t} + 
\bar{\omega} \times (\bar{\omega} \times \bar{r} )
$$

Now you can inverse it to solve for $\delta^2 \bar{r}/\delta t^2$, and substitute for $d^2 \bar{r}/ dt^2$ the Jacobi equation of motion:
$$\dfrac{\delta^2 \bar{r}}{\delta t^2} = 
\dfrac{d^2\bar{r}}{dt^2} - 
2 \bar{\omega} \times \dfrac{\delta \bar{r}}{\delta t} - 
\bar{\omega} \times (\bar{\omega} \times \bar{r} )
$$

$$
\begin{align}
\dfrac{\delta^2 \bar{r}}{\delta t^2} = 
\underbrace{-G \left( \dfrac{m_1}{r_1^3} \bar{r}_1 + \dfrac{m_2}{r_2^3} \bar{r}_2 \right)} 
\hspace{1em}
\underbrace{- \hspace{0.5em} 2 \bar{\omega} \times \dfrac{\delta \bar{r}}{\delta t} }
\hspace{1em}
\underbrace{- \hspace{0.5em} \bar{\omega} \times (\bar{\omega} \times \bar{r} )}
\\
\hspace{1em}
\begin{matrix}\text{gravitational} \\ \text{acceleration}\\ \text{due to }m_1,m_2\end{matrix}
\hspace{3em}
\begin{matrix}\text{Coriolis} \\ \text{acceleration}\end{matrix}
\hspace{1.5em}
\begin{matrix}\text{centrifugal} \\ \text{acceleration}\end{matrix}
\hspace{0.5em}
\end{align}
$$

## Nondimensionalization
Goal: Nondimensionalize mass, length, and time:
- **Mass**: For mass, make the following substitution: $$\mu = \dfrac{m_2}{m_1 + m_2} \quad , \quad 1-\mu = \dfrac{m_1}{m_1 + m_2}$$ and specify that $m_1$ is the bigger mass, i.e. $m_1 > m_2$, $\mu \leq 0.5$.
- **Distance**: Choose a distance $P_1 P_2$ as the distance unit: $$\dfrac{OP_1}{OP_2} = \dfrac{m_2}{m_1} = \dfrac{\mu}{1-\mu}$$ and so $$\begin{cases}OP_1 = \mu \\ OP_2 = 1-\mu \end{cases}$$
- **Time**: Choose the angular rate of the rotating frame as the unit of time ($\dfrac{1}{\omega}$) -> $$t^* = t\omega$$ -> $$m_2 \omega^2 OP_2 = G \dfrac{m_1 m_2}{(P_1 P_2)^2} \text{ how do you get to this shit?}$$

Rewrite equation of motion in terms of these new units:
Some SUPER FUCKED UP MATH

<Warning about dropping of \*-symbols from equation, Wakker being typical Wakker>

Drop the asterisks

You end up with
$$
\dfrac{\delta^2 \bar{r}}{\delta t^2} = 
-\left( \dfrac{1-\mu}{r_1^3} \bar{r}_1 + \dfrac{\mu}{r_2^3} \bar{r}_2 \right)
\hspace{0em}
- 2 \hat{z} \times \dfrac{\delta \bar{r}}{\delta t} 
\hspace{0em}
- \hat{z} \times (\hat{z} \times \bar{r} )
$$


Gather six scalar compatibility equations
$$\bar{r} = \begin{bmatrix} x \\ y \\ z\end{bmatrix} 
\quad , \quad
\bar{r}_1 = \begin{bmatrix} \mu+x \\ y \\ z\end{bmatrix} 
\quad , \quad
\bar{r}_2 = \begin{bmatrix} -(1-\mu-x) \\ y \\ z\end{bmatrix} 
\quad , \quad
\dfrac{\delta \bar{r}}{\delta t} = \begin{bmatrix} \dot{x} \\ \dot{y} \\ \dot{z} \end{bmatrix} 
$$
see figure:
![[cr3bp_vectorhelp1.png]]

Other two equations
$$
\hat{z} \times \dfrac{\delta \bar{r}}{\delta t} = \begin{bmatrix} -\dot{y} \\ \dot{x} \\ 0\end{bmatrix} 
\quad , \quad
\hat{z} \times (\hat{z} \times \bar{r}) = \begin{bmatrix} -x \\ -y \\ 0\end{bmatrix} 
$$
Put expanded math into math block


Write the equation of motion as a system of three second-order scalar differential equations
$$
\dfrac{\delta^2 \bar{r}}{\delta t^2} = 
-\left( \dfrac{1-\mu}{r_1^3} \bar{r}_1 + \dfrac{\mu}{r_2^3} \bar{r}_2 \right)
- 2 \hat{z} \times \dfrac{\delta \bar{r}}{\delta t} 
- \hat{z} \times (\hat{z} \times \bar{r} ) $$
or by writing out the vectors:
$$\begin{bmatrix}\ddot{x} \\ \ddot{y} \\ \ddot{z} \end{bmatrix}
= -\left( \dfrac{1-\mu}{r_1^3} \begin{bmatrix} \mu+x \\ y \\ z\end{bmatrix}  + \dfrac{\mu}{r_2^3} \begin{bmatrix} -(1-\mu-x) \\ y \\ z\end{bmatrix} \right)
\hspace{0em}
- 2 \begin{bmatrix} -\dot{y} \\ \dot{x} \\ 0\end{bmatrix}
\hspace{0em}
- \begin{bmatrix} -x \\ -y \\ 0\end{bmatrix} 
$$

$$
= \begin{cases}
\ddot{x} = 
-\left( \dfrac{1-\mu}{r_1^3} \cdot (\mu+x) + \dfrac{\mu}{r_2^3} \cdot -(1-\mu-x) \right) - 2 \cdot -\dot{y} - -x 
\\
\ddot{y} = 
-\left( \dfrac{1-\mu}{r_1^3} y + \dfrac{\mu}{r_2^3} y \right)
- 2 \cdot\dot{x} 
- -y
\\
\ddot{z} = 
-\left( \dfrac{1-\mu}{r_1^3} z + \dfrac{\mu}{r_2^3} z \right)
- 2 \cdot 0 
- 0
\end{cases}
$$
$$
\begin{align}
= 
\begin{cases}
\ddot{x} \hspace{2em} - 2\dot{y} \hspace{1em}= \hspace{1em}
x \hspace{2em} -\dfrac{1-\mu}{r_1^3} (\mu+x) + \dfrac{\mu}{r_2^3} (1-\mu-x)
\\
\ddot{y} \hspace{2em}+ 2\dot{x} \hspace{1em} = \hspace{1em}
y \hspace{2em} - \dfrac{1-\mu}{r_1^3} y - \dfrac{\mu}{r_2^3} y
\\
\ddot{z} \hspace{5.3em}= \hspace{1em}
\hspace{2.8em} - \dfrac{1-\mu}{r_1^3} z - \dfrac{\mu}{r_2^3} z
\end{cases}
\\
\underbrace{\hspace{2.5em}} \hspace{1.5em} 
\underbrace{\hspace{2.5em}} \hspace{0.5em}
\underbrace{\hspace{15em}} \hspace{0em}
\\
\text{Coriolis} \hspace{0.5em} 
\text{centrifugal} \hspace{4em}
\text{gravitational} \hspace{5em}
\end{align}
\tag{w3.49}
$$

Introduce **scalar potential function** $U$ (link to wikipedia visualization)
$$U = \dfrac{1}{2} (x^2 + y^2) + \dfrac{1-\mu}{r_1} + \dfrac{\mu}{r_2}$$
Mathematically speaking, this function is chosen somewhat arbitrarily, we could choose something else. However, we use this function because its partial derivatives look very similar to the system of equations of motion of $\text{w3.49}$:
\<partial derivatives of U here>

Simplify equations of motion by using scalar potential derivatives:
$$
\begin{align}
= 
\begin{cases}
\ddot{x} \hspace{2em} - 2\dot{y} \hspace{1em} = 
\hspace{1em} \dfrac{\partial U}{\partial x}
\\
\ddot{y} \hspace{2em}+ 2\dot{x} \hspace{1em} = 
\hspace{1em} \dfrac{\partial U}{\partial y}
\\
\ddot{z} \hspace{5.3em}= \hspace{1em}
\dfrac{\partial U}{\partial z}
\end{cases}
\\
\underbrace{\hspace{2.5em}} \hspace{1.5em} 
\underbrace{\hspace{4em}} \hspace{-1.5em}
\\
\text{Coriolis} \hspace{1.5em} 
\begin{matrix}\text{centrifugal \&} \\\text{gravitational}\end{matrix}\hspace{-3em}
\end{align}
\tag{w3.50}
$$


Remarks about potential function $U$:
 - Accounts for gravitational and centrifugal accelerations
 - Does not account for Coriolis acceleration, which contains velocity components
 - Produces a non-central forcefield
 - Is not time-dependent and therefore conservative.

Plot code to help folks out:
![[CR3BP_potential.png]]

> [!python]- *cr3bp_potential.py*
> ```py
> """
> cr3bp_potential.py
> 
> @author: Johan Monster
> """
> 
> import numpy as np
> import matplotlib.pyplot as plt
> 
> plot_gravitational_potential_U1 = True
> plot_gravitational_potential_U2 = True
> plot_centrifugal_potential = True
> 
> mu = 0.2 # You can set 0 < mu < 0.5
> 
> X, Y = np.mgrid[-2.5:2.5:64j, -2.5:2.5:64j]
> Z = 0
> U = np.zeros([len(X),len(Y)])
> r1 = np.sqrt(  (mu+X)**2 + Y**2 + Z**2)
> r2 = np.sqrt((1-mu-X)**2 + Y**2 + Z**2)
> 
> if plot_gravitational_potential_U1:
>     U += (1-mu)/r1
> 
> if plot_gravitational_potential_U2:
>     U += mu/r2
> 
> if plot_centrifugal_potential:
>     U += 0.5*(X**2 + Y**2)
> 
> fig = plt.figure(figsize=(7,8))
> ax = fig.add_subplot(111, projection="3d")
> ax.set_zlim3d(-10,10)
> ax.plot_surface(X, Y, U, cmap="gnuplot", linewidth=1, rstride=4, cstride=4, alpha=0.7)
> ax.plot_wireframe(X, Y, U, color='k', linewidth=1, rstride=4, linestyle="solid", cstride=4, alpha=0.9)
> ax.contour(X, Y, U, 64, linewidths=1, colors="k", linestyles="solid",alpha=0.7)
> 
> ax.contour(X, Y, U, 64, linewidths=1, cmap="gnuplot", linestyles="solid", offset=-10)
> plt.show()
> ```

___