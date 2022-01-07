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

The other two terms are due to the third body being present. These accelerations point along their respective position vector and are therefore positive.

___
## Equations of motion - Jacobi form
Of course Jacobi thought all this was much too easy, and so he came up with a seemingly more convoluted, but ultimately more powerful formulation.