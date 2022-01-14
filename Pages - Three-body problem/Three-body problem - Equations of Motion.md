# Three-body problem - Equations of Motion

```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25
```

<!-- Wakker section 3.1 -->
As mentioned [[The N-body problem|previously]], the three-body problem looks at how three masses behave under the influence of each other's gravity. Although such a system can be described deterministically, its behaviour is inherently chaotic; you can never describe the system's state at infinity without specifying some initial conditions with infinite precision. Small errors always become large errors.

Nonetheless, in this section we are going to lay out the equations of motion of the three body problem. It turns out that these come in several flavours:
 - The **Euler form** (or classical form)
 - The **Lagrange form**
 - The **Jacobi form**

```ad-note
title: Explain what the point of having different flavours is
icon: hammer
color: 240,200,25
```

```ad-note
The aformentioned forms all refer to mathematicians who struggled with the three-body problem during their lives. The moral of the story is that if you struggle with the three-body problem enough, you might also get your very own form of equations of motion named after you.
```
___

## Equations of motion - Euler form
To derive the equations of motion of the three-body problem, we start with the general formulation that we derived for the N-body problem, which hopefully by now should look familiar. In short, it tells you that a body $i$ experiences a bunch of gravitational forces from all the bodies $j$ around it, in the following way:
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \tag{w2.3}$$

So if we talk about the three-body problem, we have only 3 bodies, not N. So from now on, we're just going to consider bodies $i$, $j$, and $k$ (so $j$ now refers to a single body). 

![[threebody_euler.png]]

According to equation $\text{w2.3}$, body $i$ then experiences the following net force:
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} + G \dfrac{m_i m_k}{r^3_{ik}} \bar{r}_{ik}$$

or, dividing everything by $m_i$, the following acceleration:

$$\dfrac{d^2 \bar{r}_i}{dt^2} = G \dfrac{m_j}{r^3_{ij}} \bar{r}_{ij} + G \dfrac{m_k}{r^3_{ik}} \bar{r}_{ik} \tag{w3.1}$$

This the **Euler form** that was alluded to earlier.

___
## Equations of motion - Lagrange form
In the Euler from, we use a bunch of absolute position vectors (such as $\bar{r}_i$) as wel as relative position vectors (such as $\bar{r}_{ij}$). To get to the Lagrange form, we're going to ditch the absolute position vectors and just use three relative position vectors to describe the problem. These vectors are visualized below:

![[threebody_lagrange.png]]

```ad-tip
title: Tip: A matter of perspective
icon: lightbulb

You can think of the difference between the Euler form and the Lagrange form as follows: In the Euler form, you can stand at the origin of the inertial reference frame and before you you will see the three bodies move around each other. With the Lagrange form, you're going to sit on one of the masses and see how one of the other two masses moves around. But because the mass you're sitting on keeps moving around as well, your perspective will as a result constantly move.
```

The way the relative position vectors are set up in the figure results in a compatibility equation:
$$\bar{r}_{12} + \bar{r}_{23} + \bar{r}_{31} = 0$$
This is essentially a mathematical way of saying: _"If you go from $m_1$ to $m_2$, then to $m_3$, and then back to $m_1$, you are exactly where you started."_ Look at the figure above if you are not convinced.

So to get to the Lagrange form, we want to formulate the problem with one of the bodies as reference, rather than the origin of the inertial reference frame. Our first step is to start with body $m_1$ and see if we can describe the acceleration of $m_2$. We are therefore interested in the second derivative of vecor $\bar{r}_{12}$. Since we know that:
$$\bar{r}_{12} = \bar{r}_2 - \bar{r}_1$$

We can differentiate this twice to get the acceleration:
$$\dfrac{d^2 \bar{r}_{12}}{dt^2} = \dfrac{d^2 \bar{r}_{2}}{dt^2} - \dfrac{d^2 \bar{r}_{1}}{dt^2}$$

And then just shove the Euler formulation from before into the right side of this equation:

$$\dfrac{d^2 \bar{r}_{12}}{dt^2} = 
G \dfrac{m_3}{r^3_{23}} \bar{r}_{23} + G \dfrac{m_1}{r^3_{21}} \bar{r}_{21} - 
\left(
G \dfrac{m_2}{r^3_{12}} \bar{r}_{12} + G \dfrac{m_3}{r^3_{13}} \bar{r}_{13}
\right)$$
As you can see, there are no absolute position vectors in here anymore, just relative vectors. We can write this to a slightly different form, which is the Lagrangian form. On the way, we also use the fact that $\bar{r}_{12} = -\bar{r}_{21}$ and $\bar{r}_{31} = -\bar{r}_{13}$, because we said we would just use the three vectors from the figure above:

$$\dfrac{d^2 \bar{r}_{12}}{dt^2} = 
G \left[
m_3 \left( \dfrac{\bar{r}_{23}}{r^3_{23}} + \dfrac{\bar{r}_{13}}{r^3_{13}} \right) 
- (m_1+m_2) \dfrac{\bar{r}_{12}  }{r^3_{12}} 
\right]$$

