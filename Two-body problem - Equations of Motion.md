# Two-body problem - Equations of Motion

This section forms the start of a foray into the properties of the two body problem. Even though in reality you almost never deal with a system that is influenced by merely two bodies, it is often the case that you can reliably simplify some $N$-body system to a two-body system, where the influence of the other $N-2$ bodies are neglected. 

For example, when designing an orbital transfer from Earth to the moon, as a first order approximation you can neglect the influence of all the other planets, as well as the sun. This collapses an N-body problem into a simple two-body problem, which [[The N-body problem#Introduction|as we've seen before]] means that you can now describe it with a closed-form expression. On our journey through the properties of the two-body problem we will make use of this, and amass a [[Two-body Roadmap|useful collection of equations]] that can help us design simple orbital trajectories.

You will find that the focus of this journey is the case where one of the two bodies is much smaller than the other, because this corresponds to for example a spacecraft orbiting a larger planetary body. So you will see that we very quickly make the assumption that one mass is much larger than the other.

___

## Starting point
So where do we start? It's quite simple: we start with the framework of [[N-body relative motion#Equations of motion|relative motion in an N-body system]], and just cut out the effects of all bodies except two. Specifically, we can start at equation $\text{w4.4}$:
$$\dfrac{d^2 \bar{r}_{ki}}{dt^2} = - G \dfrac{m_i + m_k}{r_{ki}^3}\bar{r}_{ki}  + G \sum_{j \neq i,k} m_j \left( \dfrac{\bar{r}_{kj} - \bar{r}_{ki}}{r_{ij}^3} -  \dfrac{\bar{r}_{kj} }{r_{ij}^3}\right) \tag{w4.4}$$

And then remove the effects of all bodies $j$, so we only consider bodies $i$ and $k$:
$$\dfrac{d^2 \bar{r}_{ki}}{dt^2} = - G \dfrac{m_i + m_k}{r_{ki}^3}\bar{r}_{ki} \tag{w5.1-1}$$
Remember that we are talking about relative motion here, and so the index $ki$ indicates that the motion of body $i$ is described relative to a non-rotating reference frame with body $k$ as origin. 

We can also write the following equation, in which we omit the subscript $ki$, but remember that we're describing everything relative to mass $k$:
$$\dfrac{d^2 \bar{r}}{dt^2} = - \dfrac{\mu}{r^3}\bar{r} \tag{w5.3}$$

This is just a different way of writing the previous equation, but we tend to use it more frequently. Remember that $\mu$ is the **gravitational parameter**, which is formally defined as:

$$\mu = G m_k \left( 1 + \dfrac{m_i}{m_k}\right) \tag{w5.2-1}$$

As mentioned before, we wish to focus on cases where one of the masses is much smaller than the other mass, i.e. $m_i << m_k$. This will help simplify the equations for many cases that are interesting to space engineering, namely the motion of a small vehicle with respect to a large planetary mass.

```ad-warning
title: Assumption: $m_i << m_k$
color: 200,80,225
```

This allows us to write the gravitational parameter as:
$$\mu \approx G m_k \left( 1 + 0\right) = Gm_k\tag{w5.4}$$

With these equations as starting point, we can derive some very useful conservation laws.
___

## Conservation laws
The two conservation laws that we will derive in this section are general properties of any two-body system, which means that you can always apply them[^1]. The first of these conservation laws is known as the [[Vis-viva Equation|vis-viva equation]], a stupendously useful equation that we will use **a lot**, and the other one is known as Kepler's Second Law.

[^1]: Given that the two masses are point masses (uniform mass distributions, unable to store rotational momentum, etc), relativistic effects are ignored, etc.

### Deriving the vis-viva equation
To derive the vis-viva equation, we do something very similar to the time when we derived the [[Derivation - N-body constant total energy|the constant energy property]] of an N-body system. We take equation $\text{w5.3}$ and take the scalar product of $d\bar{r}/dt$ and it:
$$\dfrac{d\bar{r}}{dt} \cdot \left( \dfrac{d^2 \bar{r}}{dt^2} \right) = - \dfrac{\mu}{r^3}\bar{r}\cdot \dfrac{d\bar{r}}{dt} $$
$$\dfrac{d\bar{r}}{dt} \cdot \left( \dfrac{d^2 \bar{r}}{dt^2} \right) + \dfrac{\mu}{r^3}\bar{r}\cdot \dfrac{d\bar{r}}{dt} = 0$$

The two terms of this equation we can rewrite by virtue of the chain rule, similar to what we did [[Derivation - N-body constant total energy#Manipulating the left-hand side|when we derived the constant energy property]] [^2]. We then get:

$$\dfrac{1}{2} \dfrac{d}{dt} \left( \dfrac{d \bar{r}}{dt} \cdot \dfrac{d \bar{r}}{dt} \right) + \dfrac{1}{2} \dfrac{\mu}{r^3}  \dfrac{d}{dt} \left( \bar{r} \cdot \bar{r} \right) = 0$$

[^2]: Apply the following equation to both terms: $$\dfrac{d}{dt} \left( \dfrac{1}{2}y^2 \right) = y \cdot \dfrac{dy}{dt}$$

If we apply [[Vector Identities#Vector identity 1|vector identity 1]], we can simply write the bracketed term as 1/2 times the derivative of $(dr/dt)^2$, which is simply the velocity squared. In the second term, we can do the same for vector $\bar{r}$, reducing the above to:

$$\dfrac{1}{2} \dfrac{d}{dt} \left( V^2 \right) + \dfrac{1}{2} \dfrac{\mu}{r^3}  \dfrac{d}{dt} \left( r^2 \right) = 0$$

$$\dfrac{1}{2} \dfrac{d}{dt} \left( V^2 \right) - \dfrac{d}{dt} \left( \dfrac{\mu}{r}  \right) = 0$$
```ad-note
title: ## To do: Explain what happened to the second term in this step!
icon: hammer
color: 240,200,25
```

Now we can simply integrate, and call the integration constant $\mathcal{E}$:

$$\dfrac{1}{2} V^2 - \dfrac{\mu}{r}  = \mathcal{E}$$

This equation is known as the [[Vis-viva Equation|vis-viva equation]]. In essence, this equation tells us that the internal energy of any two-body system consists of kinetic energy (first term) and potential energy (second term), and that the total amount is some constant value $\mathcal{E}$.

This equation will be very useful going forward. Its main strength lies in the fact that we can pretty much always apply it, no matter whether we are considering circular orbits, elliptical orbits, hyperbolic orbits, etc. 

```ad-tip
title: Tip
icon: lightbulb

If you're going to learn one equation by heart for the exam, it should be this one. If you're stuck at a particular two-body related exam question, **always** check if you can apply the vis-viva equation to find one of the missing parameters. This will often be the case, so this is always worth doing. 

It can also be used to verify your answer, by checking whether the internal energy of the system has the correct sign for the orbit type. More on that later. The main point is that the vis-viva equation will [never let you down](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

```


### Deriving Kepler's Second Law
