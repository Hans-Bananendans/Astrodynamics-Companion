# Derivation - N-body constant angular momentum
```ad-note
title: Note: A less detailed derivation can be found on page 26-27 of the [[Wakker|Wakker book]].
```

First, let's keep equation $\text{w2.3}$ close on hand, as we will need it in a moment:
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \tag{w2.3}$$

According to the [[N-body problem - Integrals of Motion#Derivation recipe|derivation recipe]], we start this derivation by taking the cross product between $\bar{r}_i$ and equation $\text{w2.3}$:

$$\sum_i \bar{r}_i \times
\left( m_i \dfrac{d^2 \bar{r}_i}{dt^2} \right) = \sum_i \bar{r}_i \times
\left( \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \right) $$

If we remember that $\bar{r}_{ij}=\bar{r}_{j}-\bar{r}_{i}$, we can rewrite this:

$$\sum_i \bar{r}_i \times
\left( m_i \dfrac{d^2 \bar{r}_i}{dt^2} \right) = \sum_i \bar{r}_i \times
\left( \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} (\bar{r}_{j} - \bar{r}_{i}) \right) $$
$$\sum_i m_i \bar{r}_i \times\dfrac{d^2 \bar{r}_i}{dt^2} = G \sum_i \sum_{j \neq i} \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_i \times \bar{r}_{j} - G \sum_i \sum_{j \neq i} \dfrac{m_i m_j}{r^3_{ij}} \cancel{\bar{r}_i \times \bar{r}_{i}}^{=0} $$
$$\sum_i m_i \bar{r}_i \times\dfrac{d^2 \bar{r}_i}{dt^2} = G \sum_i \sum_{j \neq i} \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_i \times \bar{r}_{j}$$

At this point the book says that the right-hand side is zero "_due to its anti-symmetric properties_". That's not very helpful, so check the math block below to see why this is indeed true.

```ad-note
title: Why the right-hand side of that equation is zero
icon: paperclip
collapse: closed
color: 180,180,180

$$ \text{Why is } G \sum_{i=1}^n \sum_{\substack{j=1\\j \neq i}}^n \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_i \times \bar{r}_{j} \text{ equal to 0?} \tag{r1}$$

The reason why this is the case is because it will produce pairs of vectors that cancel each other out. To illustrate this, we will choose $n=3$, and write out all the terms:

$$G \sum_{i=1}^3 \sum_{\substack{j=1\\j \neq i}}^3 \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_i \times \bar{r}_{j} \tag{r2}$$

$$= G \dfrac{m_1 m_2}{r^3_{12}} \bar{r}_1 \times \bar{r}_{2} + G \dfrac{m_1 m_3}{r^3_{13}} \bar{r}_1 \times \bar{r}_{3} + G \dfrac{m_2 m_1}{r^3_{21}} \bar{r}_2 \times \bar{r}_{1} $$
$$ + G \dfrac{m_2 m_3}{r^3_{23}} \bar{r}_2 \times \bar{r}_{3} + G \dfrac{m_3 m_1}{r^3_{31}} \bar{r}_3 \times \bar{r}_{1} + G \dfrac{m_3 m_2}{r^3_{32}} \bar{r}_3 \times \bar{r}_{2} \tag{r3}$$

Now remember that the cross product of two vectors is [anticommutative](https://en.wikipedia.org/wiki/Anticommutative_property), meaning that:
$$\bar{r}_i \times \bar{r}_{j} = -(\bar{r}_j \times \bar{r}_{i}) \tag{r4}$$

In addition, remember that the length of two identical but opposing vectors is the same:
$$|\bar{r}_{ij}| = |\bar{r}_{ji}| \tag{r5}$$

We can rewrite $\text{r3}$ as:
$$= G \dfrac{m_1 m_2}{r^3_{12}} \bar{r}_1 \times \bar{r}_{2} + G \dfrac{m_1 m_3}{r^3_{13}} \bar{r}_1 \times \bar{r}_{3} - G \dfrac{m_2 m_1}{r^3_{12}} \bar{r}_1 \times \bar{r}_{2} $$
$$ + G \dfrac{m_2 m_3}{r^3_{23}} \bar{r}_2 \times \bar{r}_{3} - G \dfrac{m_3 m_1}{r^3_{13}} \bar{r}_1 \times \bar{r}_{3} - G \dfrac{m_3 m_2}{r^3_{23}} \bar{r}_2 \times \bar{r}_{3} \tag{r6}$$

If you look closely, you will see that there are three pairs of identical terms, one always positive and the other always negative. So every term cancels out, and this is indeed equal to zero.


```

So if the right-hand side of the previous equation is zero, then the right-hand side of the equation is also equal to zero:
$$\sum_i m_i \bar{r}_i \times\dfrac{d^2 \bar{r}_i}{dt^2} = 0$$
We can extract one differential operator and write this as follows:
$$\dfrac{d}{dt} \left( \sum_i m_i \bar{r}_i \times \dfrac{d \bar{r}_i}{dt} \right) = 0 \tag{w2.9}$$
Now we can integrate and note that the right hand side is actually the same thing as the total angular momentum (see the figure below):
$$\bar{H} = \sum_i m_i \bar{r}_i \times \dfrac{d \bar{r}_i}{dt}  = \bar{c} \tag{w2.10}$$

![[angular_momentum.png|Figure 1: The angular momentum of mass i. Note the implicit assumption that the the mass is constant over time.]]

So that means that the equation tells us directly that the angular momentum is constant, because its time derivative is zero. To get the next three integrals of motion, we split equation $\text{w2.10}$ up into the Cartesian components:

$$
\begin{align}
H_x = \sum_i m_i (y_i\dot{z}_i-z_i \dot{y_i}) = c_1 \\
H_y = \sum_i m_i (z_i\dot{x}_i-x_i \dot{z_i}) = c_2 \tag{w2.11} \\
H_z = \sum_i m_i (x_i\dot{y}_i-y_i \dot{x_i}) = c_3
\end{align}
$$

```ad-warning
Previously in this analysis, we have assumed that all considered masses are **point masses**. A point is a zero-dimensional object, and cannot rotate itself. Compare this to a planet, which has mass, but also some finite radius. If this planet were to rotate **around its own axis**, this would increase the total angular momentum of the system also. 

However, in this analysis, we only consider point masses which cannot rotate themselves, and so the **only** source of angular momentum from the system is from the motion of the masses around the barycenter. So useful as it may be, do not forget that this model is flawed, and merely a model.
```
___