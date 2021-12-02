# Derivation - N-body constant linear momentum
```ad-note
title: Note: A less detailed derivation can be found on page 26 of the [[Wakker|Wakker book]].
```

According to the [[N-body problem - Integrals of Motion#Derivation recipe|derivation recipe]], to start this derivation we want to sum equation $\text{w2.3}$ over all bodies $i$.  So we take equation $\text{w2.3}$:
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \tag{w2.3}$$
And sum both sides over all bodies $i$:
$$\sum_i m_i \dfrac{d^2 \bar{r}_i}{dt^2} = G \sum_i \sum_{j \neq i} \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij}$$
The book off-handedly mentions that the right-hand side of this equation is zero, and that this is obvious. It was by no means obvious to me, so here is a math block explaining why that is.

```ad-note
title: Why the right-hand side of that equation is indeed zero
icon: paperclip
collapse: close
color: 180,180,180

$$\text{Why is } G \sum_i \sum_{j \neq i} \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \text{ equal to 0?} \tag{r1}$$

First, let's write this properly, without omitting the properties of iterators $i$ and $j$. They both iterate from body $1$ to body $n$, so we write:

$$G \sum_{i=1}^n \sum_{\substack{ j=1 \\ j\neq i }}^n \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij}\tag{r2}$$

The secret of why $\text{r1}$ is zero is hidden in the vector $\bar{r}_{ij}$. Let's isolate this: We're going to perform the above summation, but we ignore every term except the term $\bar{r}_{ij}$:

$$\sum_{i=1}^n \sum_{\substack{ j=1 \\ j\neq i }}^n \bar{r}_{ij} \tag{r3}$$

Also, if equation $\text{r1}$ equation is equal to zero **in general**, it doesn't matter what $n$ we choose. Let's choose $n=3$, because this will make illustrating this a bit easier.

$$\sum_{i=1}^3 \sum_{\substack{ j=1 \\ j\neq i }}^3 \bar{r}_{ij} \tag{r4}$$

If you write out these terms, you get:

$$
\sum_{i=1}^3 \sum_{\substack{ j=1 \\ j\neq i }}^3 \bar{r}_{ij}
=
(\cancel{\bar{r}_{11}} + \bar{r}_{12} + \bar{r}_{13}) + (\bar{r}_{21} + \cancel{\bar{r}_{22}} + \bar{r}_{23}) + (\bar{r}_{31} + \bar{r}_{32} + \cancel{\bar{r}_{33}})
$$

$$ = \bar{r}_{12} + \bar{r}_{13} + \bar{r}_{21} + \bar{r}_{23} + \bar{r}_{31} + \bar{r}_{32} \tag{r5}$$

The vectors $\bar{r}$ that have two identical indices (e.g. $\bar{r}_{11}$) are crossed out because of the ($j\neq i$) in the inner summation. The figure below should give you a second reason as to why these vectors are crossed out; For example, the vector $\bar{r}_{11}$ corresponds to the distance from $m_1$ to $m_1$, but this distance is clearly zero, and its direction is undefined. 

Now, we've chosen $n=3$ because in our case the above equation comes up when considering a 3-body system. The figure below shows the vectors from equation $\text{r5}$:

![[rel_r.png]]

So if we apply the relations from the figure to equation $\text{r5}$, we get:
$$
\sum_{i=1}^3 \sum_{\substack{ j=1 \\ j\neq i }}^3 \bar{r}_{ij} = \bar{r}_{12} + \bar{r}_{13} + (-\bar{r}_{12}) + \bar{r}_{23} + (-\bar{r}_{13}) + (-\bar{r}_{32}) = 0 \tag{r6}$$

So this is our first indication that applying the double summation gives us terms that all cancel and become zero. However, if it works for equation $\text{r3}$, does it also work for $\text{r2}$? 

Let's write out equation $\text{r2}$ for $n=3$ in a similar manner:

$$G \sum_{i=1}^3 \sum_{\substack{ j=1 \\ j\neq i }}^3 \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} = G \left[ 
\left( \cancel{\dfrac{m_1 m_1}{r^3_{11}} \bar{r}_{11}} + \dfrac{m_1 m_2}{r^3_{12}} \bar{r}_{12} + \dfrac{m_1 m_3}{r^3_{13}} \bar{r}_{13}\right) \right. $$

$$\left. +
\left( \dfrac{m_2 m_1}{r^3_{21}} \bar{r}_{21} + \cancel{\dfrac{m_2 m_2}{r^3_{22}} \bar{r}_{22}} + \dfrac{m_2 m_3}{r^3_{23}} \bar{r}_{23}\right) +
\left( \dfrac{m_3 m_1}{r^3_{31}} \bar{r}_{31} + \dfrac{m_3 m_2}{r^3_{32}} \bar{r}_{32} + \cancel{\dfrac{m_3 m_3}{r^3_{33}} \bar{r}_{33}}\right)
\right]$$

$$= G \left[ 
\dfrac{m_1 m_2}{r^3_{12}} \bar{r}_{12} + 
\dfrac{m_1 m_3}{r^3_{13}} \bar{r}_{13} +
\dfrac{m_2 m_1}{r^3_{21}} \bar{r}_{21} + 
\dfrac{m_2 m_3}{r^3_{23}} \bar{r}_{23} +
\dfrac{m_3 m_1}{r^3_{31}} \bar{r}_{31} + 
\dfrac{m_3 m_2}{r^3_{32}} \bar{r}_{32} \right]
\tag{r7}$$

And because each pair of vectors in the figure above point in opposite direction, but their lengths are equal, we can write it like this:

$$ G \left[ 
\dfrac{m_1 m_2}{r^3_{12}} \bar{r}_{12} + 
\dfrac{m_1 m_3}{r^3_{13}} \bar{r}_{13} +
\left( -\dfrac{m_2 m_1}{r^3_{12}} \bar{r}_{12} \right) + 
\dfrac{m_2 m_3}{r^3_{23}} \bar{r}_{23} +
\left( -\dfrac{m_3 m_1}{r^3_{13}} \bar{r}_{13} \right) + 
\left( -\dfrac{m_3 m_2}{r^3_{23}} \bar{r}_{23} \right) 
\right]$$

$$ = G\cdot [0] = 0 \tag{r8}$$

While not a formal mathematical proof, it should illustrate to you why it is that in general it is true that:
$$G \sum_i \sum_{j \neq i} \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} = 0$$
Because of the nature of the N-body problem, you end up with vectors $\bar{r}$ which are all cancelling pairs, and so the result of this particular double summation will indeed be zero. How obvious, mr. Wakker, how obvious...
```

Anyway, when the right-hand side of an equation is equal to zero, this means that the left-hand side is also equal to zero. So we can write:
$$\sum_i m_i \dfrac{d^2 \bar{r}_i}{dt^2} = 0 $$

What we do now is bring the term $\sum_i m_i$ into the double derivative. We can only do this without hassle if we assume that the mass of each body remains constant. 
```ad-warning
title: Assumption: Each body has constant mass: $\; \dfrac{dm_i}{dt} = 0$
color: 200,80,225
```
So we get:
$$\sum_i m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \dfrac{d^2}{dt^2} \left( \sum_i \bar{r}_i m_i\right) = 0 \tag{w2.5}$$

Now we integrate **once**, and we find: 
$$\sum_i m_i \dfrac{d \bar{r}_i}{dt} = \bar{c} $$

Where $\bar{c}$ is just some vectorial integration constant. Now if you remember [[Newtonian Mechanics#Newton's second law|Newton's second law]], you may recognise that the term $m_i \cdot d{r}_i/dt$ is actually the definition of linear momentum for a particle with constant mass. So what the equation above tells us is that **the sum total of the linear momentum of each body in the system** is **constant**. 

If we take the integrated form of equation $\text{w2.5}$ and split it up in the three Cartesian components, we end up with **the first three integrals of motion**:

$$
\sum_{i=1}^n m_i \dfrac{dx_i}{dt} = c_1 \hspace{3em}
\sum_{i=1}^n m_i \dfrac{dy_i}{dt} = c_2 \hspace{3em}
\sum_{i=1}^n m_i \dfrac{dz_i}{dt} = c_3 \tag{w2.6}
$$

You may be aware of the definition of the barycentre (also known as the centre of mass) of a set of masses:
$$\bar{r}_{cm} = \dfrac{\sum_{i} m_i \bar{r}_i}{\sum_{i} m_i }$$

You can combine this with equation $\text{w2.5}$ to find that:
$$\bar{r}_{cm} = \bar{a}t+\bar{b}$$

```ad-note
title: Math
icon: paperclip
collapse: closed
color: 180,180,180

Start with
$$\bar{r}_{cm} = \dfrac{\sum_{i} m_i \bar{r}_i}{\sum_{i} m_i } \tag{r1}$$
and
$$
\sum_i m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \dfrac{d^2}{dt^2} \left( \sum_i \bar{r}_i m_i\right) = 0 \tag{r2}
$$

Rewrite the equation for the barycenter:
$$\sum_{i} m_i \bar{r}_{cm} = \sum_{i} m_i \bar{r}_i \tag{r3}$$
Differentiate twice with respect to time:
$$\dfrac{d^2}{dt^2} \left( \sum_{i} m_i \bar{r}_{cm} \right)= \dfrac{d^2}{dt^2} \left( \sum_{i} m_i \bar{r}_i \right) \tag{r4}$$
Substitute $\text{r2}$ into $\text{r4}$:
$$\dfrac{d^2}{dt^2} \left( \sum_{i} m_i \bar{r}_{cm} \right)= 0\tag{r5}$$

Since mass is constant, it is not affected by the differentiation or integration with respect to time. Therefore we can find that (integrating once):

$$\dfrac{d}{dt} \left( \bar{r}_{cm} \right) = \bar{a}\tag{r6}$$

And also (integrating again):

$$\bar{r}_{cm} = \bar{a}t+\bar{b}\tag{r7}$$

Where $\bar{a}$ and $\bar{b}$ are simple vectorial constants.
```
In other words, the barycentre of any moves in a straight line. Splitting this up into three Cartesian components gives us the next three integrals of motion:

$$
x_{cm} = a_1 t + b_1 \hspace{3em}
y_{cm} = a_2 t + b_2 \hspace{3em}
z_{cm} = a_3 t + b_3 \tag{w2.8}
$$

So the conclusion here is that any N-body system has a constant amount of linear momentum. This means that since the total mass does not change, the velocity with which the whole system travels is constant. So if you were an outsider looking at such a system, you could consider the barycentre of the system and find it travelling along at some constant velocity. 
___