and in the same way, you can derive the motion of the other two masses:
$$\dfrac{d^2 \bar{r}_{23}}{dt^2} = 
G \left[
m_1 \left( \dfrac{\bar{r}_{31}}{r^3_{31}} + \dfrac{\bar{r}_{12}}{r^3_{12}} \right) 
- (m_2+m_3) \dfrac{\bar{r}_{23}  }{r^3_{23}} 
\right]$$

$$\dfrac{d^2 \bar{r}_{31}}{dt^2} = 
G \left[
m_2 \left( \dfrac{\bar{r}_{12}}{r^3_{12}} + \dfrac{\bar{r}_{23}}{r^3_{23}} \right) 
- (m_3+m_1) \dfrac{\bar{r}_{31}  }{r^3_{31}} 
\right]$$

Okay, the mathematics check out, but who in their right mind would use this formulation when you already have a perfectly good (and much easier to remember) Euler formulation? The [[Wakker]] book does not explain this at all, but it's in part because the Lagrange formulation offers some insight that the Euler form does not. It turns out you can split the above equations into a two-body part and a third-body part:

![[threebody_lagrangewithbenefits.png]]

The two-body term is simply the acceleration that $m_2$ experiences from $m_1$ pulling on it. There is a minus-sign in front of this term, because the acceleration points in **opposite direction** with respect to position vector $\bar{r}_{12}$. If this was a two-body problem, this would be the only term you would have.

The other two terms are due to the third body being present. These accelerations point **along** their respective position vector and are therefore positive.

___
## Equations of motion - Jacobi form
Of course Jacobi thought all this was much too easy, and so he came up with a seemingly more convoluted, but ultimately more powerful formulation. To use this form, we do the following:
1. Place the inertial reference frame at the [[N-body problem - Barycentric relative motion|barycentre]] $O$ of the three-body system.
2. Draw a position vector $\bar{r}_{12}$ from body $m_1$ to body $m_2$.
3. Locate the two-body barycentre of $m_1$ and $m_2$. We call this point $O_{12}$.
4. Then we draw a vector $\bar{R}$ from $O_{12}$ that goes through $O$.
5. Using this vector $\bar{R}$, we describe the position of body $m_3$. Because of the definition of the barycentre, you can **always** do this ($\bar{R}$ will never "miss" $m_3$).

![[threebody_jacobi.png]]

It turns out that you can write the equations of motion of this system **just** with  $\bar{r}_{12}$ and $\bar{R}$. This may not seem like much, but it's actually remarkable. The Euler and the Lagrange formulation both relied on three position vectors $\bar{r}$, but the Jacobi formulation has only two, and is still able to describe the whole system. 

As we will see, you still end up with second-order differential equations, and so whereas the Euler and Lagrange formulations require 18 equations to solve completely (remember the [[N-body problem - Integrals of Motion|integrals of motion]]), by just rewriting the coordinate system to the Jacobi form you can reduce this number to only 12 equations. Mind you, it still does not allow you to solve the three-body problem in general, but it can be very insightful for several applications within the solar system, such as describing the Sun-Earth-Moon system.

To use this form, we use a parameter $\alpha$, which is basically how much of the mass $m_1$ has relative to the $m_1$, $m_2$-system:
$$\alpha = \dfrac{m_1}{m_1+m_2} \tag{w3.6}$$

and we use $M$ for the total system mass:
$$M = m_1 + m_2 + m_3$$

```ad-note
title: Add the derivation of the Jacobi formulation (see Wakker p. 48)
icon: hammer
color: 240,200,25
```

You can then write the equations of motion as:

$$\dfrac{d^2 \bar{R}}{dt^2} = 
- G \left[
(m_1+m_2) \dfrac{\bar{r}_{12}  }{r^3_{12}}+m_3 \left( \dfrac{\bar{r}_{13}}{r^3_{13}} - \dfrac{\bar{r}_{23}}{r^3_{23}} \right) 
\right] \tag{w3.9-1}$$

$$\dfrac{d^2 \bar{r}_{12}}{dt^2} = 
- G M \left[ \alpha \dfrac{\bar{r}_{13}}{r^3_{13}} +
(1-\alpha)\dfrac{\bar{r}_{23}}{r^3_{23}}
\right] \tag{w3.9-2}$$

Which in 3D is a 12th-order system, as opposed to an 18th-order system. We can simplify the Jacobi form with some assumptions, which turn out to be very useful in practice. [[Wakker]] discusses two such cases: the **lunar case** and the **planetary case**.


### Lunar case
In the lunar case, we make use of the fact that there is a large mass difference and a large distance difference between the three bodies. We use the following convention:
 - $m_1$: Moon
 - $m_2$: Earth
 - $m_3$: Sun

Since the mass of the Earth ($6.0\times 10^{24}$ kg) is much larger than the mass of the Moon ($7.3\times 10^{22}$ kg) and therefore:

