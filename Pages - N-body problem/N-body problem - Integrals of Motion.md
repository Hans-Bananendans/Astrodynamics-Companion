# N-body integrals of motion
<!-- [Wakker] section 2.1 -->
We have established that for any N-body system, we **generally** cannot describe the motion with a nice closed-form set of equations if $n>2$. But why should you believe me? In this section we will see that you can generally only get set up ten equations of motions for any N-body problem, and that this is not enough equations to solve a system of three bodies or more. These ten equations are referred to as the **integrals of motion**, and deriving them gives a lot of insight in some interesting properties that all N-body systems have in common. These properties are:
1. Any N-body system has **constant linear momentum**.
2. Any N-body system has **constant angular momentum**.
3. Any N-body system has **constant total mechanical energy**.

You will not have to take this on faith: we will derive them in a moment. You will have to know these derivations for the exam anyway.

```ad-warning
Why are they called the **integrals** of motion? Great question, because the term doesn't actually refer to [Riemannian integrals](https://en.wikipedia.org/wiki/Riemann_integral). Instead, it refers to a bunch of constants; six of which determine where the barycentre of the system is, and in which direction it moves. Three others refer to the angular momentum of the whole system, and then the last one of them is just an expression for the sum of potential and kinetic energy.

In short, beware! The **integrals** of motion are actually **constants** of motion.

```
___
## Derivation recipe
Now will follow a recipe for the derivations of the integrals of motion:

First, remember this general equation of motion (2.3 from [[Wakker]]):
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \tag{w2.3}$$

- Deriving **constant linear momentum**:
-> Sum equation $\text{w2.3}$ over all bodies $i$ in the system.

- Deriving **constant angular momentum**:
-> Calculate $\bar{r}_i \times \text{w2.3}$ and them sum over all bodies $i$.

- Deriving **constant total mechanical energy**:
-> Calculate $\dfrac{d\bar{r}_i}{dt} \cdot \text{w2.3}$ and them sum over all bodies $i$.

