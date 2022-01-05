# N-body relative motion

```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25
To do:
 - [ ] Add derivation of Sphere of Influence 
```

<!-- This covers sections 4.1-4.3 from [Wakker] -->
In chapter 2 of the [[Wakker|Wakker book]], we dealt with the N-body problem and set up the equations of motions. However, those equations of motion were usually defined in terms of some arbitrary [[Newtonian Mechanics#Inertial reference frames|inertial reference frame]] or the inertial reference frame at the barycentre of the system.

However, in reality you will hardly ever be interested in how all the bodies of an N-body system move in respect to a barycentre, but in how one particular body moves with respect to another. For example, how the moon rotates around the Earth in the many-body system of the solar system. Or, how a martian satellite mission orbits Mars (maybe in the presence of some moons). In such cases, we are interested in **relative motion**, motion in which the reference frames are often no longer inertial reference frames. This means that we cannot use the equations of motion that we derived previously, but have to make new ones.

```ad-warning
title: Warning! How not to look stupid on the exam:

Be sure to understand _when_ you are dealing with relative motion, and _which_ equations you can and cannot use in that case. If you're trying to describe relative motion in general, but you use the equations that are only valid when working with inertial reference frames, you're almost certainly going to arrive at a wrong answer on the exam.

So this guy:
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \tag{w2.3}$$

or this guy:
$$\dfrac{d^2 \bar{r}_i}{dt^2} =
- G \dfrac{M}{r_i^3}\bar{r}_{i} +
G \sum_{ j\neq i} m_j \left( \dfrac{1}{r^3_{ij}} -\dfrac{1}{r_i^3} \right) \bar{r}_{ij}  \tag{w2.21}$$

Just throw those into the garbage for now. **Do not use them for relative motion**.

```
___
## Equations of motion
<!-- [Wakker] section 4.1 -->
Fine then, how do we get started with making new equations of motion that are valid for relative motion? Well, let's just start with what we know: an N-body system with an inertial reference frame $XYZ$, as depicted.

![[relative_motion1.png|Figure 1: Points i, j, and k described from the origin of XYZ]]

We're going to describe the motion of bodies $i$ and $k$ with respect to this inertial reference frame $XYZ$. There may also be any number of other bodies $j$ in the system. We're not going to describe the motion of those here, but we will include their effect on $i$ and $k$. Using equation $\text{w2.3}$, we get:
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r_{ij}^3}\bar{r}_{ij} \tag{w4.1-1}$$
$$m_k \dfrac{d^2 \bar{r}_k}{dt^2} = \sum_{j \neq k} G \dfrac{m_k m_j}{r_{ij}^3}\bar{r}_{kj} \tag{w4.1-2}$$
Just to be clear, this motion is described with respect to the origin of $XYZ$. It turns out that we can write these equations slightly differently by extracting out one of the terms of the summation. For equation $\text{w4.1-1}$, we do this by extracting the term corresponding to body $k$, and for equation $\text{w4.1-2}$, we extract the term corresponding to body $i$:
$$\dfrac{d^2 \bar{r}_i}{dt^2} = G \dfrac{m_k}{r_{ik}^3}\bar{r}_{ik} + \sum_{j \neq i,k} G \dfrac{m_j}{r_{ij}^3}\bar{r}_{ij} \tag{w4.2-1}$$
$$\dfrac{d^2 \bar{r}_k}{dt^2} = G \dfrac{m_i}{r_{ki}^3}\bar{r}_{ki} + \sum_{j \neq i,k} G \dfrac{m_j}{r_{kj}^3}\bar{r}_{kj} \tag{w4.2-2}$$

You may also have noticed that we divided by $m_i$ and $m_k$ respectively, just to keep things orderly. Now, have a look at the figure again, and verify that the following vectorial relations all hold:
$$
\bar{r}_{ik} = -\bar{r}_{ki} 
\hspace{2em}
\bar{r}_{ki} = \bar{r}_i - \bar{r}_k
\hspace{2em}
\bar{r}_{kj} - \bar{r}_{ki} = \bar{r}_j - \bar{r}_k - (\bar{r}_i - \bar{r}_k) = \bar{r}_j - \bar{r}_i = \bar{r}_{ij} \tag{w4.3}
$$

Now we are going to subtract $\text{w4.2-2}$ from $\text{w4.2-1}$ and use the vectorial relations $\text{w4.3}$ to clean things up:

$$\dfrac{d^2 \bar{r}_i}{dt^2} - \dfrac{d^2 \bar{r}_k}{dt^2}= G \dfrac{m_k}{r_{ik}^3}\bar{r}_{ik} + \sum_{j \neq i,k} G \dfrac{m_j}{r_{ij}^3}\bar{r}_{ij} - \left( G \dfrac{m_i}{r_{ki}^3}\bar{r}_{ki} + \sum_{j \neq i,k} G \dfrac{m_j}{r_{ij}^3}\bar{r}_{kj} \right)$$

$$\dfrac{d^2 \bar{r}_{ki}}{dt^2} = G \dfrac{m_k}{r_{ik}^3}\bar{r}_{ik} - G \dfrac{m_i}{r_{ki}^3}\bar{r}_{ki} + \sum_{j \neq i,k} G \dfrac{m_j}{r_{ij}^3}\bar{r}_{ij} - \sum_{j \neq i,k} G \dfrac{m_j}{r_{ij}^3}\bar{r}_{kj} $$

$$\dfrac{d^2 \bar{r}_{ki}}{dt^2} = - G \dfrac{m_k}{r_{ki}^3}\bar{r}_{ki} - G \dfrac{m_i}{r_{ki}^3}\bar{r}_{ki} + \sum_{j \neq i,k} G \dfrac{m_j}{r_{ij}^3}\bar{r}_{ij} - \sum_{j \neq i,k} G \dfrac{m_j}{r_{ij}^3}\bar{r}_{kj} $$

$$\dfrac{d^2 \bar{r}_{ki}}{dt^2} = - G \dfrac{m_i + m_k}{r_{ki}^3}\bar{r}_{ki}  + G \sum_{j \neq i,k} m_j \left( \dfrac{\bar{r}_{ij}}{r_{ij}^3} -  \dfrac{\bar{r}_{kj} }{r_{ij}^3}\right)$$

$$\dfrac{d^2 \bar{r}_{ki}}{dt^2} = - G \dfrac{m_i + m_k}{r_{ki}^3}\bar{r}_{ki}  + G \sum_{j \neq i,k} m_j \left( \dfrac{\bar{r}_{kj} - \bar{r}_{ki}}{r_{ij}^3} -  \dfrac{\bar{r}_{kj} }{r_{ij}^3}\right) \tag{w4.4}$$

Now, this may look like a bunch of busywork, but what have we achieved here? Well, we have an equation with on one hand the acceleration of body $i$ **with body $k$ as reference point**, and on the other side of the equation we have two terms, both of which look pretty similar to equation $\text{w2.21}$, the equation for barycentric relative motion. Note that **all vectors $\bar{r}$ have body $k$ as reference point**!

In other words, $\text{w4.4}$ is an equation of motion for body $i$, but **relative** to body $k$, and **not** the origin of $XYZ$. It is as though we put a reference frame at body $k$, although that would obviously be a non-inertial reference frame, since body $k$ is almost certainly not making a nice rectilinear motion with respect to the origin of $XYZ$.

```ad-warning
title: Warning!

At this point K.F. Wakker drops some subscripts in [[Wakker|the book]]. He reasons: since we have written equation $\text{w4.4}$ fully with $k$ as reference point, we may as well drop the redundant subscripts $k$ henceforth, as long as we remember that we are operating from a reference frame at $k$. 

I have decided to follow Wakker's notation in this summary, because although it may take a while for you to get used to the notation, it will avoid confusion when reading this summary alongside the [[Wakker|Wakker book]].

With the change in notation, equation $\text{w4.4}$ now looks like:
$$\dfrac{d^2 \bar{r}_{i}}{dt^2} = - G \dfrac{m_i + m_k}{r_{i}^3}\bar{r}_{i}  + G \sum_{j \neq i,k} m_j \left( \dfrac{\bar{r}_{j} - \bar{r}_{i}}{r_{ij}^3} -  \dfrac{\bar{r}_{j} }{r_{ij}^3}\right) \tag{w4.4}$$

```

I have redrawn the Figure 1 to illustrate the change in notation. All the vectors are now redefined to originate from $k$, even if this is not explicitly reflected in the subscripts.
![[relative_motion2.png|Figure 2: Points i and j described with respect to k]]

Let's take a closer look at equation $\text{w4.4}$. It turns out that, much like equation $\text{w2.21}$, we can split it up into two terms. The first term corresponds to a two body term, solely dependent on bodies $i$ and $k$. In the book, this is also referred to as the **primary** term. The second term is caused by the effect of all other bodies $j$ on body $i$. As such, they can be said to be "disturbing" or "perturbing" the motion caused by the primary term, and therefore this term is often called the **disturbing** term.
$$
\begin{align}
\dfrac{d^2 \bar{r}_{i}}{dt^2} \hspace{1em} = \hspace{1em} - G \dfrac{m_i + m_k}{r_{i}^3}\bar{r}_{i} \hspace{2.5em} + \hspace{2.5em} G \sum_{j \neq i,k} m_j \left(\dfrac{\bar{r}_{j} - \bar{r}_{i}}{r_{ij}^3} -  \dfrac{\bar{r}_{j} }{r_{ij}^3}\right) \tag{w4.4}
\\
\hspace{0em} 
\text{primary motion}
\hspace{8em} 
\text{disturbing motion}
\hspace{2em} 
\end{align}
$$


In conclusion, with this knowledge, we can describe bodies in an N-body system from any reference point we like. For example, we could describe the motion of an interplanetary probe on its way through the solar system with the Earth as reference point, rather than the sun. In practice, there are many other reasons to describe motion relatively rather than absolutely, especially in situations where relativity effects can no longer be ignored. See page 106 of the [[Wakker|Wakker book]] for more details about this.

___
## 	Relative perturbing acceleration of the Earth and of an Earth satellites
<!-- [Wakker] section 4.2-->

```ad-note
title: Note: In this section, [[Wakker]] sometimes uses $a_m$ for the mass of the primary body. I instead use $a_k$ for internal consistency.
```

In this section, we dive deeper into perturbed motion. As a model, we will consider a satellite labelled $i$ in an orbit around the Earth (labelled $k$). We center our reference frame at the center of the Earth. Imagine that we also consider the Sun, which will be the perturbing body $d$. Let's see what kinds of accelerations this satellite experiences as a result of this situation.

You can see the situation in the figure below. Note that the angle between $\bar{r}_i$ and $\bar{r}_{id}$ is **not** necessarily $90^\circ$.

![[perturbation1.png]]

Using equation $\text{w4.4}$, we can calculate the acceleration both of the primary motion around $k$, as well as the acceleration of the perturbation of $d$. 
```ad-warning
title: Assumption: Spacecraft mass is negligible
color: 200,80,225
Let's make the assumtion that the spacecraft mass is much smaller than the mass of the Earth and the Sun, and can be neglected during this analysis:
$$m_i << m_k, m_d \quad \rightarrow \quad m_i \approx 0$$

```

For the acceleration of the primary body we have according to $\text{w4.4}$:

$$\bar{a}_k = - G \dfrac{m_i + m_k}{r_{i}^3}\bar{r}_{i} \approx - G \dfrac{m_k}{r_{i}^3}\bar{r}_{i}$$

Or, as long as we remember that $\bar{a}_k$ points in the opposite direction of $\bar{r}_i$, the magnitude of the acceleration is:

$$a_k = G \dfrac{m_k}{r_{i}^2} \tag{w4.9}$$

The perturbing acceleration we can also get from equation $\text{w4.4}$:
$$a_d = G m_d \sqrt{\dfrac{1}{r_{id}^4} + \dfrac{1}{r_{d}^4} - \dfrac{2 \cos{\beta}}{r_{id}^2 r_{d}^2}} \tag{w4.10}$$

```ad-note
title: Math
icon: paperclip
collapse: closed
color: 180,180,180

To find the perturbing acceleration, we look at the second term of equation $\text{w4.4}$, and modify it for the given situation. Since we have only one disturbing body, the summation is just one term.

$$ \bar{a}_d = G m_d  \left( \dfrac{\bar{r}_{d} - \bar{r}_{i}}{r_{id}^3} -  \dfrac{\bar{r}_{d} }{r_{id}^3}\right) \tag{r1}$$

Nice, but we would actually like to have a scalar form of this equation, rather than a vectorial form. This will allow us to compare the magnitude $a_d$ with $a_k$. So we simplify equation $\text{r1}$ by first substituting $\bar{r}_{id} = \bar{r}_d - \bar{r}_i$ and performing a little trick: Squaring the bracketed term, while at the same time taking the square root of it:
$$ \bar{a}_d = G  \left( \dfrac{\bar{r}_{id}}{r_{id}^3} -  \dfrac{\bar{r}_{d} }{r_{id}^3}\right) = G m_d \sqrt{\left( \dfrac{\bar{r}_{id}}{r_{id}^3} -  \dfrac{\bar{r}_{d} }{r_{id}^3}\right) \cdot \left( \dfrac{\bar{r}_{id}}{r_{id}^3} -  \dfrac{\bar{r}_{d} }{r_{id}^3}\right)} \tag{r2}$$

$$  = G m_d \sqrt{ \dfrac{\bar{r}_{id} \cdot \bar{r}_{id}}{r_{id}^6} + \dfrac{\bar{r}_{d} \cdot \bar{r}_{d} }{r_{id}^6} - 2 \dfrac{\bar{r}_d \cdot \bar{r}_{id}}{r_d^3 r_{id}^3}} \tag{r3}$$

Given [[Vector Identities#Vector identity 1|Vector identity 1]] and the definition of the [dot product](https://en.wikipedia.org/wiki/Dot_product), we can rewrite this to:

$$  = G m_d \sqrt{ \dfrac{r_{id}^2}{r_{id}^6} + \dfrac{r_{d}^2}{r_{id}^6} - 2 \dfrac{r_d r_{id} \cos\beta}{r_d^3 r_{id}^3}} = G m_d \sqrt{ \dfrac{1}{r_{id}^4} + \dfrac{1}{r_{id}^4} - \dfrac{2 \cos\beta}{r_d^2 r_{id}^2}} \tag{r4}$$

where $\beta$ is the angle between $\bar{r}_d^3$ and $\bar{r}_{id}^3$. At this point we have eliminated every vector, and we may write $\bar{a}_d$ as $a_d$:

$$ a_d = G m_d \sqrt{ \dfrac{1}{r_{id}^4} + \dfrac{1}{r_{id}^4} - \dfrac{2 \cos\beta}{r_d^2 r_{id}^2}} \tag{r5}$$

```

### The influence of $\alpha$ and $\gamma$ on $a_d$
It turns out that we can derive a grotesque but quite useful equation. This equation will describe the perturbing acceleration $a_d$ as a function of the distance ratio of the primary and disturbing body, and of the angle $\alpha$. To derive this equation, we will need two geometric compatibilities.

![[perturbation2.png]]
First, take a look at the cyan triangle in the figure above. Using the definition of the [cosine](https://en.wikipedia.org/wiki/Sine_and_cosine), we can write that:
$$\cos{\beta} = \dfrac{r_d - r_i \cos{\alpha}}{r_{id}}$$

Also, by virtue of the [law of cosines](https://en.wikipedia.org/wiki/Law_of_cosines) we can write:
$$r_{id}^2 = r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha$$
This is of course true for any triangle, so this is still valid even if we start changing angle $\alpha$.

If we substitute these two geometric compatibilities into equation $\text{w4.10}$ and spend an unhealthy amount of time manipulating it, we arrive at:
$$a_d = G \dfrac{m_d}{r_d^2} 
\sqrt{
1 +
\dfrac{1}{[1+\gamma^2 - 2 \gamma \cos(\alpha)]^2} -
\dfrac{2(1-\gamma \cos(\alpha))}{[1+\gamma^2 - 2 \gamma \cos(\alpha)]^{3/2}}
}  
\tag{w4.11}$$

In this equation, we have introduced a quantity $\gamma$, which is the aforementioned distance ratio:
$$\gamma = \dfrac{r_i}{r_d}$$

```ad-note
title: Math
icon: paperclip
collapse: closed
color: 180,180,180

Start with:

$$a_d = G m_d \sqrt{\dfrac{1}{r_{id}^4} + \dfrac{1}{r_{d}^4} - \dfrac{2 \cos{\beta}}{r_{id}^2 r_{d}^2}} \tag{w4.10}$$

and 

$$
\gamma = r_i / r_d
\hspace{2em} , \hspace{2em} 
\cos{\beta} = \dfrac{r_d - r_i \cos{\alpha}}{r_{id}} 
\hspace{2em} , \hspace{2em} 
r_{id}^2 = r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha \tag{r1}$$

Simply substitute the equations $\text{r1}$ into $\text{w4.10}$:

$$a_d = G m_d \sqrt{\dfrac{1}{r_{id}^4} + \dfrac{1}{r_{d}^4} - \dfrac{2 (r_d - r_i \cos{\alpha})}{r_{id}^3 r_{d}^2}} \tag{r2}$$


$$ = G m_d \sqrt{\dfrac{1}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2} + \dfrac{1}{r_{d}^4} - \dfrac{2 (r_d - r_i \cos{\alpha})}{r_{d}^2 [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}} \tag{r3}$$

For our first trick, we will multiply everything inside the square root by $r_{d}^4$ divided by itself. The numerator we will use to manipulate the fractions, whilst the denominator we will extract from the square root:
$$ a_d = G m_d \sqrt{ \dfrac{r_{d}^4}{r_{d}^4} \left\{ \dfrac{1}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2} + \dfrac{1}{r_{d}^4} - \dfrac{2 (r_d - r_i \cos{\alpha})}{r_{d}^2 [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}} \right\} }  \tag{r4}$$

$$ = G \dfrac{m_d}{r_{d}^2} \sqrt{  \dfrac{r_{d}^4}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2} + 
\dfrac{r_{d}^4}{r_{d}^4} - 
\dfrac{2 (r_d - r_i \cos{\alpha}) r_{d}^4}{r_{d}^2 [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}} }  \tag{r5}$$

The middle term inside the square root is easy to deal with, but the two others look pretty hairy. Let's look at them separately:
$$ \text{SQRT TERM \#1} = \dfrac{r_{d}^4}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2} \hspace{8em}$$

$$= \dfrac{1/r_{d}^4}{1/r_{d}^4} \cdot \dfrac{r_{d}^4}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2}$$

$$ = \dfrac{1}{1/r_{d}^4 \cdot[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2}$$

$$ = \dfrac{1}{[1/r_{d}^2 \cdot (r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha)]^2}$$

$$ = \dfrac{1}{[r_{i}^2/r_{d}^2 + r_{d}^2/r_{d}^2 - 2 \cdot r_{i}/r_{d} \cdot r_{d}/r_{d} \cdot \cos \alpha]^2}$$

$$ = \dfrac{1}{[\gamma^2 + 1 - 2 \gamma \cos \alpha]^2} \tag{r6}$$

And for the other term:
$$ \text{SQRT TERM \#3} = \dfrac{2 (r_d - r_i \cos{\alpha}) r_{d}^4}{r_{d}^2 [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}} \hspace{8em}$$

$$ = \dfrac{2 (r_d - r_i \cos{\alpha}) r_{d}^2}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}$$

$$ = \dfrac{1/r_{d}}{1/r_{d}} \cdot \dfrac{1/r_{d}^2}{1/r_{d}^2} \cdot \dfrac{2 (r_d - r_i \cos{\alpha}) r_{d}^2}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}$$

$$ = \dfrac{1/r_{d}}{1/r_{d}} \cdot \dfrac{2 (r_d - r_i \cos{\alpha}) }{1/r_{d}^2 \cdot [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}$$

$$ = \dfrac{1/r_{d} \cdot 2 (r_d - r_i \cos{\alpha})}{1/r_{d}^3 \cdot [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}$$

$$ = \dfrac{2 (r_d/r_d - r_i/r_d \cdot \cos{\alpha}) }{[1/r_{d}^2 \cdot (r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha)]^{3/2}}$$

$$ = \dfrac{2 (r_d/r_d - r_i/r_d \cdot \cos{\alpha}) }{[r_{i}^2/r_{d}^2 + r_{d}^2/r_{d}^2 - 2 \cdot r_{i}/r_{d} \cdot r_{d}/r_{d} \cdot \cos \alpha]^{3/2}}$$

$$ = \dfrac{2 (1 - \gamma \cos{\alpha}) }{[\gamma^2 + 1 - 2 \gamma \cos \alpha]^{3/2}} \tag{r7}$$


If we substitute $\text{r6}$ and $\text{r7}$ back into equation $\text{r5}$, we get:

$$a_d = G \dfrac{m_d}{r_d^2} 
\sqrt{
1 +
\dfrac{1}{[1+\gamma^2 - 2 \gamma \cos(\alpha)]^2} -
\dfrac{2(1-\gamma \cos(\alpha))}{[1+\gamma^2 - 2 \gamma \cos(\alpha)]^{3/2}}
}  
\tag{w4.11}$$

God have mercy on you if you have to derive this one on the exam.
![[thisisfine.png|200]]

```

So equation $\text{w4.11}$ is essentially written as a function of $\alpha$ and $\gamma$. Both variables are enclosed in the square root, with some factor $G m_d r_d^{-2}$ in front of it. If we plot this as function of $\alpha$ and $\gamma$, we get something that looks like this:
![[hell_equation_colours.png]]

````ad-abstract
title: Plot code
icon: python
collapse: closed
color: 45,215,60

```py
import numpy as np
import matplotlib.pyplot as plt

def a_d(alpha, gamma, G=1, rd=1, mj=1):
    q1 = 1/(1+gamma**2 - 2*gamma*np.cos(alpha))**2
    q2 = 2*(1-gamma*np.cos(alpha))/(1+gamma**2 - 2*gamma*np.cos(alpha))**(3/2)
    return G*mj/rd**2*np.sqrt(1+q1-q2)

alpha = np.linspace(0,np.pi,20)
gamma = np.logspace(-2,5,20)

ag_surface = np.zeros((len(alpha), len(gamma)))

for Alpha in range(len(alpha)):
    for Gamma in range(len(gamma)):
        ag_surface[Alpha,Gamma] = a_d(alpha[Alpha],gamma[Gamma])
        
fig, ax = plt.subplots()
plot1 = ax.pcolormesh(gamma, alpha, ag_surface, shading='auto')
plt.xscale("log")
plt.xlim(min(gamma),max(gamma))
plt.ylim(min(alpha),max(alpha))
plt.xlabel("r_i / r_d")
plt.ylabel("alpha [rad]")

fig.colorbar(plot1)
```

````

The plot suggests that most of the interesting stuff, namely the highest perturbing accelerations, happen where $\alpha$ is close to $0^\circ$, and $\gamma$ is of order of magnitude of $10^0$. The [[Wakker|book]] takes a more analytical approach, and mentions the following points:

1. The acceleration $a_d$ is always positive, regardless of $\alpha$, so long as $\gamma>0$.
2. The maximum $a_d$ happens when $\alpha = 0^\circ$. This is true regardless of the value of $\gamma$.
![[perturbation3.png]]
3. A second maximum appears at $\alpha = 180^\circ$ only when $\gamma < 1.74$. The acceleration value at this local maximum is typically smaller in magnitude than the one at $\alpha = 0^\circ$. As a result, it did not even really register on the previous plot, but it is there in the mathematics.
![[perturbation4.png]]
4. We can also find the combination of $\alpha$ and $\gamma$ for which the acceleration is minimal. It turns out these minima can be visualized as points, and the points move as a result of varying $\gamma$:
	- When $\gamma$ is below 0.5, the minimum acceleration due to perturbations can be found around the central body at the places that correspond to $\alpha = 90^\circ$ and $\alpha = 270^\circ$.
![[perturbation5a.png]]
	- When $\gamma$ is then increased above 0.5, the locations of the minima start moving back further towards $\alpha = 180^\circ$.
![[perturbation5b.png]]
	- Finally, when $\gamma$ is increased beyond $1.74$, the point at $\alpha=180^\circ$ becomes the minimum.
![[perturbation5c.png]]
5. The [[Wakker|book]] also mentions that for very small values of $\gamma$ ($< 0.1$) the whole square root term from $\text{w4.11}$ is approximately equal to $\gamma$, and the maximum value is about equal to $2 \gamma$.

### Maximum disturbance acceleration

Using equation $\text{w4.11}$, one can calculate the magnitude of the maximum acceleration, which happens for $\alpha = 0^\circ$:
$$ (a_d)_{max} = G \dfrac{m_d}{r_d^2} 
\left| \dfrac{1}{(1-\gamma)^2} -1 \right| 
\tag{w4.12}$$

```ad-note
title: Math
icon: paperclip
collapse: closed
color: 180,180,180

Substitute $\alpha = 0^\circ$ into $\text{w4.11}$:
$$a_d = G \dfrac{m_d}{r_d^2} 
\sqrt{
1 +
\dfrac{1}{[1+\gamma^2 - 2 \gamma \cos(0^\circ)]^2} -
\dfrac{2(1-\gamma \cos(0^\circ))}{[1+\gamma^2 - 2 \gamma \cos(0^\circ)]^{3/2}}
} \tag{r1}$$

$$ = G \dfrac{m_d}{r_d^2} 
\sqrt{
1 +
\dfrac{1}{[1+\gamma^2 - 2 \gamma]^2} -
\dfrac{2(1-\gamma )}{[1+\gamma^2 - 2 \gamma]^{3/2}}
}  
\tag{r2}$$

$$ = G \dfrac{m_d}{r_d^2} 
\sqrt{
1 +
\dfrac{1}{[(1-\gamma)^2]^2} -
\dfrac{2(1-\gamma )}{[(1-\gamma)^2]^{3/2}}
}  
\tag{r3}$$

$$ = G \dfrac{m_d}{r_d^2} 
\sqrt{
1 +
\dfrac{1}{[(1-\gamma)^2]^2} -
\dfrac{2(1-\gamma )}{(1-\gamma)^3}
}  
\tag{r3}$$

$$ = G \dfrac{m_d}{r_d^2} 
\sqrt{
1^2 +
\left[ \dfrac{1}{(1-\gamma)^2}\right]^2 -
2 \cdot \left [\dfrac{1}{(1-\gamma)^2} \right]
}  
\tag{r5}$$


At this point the solution could either be:
$$ G \dfrac{m_d}{r_d^2} 
\sqrt{ \left( 1 - \left[ \dfrac{1}{(1-\gamma)^2}\right]\right)^2} 
\quad \text{or} \quad
G \dfrac{m_d}{r_d^2} 
\sqrt{ \left(\left[ \dfrac{1}{(1-\gamma)^2}\right]-1\right)^2} 
\tag{r6}$$

which is:

$$ G \dfrac{m_d}{r_d^2} 
\left( 1 - \dfrac{1}{(1-\gamma)^2} \right) 
\quad \text{or} \quad
G \dfrac{m_d}{r_d^2} 
\left( \dfrac{1}{(1-\gamma)^2} -1 \right) 
\tag{r7}$$

[[Wakker]] resolves this by taking the absolute value of the bracketed term, forcing the outcome to be positive:

$$ (a_d)_{max} = G \dfrac{m_d}{r_d^2} 
\left| \dfrac{1}{(1-\gamma)^2} -1 \right| 
\tag{w4.12}$$

```

Finally, we can compare the perturbing accelerations of a primary body $k$ and a perturbing body $d$ by calculating the **maximum relative perturbing acceleration**:

$$ \left(\dfrac{a_d}{a_k}\right)_{max} = \dfrac{m_d}{m_k} \left(\dfrac{r_k}{r_d}\right)^2 
\left| \dfrac{1}{(1-r_k/r_d)^2} -1 \right| 
\tag{w4.14}$$

On page 109 of the [[Wakker]] book you can find a table with the values of the maximum relative perturbing acceleration of various celestial bodies on the orbit of Earth around the sun. It is interesting to note that the values are heavily influenced by both the $m_d/m_k$ term as well as the $r_k/r_d$ term. The strongest influence on Earth's orbit is the moon, where $\left(\dfrac{a_d}{a_k}\right)_{max}$ is of $\mathcal{O}(-3)$, followed by Venus and Jupiter, whose influence is of $\mathcal{O}(-5)$.
___
## Sphere of influence
<!-- [Wakker] section 4.3 -->

```ad-note
title: ## To do: Add derivation of the Sphere of Influence radius
icon: hammer
color: 240,200,25
It may be possible to combine the overly convoluted derivation in [[Wakker]] and the [simpler derivation on Wikipedia](https://en.wikipedia.org/wiki/Sphere_of_influence_(astrodynamics)#Derivation) together to create a derivation that is comprehensive but comprehensible.
```

What we have seen in the previous section is that if you have a spacecraft that is located somewhere in relation to two bodies, it will experience a gravitational acceleration from either body. The magnitude of this acceleration depends on where exactly the spacecraft is located with respect to the two bodies. The question is now: when is it appropriate to describe the spacecraft's position in terms of the first body, and when in terms of the second body? When do the graviational effects of the one body take precedent over the other?

This is a question that none other than Laplace himself considered, and he developed a concept called the **sphere of influence** (or SOI) as part of his answer. In essence, this is a circle (or a sphere in 3D space) around a body with mass. Inside the circle, the body's gravitational effects dominate, whilst outside the circle, those of the other body dominate. For the Earth and the sun, this looks something like this:
![[SOI.png]]

In reality, there will be more bodies which will distort the shape of the "sphere" of influence. Note for example that in the above image, we've conveniently left out the moon, Venus, or Jupiter. However, for most situations in the solar system, you can approximate things pretty well with a two-body model (except for example near the [Pluto-Charon system](https://en.wikipedia.org/wiki/Pluto#Satellites)). 

But even for a two-body case such as we consider here, the sphere of influence is not truly a sphere, but almost a sphere. This can be thought of as something I like to refer to as the "egg of influence", depicted below:

![[SOI_egg.png]]

The reason for this is that if you're between Earth and the sun, and you're moving toward the sun, the gravitational effects of the Sun will become dominant more quickly than if you were to move perpendicularly to the sun. It can be shown that the ratio between the two radii is:
$$\dfrac{(r_{SOI})_{min}}{(r_{SOI})_{max}} \approx \left(\dfrac{1+3 \cos^2 (0^\circ)}{1+3 \cos^2 (90^\circ)} \right)^{-1/10} \approx 0.87$$

However, it turns out that we commonly neglect this oblateness and just assume that the SOI is a perfect sphere. So we will do the same for now.
```ad-warning
title: Assumption: The Sphere of Influence is a sphere!
color: 200,80,225
When discussing the Sphere of Influence (SOI), we assume that the SOI is a perfect sphere. As such, we ignore:
 - The effect of third bodies on the shape of the SOI.
 - The oblation of the SOI in the two-body case (no "egg of influence").
```
In that case, we can calculate the radius of the SOI as follows:

$$R_{SOI} = r_{13} \left( \dfrac{m_1}{m_3}\right)^{2/5}$$

Where $r_{13}$ is the distance between body $1$ and $3$. From this we can draw a few important conclusions:
 - The size of the SOI of some primary body (e.g. the Earth) is **not** fixed, but also depends on the perturbing body that is being considered (e.g. the sun).
 - The heavier the primary body is with respect to the perturbing body, the larger the SOI of the primary body.
 - The radius of the SOI increases proportionally to the distance between the primary and disturbing body.

The concept of the Sphere of Influence is not only useful as an intellectual tool to think about bodies, but is also used practically. A notable example is a spacecraft in a lunar mission, which has the same problem as Laplace: At what point do you switch from an Earth-centric reference frame to a lunar-centric reference frame? The answer is: When you arrive at the sphere of influence of the moon, which is where the gravitational effects of the moon start dominating over those of the Earth.

![[SOI_lunar.png]]

The Sphere of Influence **not** the same thing as the [[Hill sphere]], although the concepts are closely related.

___