$$\alpha = \dfrac{m_1}{m_1+m_2} \approx \dfrac{m_1}{m_1} = 1$$

Furthermore, since the Earth-Moon distance ($4 \times 10^8$ m) is much smaller than the Earth-Sun distance ($1.5 \times 10^{11}$ m) we can asssume that:

$$\bar{r}_{13} \approx \bar{r}_{23} \approx \bar{R}$$

This collapses system $\text{w3.9}$ into a much simpler form:

$$\dfrac{d^2 \bar{R}}{dt^2} = -G(m_1+m_2) \dfrac{\bar{r}_{12}}{r^3_{12}} $$

$$\dfrac{d^2 \bar{r}_{12}}{dt^2} = - G M \dfrac{\bar{R}}{R^3}$$

```ad-note
title: Add math block for this "collapse"
icon: hammer
color: 240,200,25
```

![[threebody_jacobi_lunar.png]]

### Planetary case
In the planetary case, we use the following convention:
 - $m_1$: Sun
 - $m_2$: Earth
 - $m_3$: Some other planet (in the solar system)


Since the mass of the Earth ($6.0\times 10^{24}$ kg) is much smaller than the mass of the Sun ($2.0\times 10^{30}$ kg), we get:
$$\alpha = \dfrac{m_1}{m_1+m_2} \approx \dfrac{m_1}{m_1} = 1$$

For the same reason, the barycentre of the Sun-Earth system will lie very close to the position of the Sun ([in reality it is deep inside the sun](https://spaceplace.nasa.gov/barycenter/en/)), and so:

$$\bar{r}_{13} \approx  \bar{R}$$

Furthermore, you can assume that the other planet will have a much smaller mass than then sun, meaning that:

$$\dfrac{m_3}{m_1+m_2} << 1$$

This collapses system $\text{w3.9}$ into the same form as for the lunar case.


```ad-note
title: Add math block for this "collapse"
icon: hammer
color: 240,200,25
```
![[threebody_jacobi_planetary.png]]
___

## Summary - Three-body Equations of Motion

```ad-summary
title: Three forms of the three-body equations of motion

**Euler form** (18th order system):

$$\begin{cases}
\dfrac{d^2 \bar{r}_1}{dt^2} = G \dfrac{m_2}{r^3_{12}} \bar{r}_{12} + G \dfrac{m_3}{r^3_{13}} \bar{r}_{13}\\
\dfrac{d^2 \bar{r}_2}{dt^2} = G \dfrac{m_1}{r^3_{21}} \bar{r}_{21} + G \dfrac{m_3}{r^3_{23}} \bar{r}_{23}\\
\dfrac{d^2 \bar{r}_3}{dt^2} = G \dfrac{m_1}{r^3_{31}} \bar{r}_{31} + G \dfrac{m_2}{r^3_{32}} \bar{r}_{32}\\
\end{cases}$$


**Lagrange form** (18th order system):
$$\begin{cases}
\dfrac{d^2 \bar{r}_{12}}{dt^2} = 
G \left[
m_3 \left( \dfrac{\bar{r}_{23}}{r^3_{23}} + \dfrac{\bar{r}_{13}}{r^3_{13}} \right) 
- (m_1+m_2) \dfrac{\bar{r}_{12}  }{r^3_{12}} 
\right] \\
\dfrac{d^2 \bar{r}_{23}}{dt^2} = 
G \left[
m_1 \left( \dfrac{\bar{r}_{31}}{r^3_{31}} + \dfrac{\bar{r}_{12}}{r^3_{12}} \right) 
- (m_2+m_3) \dfrac{\bar{r}_{23}  }{r^3_{23}} 
\right] \\
\dfrac{d^2 \bar{r}_{31}}{dt^2} = 
G \left[
m_2 \left( \dfrac{\bar{r}_{12}}{r^3_{12}} + \dfrac{\bar{r}_{23}}{r^3_{23}} \right) 
- (m_3+m_1) \dfrac{\bar{r}_{31}  }{r^3_{31}} 
\right] \\
\end{cases}$$

**Jacobi form** (12th order system):
$$\begin{cases}
\dfrac{d^2 \bar{R}}{dt^2} = 
- G \left[
(m_1+m_2) \dfrac{\bar{r}_{12}  }{r^3_{12}}+m_3 \left( \dfrac{\bar{r}_{13}}{r^3_{13}} - \dfrac{\bar{r}_{23}}{r^3_{23}} \right) 
\right] \\
\dfrac{d^2 \bar{r}_{12}}{dt^2} = 
- G M \left[ \alpha \dfrac{\bar{r}_{13}}{r^3_{13}} +
(1-\alpha)\dfrac{\bar{r}_{23}}{r^3_{23}}
\right]
\end{cases}$$
with
$$\alpha = \dfrac{m_1}{m_1+m_2} \hspace{2em} , \hspace{2em} M = m_1 + m_2 + m_3$$


```