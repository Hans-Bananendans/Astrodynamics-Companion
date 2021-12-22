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

This turns our two-body problem into the so-called **restricted two-body problem**, because we assume that $\mu$ is only dependant on the mass of the more massive body. We weaken the applicability of the theory by doing this, because we won't be able to use our equations to calculate the motion of a [binary star system](https://en.wikipedia.org/wiki/Binary_star#Astrophysics), where the two stars have comparable masses, and the aforementioned assumption is clearly no longer valid. But it turns out that the restricted two-body problem has many uses for space engineering and mission design.

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
To derive Kepler's second law we take a similar approach to how you [[Derivation - N-body constant angular momentum|derive the constant angular momentum property]] of an N-body system. We start by taking the cross product of $\bar{r}$ and $\text{w5.3}$:

$$\bar{r} \times \dfrac{d^2\bar{r}}{dt^2} + \dfrac{\mu}{r^3} \cancel{\bar{r} \times \bar{r}}^{\;=\:0} = 0$$

Given [[Vector Identities#Vector identity 4|vector identity 4]], we know that any vector crossed with itself equals zero. This means that the second term nullifies and we are only left with the first term:

$$\bar{r} \times \dfrac{d^2\bar{r}}{dt^2} = 0$$

It turns out we can also write this like so:
$$\dfrac{d}{dt}\left( \bar{r} \times \dot{\bar{r}}\right) = 0$$

```ad-note
title: How is this possible?
icon: paperclip
collapse: closed
color: 180,180,180

Why are we allowed to write that
$$\bar{r} \times \dfrac{d^2\bar{r}}{dt^2} \tag{r1}$$
is equivalent to
$$\dfrac{d}{dt}\left( \bar{r} \times \dot{\bar{r}}\right) \tag{r2}$$

The answer is that we have actually applied the product rule but in reverse. Let's pretend we want to perform the derivation in $\text{r2}$. To do it, we would apply the product rule, right?

$$\dfrac{d}{dt}\left( \bar{r} \times \dot{\bar{r}}\right) = \dot{\bar{r}} \times \dot{\bar{r}} + \bar{r} \times \ddot{\bar{r}} \tag{r3}$$

By virtue of [[Vector Identities#Vector identity 4|vector identity 4]], the middle term equals zero:
$$\dfrac{d}{dt}\left( \bar{r} \times \dot{\bar{r}}\right) = \cancel{\dot{\bar{r}} \times \dot{\bar{r}}}^{\;=\:0} + \bar{r} \times \ddot{\bar{r}} \tag{r4}$$
$$\dfrac{d}{dt}\left( \bar{r} \times \dot{\bar{r}}\right) =  \bar{r} \times \ddot{\bar{r}} \tag{r5}$$
or
$$\dfrac{d}{dt}\left( \bar{r} \times \dot{\bar{r}}\right) = \bar{r} \times \dfrac{d^2\bar{r}}{dt^2} \tag{r6}$$



```

The first time derivative of $\bar{r}$ is simply the velocity $\bar{V}$, which we can substitute instead:

$$\dfrac{d}{dt}\left( \bar{r} \times \bar{V}\right) = 0$$

If we were to integrate both sides, the zero on the right-hand side simply becomes a constant. This constant is the **relative angular momentum** $\bar{h}$. And so we get:

$$\bar{h} = \bar{r} \times \bar{V} \tag{w5.6}$$

```ad-warning
title: Angular momentum vs. specific angular momentum

There is a source of confusion here that should be cleared up. In the astrodynamics, there are generally two flavours of angular momentum:
1. The (classic) angular momentum, which is defined as:
$$\bar{H} = \bar{r} \times m \bar{V}$$
2. The **specific** angular momentum, which is the same as the classic angular momentum but **normalized for the mass**:
$$\bar{h} = \dfrac{\bar{H}}{m} = \bar{r} \times \bar{V}$$

We will frequently use the second definition, but the [[Wakker]] book uses $\bar{H}$ for **both types of momentum**, and just assumes that you can figure out yourself which one to use. I think this is needlessly confusing, and therefore throughout this whole companion, I will follow professor Cowan's convention, which uses the symbols as defined above; $\bar{H}$ denotes the (classic) angular momentum, whereas $\bar{h}$ denotes the **specific** angular momentum.
```

We have now in essence proven that the specific angular momentum for a restricted two-body system is constant. Of course [[Derivation - N-body constant angular momentum|we already knew that]], given that this is so for any N-body system. 

To get to Kepler's second law, we're now going to split up the velocity vector $\bar{V}$ into a tangential component $\bar{V}_{\theta}$ and a radial component $\bar{V}_{r}$, as depicted below:
![[velocity_components.png]]
This we're going to substitute into $\text{w5.6}$:

$$\bar{h} = \bar{r} \times \bar{V}$$
$$ = \bar{r} \times (\bar{V_r}+\bar{V}_{\theta})$$
$$ = \cancel{\bar{r} \times \bar{V_r}}^{\:=\:0} + \bar{r} \times \bar{V}_{\theta}$$

If you look at the figure above, you'll see that vectors $\bar{r}$ and $\bar{V}_{r}$ are parallel, and so their cross product will be zero by definition. So we are left with the following:
$$\bar{h} = \bar{r} \times \bar{V}_{\theta}$$

We can collapse this vectorial function into a scalar function by noting from the figure above that the magnitude of $\bar{V}_{\theta}$ is equal to $r \dot{\theta}$. Given that we have already proven that the specific angular momentum of this system is zero, we get:
$$h = r (r \dot{\theta}) = r^2 \dot{\theta} = \text{constant}\tag{w5.7}$$

If you look at the figure again, you'll see that the motion of vector $\bar{r}$ over angle $\theta$ sweeps a certain area $A$. Let's consider this area, but instead let's take a very small angle $\theta$, so that the area $A$ resembles a triangle:
![[kepler2_triangle.png]]
The area $A$ of this triangle equals:
$$A = \dfrac{1}{2} r^2 \cos(\theta) \sin(\theta)$$
If we make theta infinitesimally small ($d\theta \rightarrow 0$), the area $dA$ becomes:
$$dA = \dfrac{1}{2} r^2 \cos(d\theta) \cancel{\sin(d\theta)}^{\:\approx\:0}$$
The sine of a very small angle is approximately 0, and the cosine of a very small angle is approximately equal to the angle, so we get:
$$dA \approx \dfrac{1}{2} r^2 d\theta$$

If we differentiate this equation with respect to time, we find that the change in area with respect to time is:
$$\dfrac{dA}{dt} = \dfrac{1}{2} r^2 \dfrac{d\theta}{dt} = \dfrac{1}{2} r^2 \dot{\theta}$$

Now if we substitute equation $\text{w5.7}$ in here, we get:
$$\dfrac{dA}{dt} = \dfrac{1}{2} r^2 \dfrac{d\theta}{dt} = \dfrac{1}{2} h = \text{constant}$$
This is **Kepler's second law**, and it essentially remarks that when a satellite moves around a large body over a certain period $dt$, its position vector will sweep the same area no matter where you are in the orbit. For definitions like this, it's always easier to have a picture, so here you have one:
![[kepler2.png]]
More animations and visualizations can be found [here](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion#Second_law) and [here](https://ophysics.com/f6.html).
___