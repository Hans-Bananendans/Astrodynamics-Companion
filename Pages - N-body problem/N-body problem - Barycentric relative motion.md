# N-body problem - Barycentric relative motion

```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25
```

After diving in to the integrals of motion, we discovered some important things. However, one of these things has gone as of yet unmentioned. Previously we described the system in terms of some fixed [[Newtonian Mechanics#Inertial reference frames|inertial reference frame]] somewhere near the N-body system. We now know that because any N-body system has constant linear momentum, the barycentre of the N-body system moves along a straight line with a constant velocity. 

![[IRF_vs_barycentric.png]]

But what this means that if we were to attach a reference frame to the barycentre, it would actually form an inertial reference frame with respect to the original inertial reference frame! This means that we could also describe the system in terms of an inertial reference frame stuck to the system barycentre, without having to introduce those pesky [[Newtonian Mechanics#Apparent forces|apparent forces]]. We refer to this as **motion relative to the barycentre**, and it will be the main topic of this section.

```ad-warning
The [[Wakker|Wakker book]] introduces a notation change at this point. We will use it here too, so you should be aware of it. Henceforth in this section, $\bar{r}_i$ will now refer to the position vector of mass $i$ **with respect to the barycentre**.
```
___
# Deriving the barycentric relative equation of motion

We can derive a very useful relation for the acceleration of particle $i$ as described relative to the barycentre. To start deriving it, we get out our trusty equation $\text{w2.3}$:

$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \tag{w2.3}$$

Since this reference frame is attached to the barycentre, it is also an inertial reference frame, which means that we don't get apparent forces, and we can use our [[N-body problem - Integrals of Motion|integrals of motion]]. As equation $\text{w2.3}$ is valid for any intertial reference frame, we can use it here too. We first divide out the mass $m_i$ on both sides:

$$\dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_j}{r^3_{ij}} \bar{r}_{ij} \tag{2}$$

If you remember, we can also write vector $\bar{r}_{ij}$ as:

$$\bar{r}_{ij} = \bar{r}_{j} - \bar{r}_{i}$$

We multiply with the mass $m_j$ sum for all bodies:

$$\sum_{j=1}^n m_j \bar{r}_{ij} = \sum_{j=1}^n m_j \bar{r}_{j} - \sum_{j=1}^n m_j \bar{r}_{i} $$

However, since we know that the vector from body $i$ to itself ($\bar{r}_{ii}$) is zero, we can slightly shrink the summation on the left-hand side:

$$\sum_{\substack{j=1 \\ j\neq i}}^n m_j \bar{r}_{ij} = \sum_{j=1}^n m_j \bar{r}_{j} - \sum_{j=1}^n m_j \bar{r}_{i} \tag{5}$$

Now if you remember that we're operating from the barycentre here, the vector pointing from the origin of the IRF and the barycentre should be of zero:
$$\bar{r}_{CM} = \dfrac{\sum_{j=1}^n m_j \bar{r}_j}{\sum_{j=1}^n m_j} = \bar{0}$$

If a fraction is zero, that means that it's nominator is zero, so:
$$\sum_{j=1}^n m_j \bar{r}_j =0 $$

So if we look back to equation $\text{5}$, we see that we can remove one of the terms, and the equation reduces to:

$$\sum_{\substack{j=1 \\ j\neq i}}^n m_j \bar{r}_{ij} = - \sum_{j=1}^n m_j \bar{r}_{i}$$

And then **A MIRACLE HAPPENS**, and we can write this as:

$$G\sum_{\substack{j=1 \\ j\neq i}}^n \dfrac{m_j}{r_i^3}\bar{r}_{ij} + G\sum_{j}^n \dfrac{m_j}{r_i^3}\bar{r}_{i} = 0 \tag{w2.20}$$

```ad-note
title: ## To do: Explain the miracle
icon: hammer
color: 240,200,25
```

Since these two terms together are zero, we can just add or subtract $\text{w2.20}$ from anything right? Well that's exactly what we are going to do. We subtract equation $\text{w2.20}$ from the right-hand side of equation $\text{2}$:

$$\dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{\substack{j=1 \\ j\neq i}}^n G \dfrac{m_j}{r^3_{ij}} \bar{r}_{ij} - \left( G\sum_{\substack{j=1 \\ j\neq i}}^n \dfrac{m_j}{r_i^3}\bar{r}_{ij} + G\sum_{j=1}^n \dfrac{m_j}{r_i^3}\bar{r}_{i} \right)$$
$$ = \sum_{\substack{j=1 \\ j\neq i}}^n G \dfrac{m_j}{r^3_{ij}} \bar{r}_{ij} -  G\sum_{\substack{j=1 \\ j\neq i}}^n \dfrac{m_j}{r_i^3}\bar{r}_{ij} - G\sum_{j=1}^n \dfrac{m_j}{r_i^3}\bar{r}_{i} $$

We can rewrite this to its final form, and along the way we define the total system mass $M = \sum_{j=1}^n m_j$:
$$
\begin{align}
\dfrac{d^2 \bar{r}_i}{dt^2} \hspace{2em} = \hspace{2em} 
- G\sum_{j=1}^n \dfrac{M}{r_i^3}\bar{r}_{i}
\hspace{2em} + \hspace{2em} 
G \sum_{\substack{j=1 \\ j\neq i}}^n m_j \left( \dfrac{1}{r^3_{ij}} -\dfrac{1}{r_i^3} \right) \bar{r}_{ij}  
\\
\hspace{0em} 
\begin{matrix} \text{barycentric} \\ \text{2-body motion} \end{matrix}
\hspace{6em} 
\begin{matrix} \text{attraction of other} \\ \text{bodies on } i \end{matrix}
\hspace{1em} 
\end{align}
\tag{w2.21}$$

This equation is kind of special, because it seperates out two interesting components. The first term on the right-hand side is the motion of body $i$ around the barycentre as though the barycentre was a body with mass $M$. The second term is the cumulative attraction of all the other bodies on body $i$, which disturb this nice, clean 2-body motion around the barycentre. 

Often, the second term is relatively small, but it can be very large in some cases, so it cannot be ignored.
___