___
## Derivation of constant linear momentum
According to the [[N-body problem - Integrals of Motion#Derivation recipe|derivation recipe]], to start this derivation we want to sum equation $\text{w2.3}$ over all bodies $i$. This will look like this:

$$\sum_i m_i \dfrac{d^2 \bar{r}_i}{dt^2} = G \sum_i \sum_{j \neq i} \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij}$$

See the [[Derivation - N-body constant linear momentum|full derivation]] to see how you manipulate this equation. After we do this however, we find two things: Firstly, find that the barycentre of the system moves at constant speed $\bar{a}$, relative to the inertial reference frame. Splitting this up into Cartesian components gives:
$$
\dfrac{dx_{cm}}{dt} = a_1 \hspace{3em}
\dfrac{dy_{cm}}{dt} = a_2 \hspace{3em}
\dfrac{dz_{cm}}{dt} = a_3 \tag{w2.6}
$$

Secondly, we can also derive the position of the barycentre at any time in terms of the inertial reference frame. All we need to know is what its location $\bar{b}$ at some point in time was.
$$
x_{cm} = a_1 t + b_1 \hspace{3em}
y_{cm} = a_2 t + b_2 \hspace{3em}
z_{cm} = a_3 t + b_3 \tag{w2.8}
$$

We can also write this as:
$$\bar{r}_{cm} = \bar{a}t+\bar{b}$$

In other words, the barycentre of any N-body system moves in a straight line. Splitting this up into three Cartesian components gives us the first six integrals of motion.

So the conclusion here is that any N-body system has a constant amount of linear momentum. This means that since the total mass does not change, the velocity with which the whole system travels is constant. So if you were an outsider looking at such a system, you could consider the barycentre of the system and find it travelling along at some constant velocity. 

___
## Derivation of constant angular momentum
According to the [[N-body problem - Integrals of Motion#Derivation recipe|derivation recipe]], we start this derivation by taking the cross product between $\bar{r}_i$ and equation $\text{w2.3}$:

$$\sum_i \bar{r}_i \times
\left( m_i \dfrac{d^2 \bar{r}_i}{dt^2} \right) = \sum_i \bar{r}_i \times
\left( \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \right) $$

If we perform the [[Derivation - N-body constant angular momentum|full derivation]], we find that the angular momentum $\bar{H}$ of the whole system is equal to:
$$\bar{H} = \sum_i m_i \bar{r}_i \times \dfrac{d \bar{r}_i}{dt}  = \bar{c} \tag{w2.10}$$


So that means that the equation tells us directly that the angular momentum is constant, because its time derivative is zero. To get the next three integrals of motion, we split equation $\text{w2.10}$ up into the Cartesian components:

$$
\begin{align}
H_x = \sum_i m_i (y_i\dot{z}_i-z_i \dot{y_i}) = c_1 \\
H_y = \sum_i m_i (z_i\dot{x}_i-x_i \dot{z_i}) = c_2 \tag{w2.11} \\
H_z = \sum_i m_i (x_i\dot{y}_i-y_i \dot{x_i}) = c_3
\end{align}
$$
___
## Derivation of constant mechanical energy
According to the [[The N-body problem#N-body integrals of motion|recipe]], we start this derivation by taking the scalar product between $d\bar{r}_i/dt$ and equation $\text{w2.3}$, and sum over $i$:

$$\sum_i m_i \dfrac{d\bar{r}_i}{dt} \cdot \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \dfrac{d\bar{r}_i}{dt} \cdot \bar{r}_{ij} $$

After performing the [[Derivation - N-body constant total energy|full derivation]], we end up with the following equation:

$$ 
\begin{align}
\sum_i \dfrac{1}{2} m_i V_i^2 
\hspace{1.5em} - \hspace{1.5em}
\dfrac{1}{2} \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r_{ij}} \hspace{2.5em} = \hspace{2.5em} 
C 
\hspace{3.5em} \tag{w2.17}
\\
\hspace{0em} 
\begin{matrix} \text{total kinetic} \\ \text{energy} \end{matrix}
\hspace{5em} 
\begin{matrix} \text{total potential} \\ \text{energy} \end{matrix}
\hspace{5em} 
\begin{matrix} \text{total mechanical} \\ \text{energy} \end{matrix}
\end{align}
$$

This equation has two terms, one of which corresponds to the total **kinetic** energy in the system, and the other to the total **potential** energy of the system. So as the bodies move closer to each other, their relative velocity will increase, trading potential energy for kinetic energy. And vice versa when moving away from each other. However, equation $\text{w2.17}$ shows that the total amount of (mechanical) energy remains constant.

This last piece of information forms the tenth integral of motion:
$$\mathcal{E}_{kin} + \mathcal{E}_{pot} = C$$
___

## Summary - integrals of motion
```ad-summary
title: Recipe for the derivations of the integrals of motion

First, remember this general equation of motion (2.3 from [[Wakker]]):
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \tag{w2.3}$$

- Deriving **constant linear momentum**:
-> Sum equation $\text{w2.3}$ over all bodies $i$ in the system.

- Deriving **constant angular momentum**:
-> Calculate $\bar{r}_i \times \text{w2.3}$ and them sum over all bodies $i$.

- Deriving **constant total mechanical energy**:
-> Calculate $\dfrac{d\bar{r}_i}{dt} \cdot \text{w2.3}$ and them sum over all bodies $i$.
```

```ad-summary
title: The ten integrals of motion

From constant linear momentum:
$$
\dfrac{dx_{cm}}{dt} = a_1 \hspace{3em}
\dfrac{dy_{cm}}{dt} = a_2 \hspace{3em}
\dfrac{dz_{cm}}{dt} = a_3 \tag{w2.6}
$$


$$
x_{cm} = a_1 t + b_1 \hspace{3em}
y_{cm} = a_2 t + b_2 \hspace{3em}
z_{cm} = a_3 t + b_3 \tag{w2.8}
$$

From constant angular momentum:
$$
\begin{align}
H_x = \sum_i m_i (y_i\dot{z}_i-z_i \dot{y_i}) = c_1 \\
H_y = \sum_i m_i (z_i\dot{x}_i-x_i \dot{z_i}) = c_2 \tag{w2.11} \\
H_z = \sum_i m_i (x_i\dot{y}_i-y_i \dot{x_i}) = c_3
\end{align}
$$

From constant mechanical energy:
$$\mathcal{E}_{kin} + \mathcal{E}_{pot} = C$$
```
___