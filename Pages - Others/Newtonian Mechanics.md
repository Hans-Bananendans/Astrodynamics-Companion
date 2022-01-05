# Newtonian Mechanics
<!-- This covers sections 1.1-1.8 from [[Wakker]] #chapter1 -->
```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25
```
___
## Newton's laws of motion
<!-- [[Wakker]] section 1.1-->
Newton developed three laws of motion, which we now consider to be fundamental to Newtonian mechanics. Much of the mathematics in Astrodynamics start with these laws at the core, and elaborates from there. It is therefore important to understand exactly what these laws mean, so that we can understand what they imply in de context of Astrodynamics.

#### Newton's first law
_"Every particle continues in its state of rest or uniform motion in a straight line
relative to an inertial reference frame, unless it is compelled to change that state by
forces acting upon it."_
$$\text{If} \quad \bar{F}_{net} = 0 \quad \text{then} \quad \dfrac{d\bar{V}}{dt} = 0 $$

#### Newton's second law
_"The time rate of change of linear momentum of a particle relative to an inertial
reference frame is proportional to the resultant of all forces acting upon that particle
and is collinear with and in the direction of the resultant force."_
$$\bar{F}_{net} = \dfrac{d\bar{p}}{dt} = \dfrac{d(m \cdot \bar{V})}{dt} $$
In most of the theory considered in this summary, we assume that the mass of a body is constant, and in this case the time rate of change of the mass is zero. This reduces the above to:
$$\bar{F}_{net} = m \cdot \dfrac{d\bar{V}}{dt} = m \cdot \bar{a}$$

#### Newton's third law
_"If two particles exert forces on each other, these forces are equal in magnitude and
opposite in direction (action = opposite reaction)."_
$$\bar{F}_{A} = -\bar{F}_{B}$$

___
## Inertial reference frames
<!-- [[Wakker]] section 1.2-->
When applying Newton's laws, **inertial reference frames** (IRFs) come up rather often. For example, Newton's second law is _only_ valid for inertial reference frames. It is important to know what exactly this term refers to, and how such frames are different to non-inertial reference frames.

A reference frame is an inertial reference frames **if and only if**:
 - It remains static with respect to some other reference frame
or 
 - It travels uniformly on on a rectilinear path with respect to some other reference frame.

So any reference frame that for example rotates, or does not travel at constant speed with respect to some other frame, is **not** an inertial reference frame.

![[irf.png]]

In the figure depicted, you can see a reference frame XYZ, with a second, non-rotating reference frame X'Y'Z'. The frame X'Y'Z' is moving with respect to XYZ at a constant velocity $\bar{W}$. This makes X'Y'Z' also an inertial reference frame. 

You can describe the depicted point P in terms of either frame. P is described in terms of XYZ with vector $\bar{r}$, and in terms of X'Y'Z' with vector $\bar{r}'$. You can relate $\bar{r}$ and $\bar{r}'$ by using the _Galilei transformations_:
$$
\tag{w1.1}
\bar{r}' = \bar{r} - \bar{W}(t-t_0)	\quad ; \quad t' = t+T
$$
Note that for simplicity it is assumed here that the origins of the two reference frames coincide with each other at time $t_0$.

```ad-note
title: Note

The Newtonian principles discussed here use a notion that time is absolute; that there is some constant march of time that identical everywhere in the universe. However, because of Einstein we know that this is not true. The concepts of both general relativity and special relativity both presume that space and time do vary together, and that time can flow at different rates depending on your reference frame. And real-world measurements confirm that indeed it does.

In this whole summary on Astrodynamics, we ignore these effects, as their contribution is usually very small at small relative speeds. Instead, we presume that time flows equally everywhere, so that we do not have to correct our Newtonian framework for these relativistic effects.
```
___

### Apparent forces
However, it is not always convenient to use inertial reference frames. For example, if we wish to describe a satellite orbiting the Earth with respect to some location on Earth, say a ground station, we must realize that the Earth rotates around its axis once every day. In this case it is much more convenient to fix a rotating reference frame to the Earth.

When you do this, the rotating reference frame is no longer an _inertial_ reference frame, and so Newtonian mechanics can no longer be applied. However, we can still use Newtonian mechanics if we patch the model with so-called **apparent forces**. These apparent forces are not 'real' in the same sense as for example the force of a rocket's thrust is real, but they emerge from the relative motion between the reference frames. In general, we can recognize four apparent forces:

1. **Inertial force**, which is caused by a rectilinear acceleration of the reference frame's origin. $$\bar{F}_{inertial} = -m\bar{a}$$
2. **Centrifugal force**, which is caused by a constant rotation of the reference frame. $$\bar{F}_{centrifugal} = -m\bar{\omega} \times (\bar{\omega} \times \bar{r}') $$
3. **Coriolis force**, which is also caused by a constant rotation of the reference frame. $$\bar{F}_{Coriolis} = -2m\bar{\omega} \times \dfrac{d\bar{r}'}{dt}$$
5. **Euler force**, which is caused by a rotational acceleration of the reference frame. $$\bar{F}_{Euler} = m \dfrac{d\bar{\omega}}{dt} \times \bar{r}'$$

A similar thing happens with external forces. For example, for a thrusting rocket, we can write down Newton's second law as follows:
$$\bar{F} - \dot{m}\bar{V}_j = M \dfrac{d\bar{V}_{cm}}{dt} \tag{w1.9}$$
Here $\bar{F}$ is the net external (natural) force, and the second term on the left hand side is formally an apparent force also.
___
### Pseudo-inertial reference frames
<!-- [[Wakker]] section 2.6-->
Just read section 2.6 of the [[Wakker|Wakker book]]. In essence, in reality we never deal with perfect point masses and perfect inertial reference frames. However, often the motion we are interested in is of such a scale that we can ignore the effects that the non-inertial reference frames cause. The book uses the following examples:
- If you are considering the trajectory of a bullet, you can pretty much ignore the coriolis and centrifugal forces that are acting on the body because of the rotation of the Earth. These forces are tiny in comparison of the other forces on the bullet, and the flight time of the bullet is very small compared to the motion of the Earth. Instead, you can model it by sticking an inertial reference frame to the surface of the Earth.
- If you are modelling a ballistic missile, you certainly cannot ignore the rotation of the Earth. However, you can probably ignore the effect of the Earth's rotation around the sun, and use a reference frame stuck to the centre of the Earth.

In conclusion; in reality we never deal with "true" inertial reference frames, but often we can get away with pretending that they are, depending on the size scale and time scale that we're considering. In such case, we speak of **pseudo-inertial reference frames**.

___
## Chaotic motion
<!-- [[Wakker]] section 1.3-->
Many phenomena in Astrodynamics are subject to chaotic effects. In plain terms, this is the effect that the state of some system is incredibly sensitive to its past conditions. In fact, for a chaotic system, one would need to measure all the past states  with infinite precision to predict its future behaviour, especially behaviour far in the future.

We will see that an example of this is the motion of three or more bodies under each other's gravity. This is the main reason that for planning orbital trajectories, astrodynamicists often use orbit propagators: there is no general, closed-loop solution for the orbital motion of more than two bodies.

Chaos in the solar system is also associated with gravitational resonances. The simplest example of this is when two orbiting bodies have orbital periods that are close to the ratio of two integers. There are numerous examples of this in the solar system:

|System              | Resonance |
|:-------------------|----------:|
| Venus-Earth        | 13:8      |
| Venus-Mars         | 3:1       |
| Jupiter-Saturn     | 5:2       |
| Uranus-Neptune     | 2:1       |
| Neptune-Pluto      | 3:2       |
| Io-Europa-Ganymede | 4:2:1     |
| Enceladus-Dione    | 2:1       |
___

## Newton's law of gravity
<!-- [[Wakker]] section 1.4-->
Newton's law of gravity states the following:
_"Two particles attract each other with a force directly proportional to their masses and inversely proportional to the square of the distance between them."_
If the masses of these bodies are $m_1$ and $m_2$ and the distance between them is $r$, then in mathematical terms this law is:
$$F = G\dfrac{m_1 m_2}{r^2} \tag{w1.11}$$
Note that this is a scalar equation, that can only give you the magnitude of the forces involved. In practice, there is often a large difference between the masses. If this difference is large enough, for example in case of a satellite orbiting a planet, the smaller mass can be safely ignored. In terms of accelerations, the gravitational acceleration of a satellite on a planet is usually of $O(-20) \; m/s^2$, and the gravitational acceleration of two large spacecraft is in the ballpark of $O(-13) \; m/s^2$.

```ad-warning
title: Assumption
color: 200,80,225

When working with this equation, we assume that the masses involved are either **point masses** (their radius is zero) or that they behave like point masses (their shapes and mass distributions are uniform, so that their centroid and their center of gravity align).

```

The parameter $G$ in equation $\text{w1.11}$ is the **universal gravitational constant**, with a currently established value of $G= 6.67428\cdot10^{-11} \; m^3/kg \; s^2$. In practice, this parameter is extremely difficult to measure accurately. However, the product of $G$ and the mass of a large body is generally much easier to measure. Therefore we usually work with $\mu$, the body-specific gravitational parameter:
$$\mu_{body} = G \cdot M_{body}$$

We can also write equation $\text{w1.11}$ in a vectorial form, so it can be used to calculate both magnitude and direction. To do so, we consider two **point masses** with mass $m_1$ and $m_2$. The distance from $m_1$ to $m_2$ is denoted with position vector $\bar{r}_{12}$, and the gravity force exerted by $m_1$ on $m_2$ is $\bar{F}_{21}$. Now, take careful note of these subscripts, as they tell you where the vectors are pointing. This can also be seen in the figure.

![[points_gravity.png]]

You may also notice that there is another vector pointing towards $m_2$, namely the vector $\hat{r}_{12}$. This vector is **not** the same as $\bar{r}_{12}$, but instead is a univector, a vector of length 1, pointing from $m_1$ towards $m_2$. If we now wish to rewrite equation $\text{w1.11}$ into a vectorial form, we can simply multiply its righthand side with this univector $\hat{r}_{12}$. Then, the resultant force will also be vectorial. However, as you can see, force $\bar{F}_{21}$ points **in the opposite direction** of vector $\hat{r}_{12}$, and so we introduce an extra minus sign into the equation, so that $\text{w1.11}$ becomes:

$$\bar{F} = -G\dfrac{m_1 m_2}{r^2}\hat{r}_{12}$$


```ad-warning

[[Wakker|The Wakker book]] is not always very clear about the distinction between using the univector $\hat{r}$ and the relative position vector $\bar{r}$. However, you should note carefully when which form is being used, because otherwise your answer could be off by a factor of $r$.

In addition, _K.F. Wakker_ prefers to simplify the notation of subscripts frequently, but usually only draws attention to this once, and then moves on. Note that up to here, we have used double subscripts; Vector $\bar{r}_{12}$ points **from** position 1 **to** position 2. However, in [[Wakker|the Wakker book]] you will find that at this point, the first subscript has already been omitted, and the vector is denoted by $\bar{r}_{2}$ instead. Take careful notice that you still understand where the vectors are pointing, because otherwise one could easily overlook the minus sign if the vectors point in opposing directions!
```

In many cases it is more useful to write this equation not in terms of the univector $\hat{r}_{12}$, but instead in terms of the relative position vector $\bar{r}_{12}$. Since we know that $\hat{r}_{12}$ has length 1 (as it is a univector), and that $\bar{r}_{12}$ has length $r$ (as it is the distance between the two masses), we can simply say that $\bar{r}_{12}$ is $r$ times as long as $\hat{r}_{12}$, or:
$$\bar{r}_{12} = r \hat{r}_{12}$$
or alternatively:
$$\hat{r}_{12} = \dfrac{\bar{r}_{12}}{r}$$

If we substitute this in the previous equation, we find that:

$$\bar{F} = -G\dfrac{m_1 m_2}{r^2}\dfrac{\bar{r}_{12}}{r} = -G\dfrac{m_1 m_2}{r^3}\bar{r}_{12}$$

This is also the form you will find in [[Wakker|the Wakker book]]:
$$\bar{F} = -G\dfrac{m_1 m_2}{r^3}\bar{r} \tag{w1.12}$$

```ad-note
The main important take-away here is that for the equation of the gravity force between two bodies, there is a **scalar** form and a **vectorial** form. The scalar form has the force inversely proportional to $r^2$, whilst the vectorial form has the force inversely proportional to $r^3$. This is because we commonly choose to express the vectorial force in terms of the relative position vector $\bar{r}$, rather than the univector $\hat{r}$. The minus sign in the vectorial form stems from the fact that the vectors $\bar{r}$ and $\bar{F}$ point in opposite directions.

$$
\begin{align}

\text{Scalar form:}
\hspace{11em}
\text{Vectorial form:}

\\
\\

F = G\dfrac{m_1 m_2}{r^2}
\hspace{10em}
\bar{F} = -G\dfrac{m_1 m_2}{r^3}\bar{r}

\end{align}
$$

```
___
### Gravity fields and potentials
Two more useful concepts that sometimes come up are the concepts of **gravity fields** and **gravity potentials**. As we have done previously, we often think of gravity's effect as a force, but we can also conceptualize it as a field. In the situation of two masses $m_1$ and $m_2$, we can say that $m_1$ is generating a gravity field, and $m_2$ is being affected by this field. Then we can pose that the local strength of this field at $m_2$ is the _gravity force per unit mass of $m_2$_. We will denote this with $\bar{g}_2$:

$$\bar{g}_2 = \dfrac{\bar{F}}{m_2} = -G\dfrac{m_1}{r^3}\bar{r}_{2}$$

or for $\bar{g}$ in general:
$$\bar{g} = -G\dfrac{m}{r^3}\bar{r}$$

The gravity potential $U$ is defined as **the amount of work per unit mass that must be done by the force of gravity to move an object to a fixed reference location**. Note that it is a scalar quantity, and is given by:

$$U = -G\dfrac{m}{r}$$

To relate the gravitational potential $U$ with the gravity field strength at some point, we have to negate it and take the [[Gradient Operator|gradient]] of it:

$$\bar{g} = - \bar{\nabla}U $$

The gravity force field is a **conservative** field, because its potential is not explicitly dependent on time.
___

## Gravity field of a thin spherical shell and a sphere
<!-- [[Wakker]] section 1.5-->

```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25

- [ ] Perform the derivation
- [ ] Add some better graphics
- [ ] Proofread

```

___
## External gravity field of a body with arbitrary mass distribution
<!-- [[Wakker]] section 1.6-->

```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25

- [ ] Perform the derivation
- [ ] Add some better graphics
- [ ] Proofread

```

___

## Maneuvers with rocket thrust
<!-- [[Wakker]] section 1.7-->

```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25

- [ ] Perform the derivation
- [ ] Refer to the [[Derivation - Ideal rocket equation]]
- [ ] Proofread

```

___