# Derivation - Ideal rocket thrust
```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25

- [ ] Assumption ~~3~~ 4 is wrong (product of two dotted terms)
```

```ad-note
title: Note: The lecturer has an awesome video guide for this derivation on Brightspace
```

```ad-note
title: Note
This derivation features pressure and momentum, both of which are commonly denoted by $p$. To avoid confusion, this derivation uses the following notation:
 - Pressure is denoted by $P$.
 - Momentum is denoted by $p$.
```

This derivation is a continuation of the [[Derivation - Ideal rocket equation|derivation of the ideal rocket equation]], so go read that first if you haven't already. 

Although the ideal rocket equation is very useful for determining $\Delta V$ and the masses involved, it does not actually tell us anything about the thrust. To say something about the thrust, we have to adapt the model for the ideal rocket equation to also include pressure terms.

![[ideal_rocket_equation3.png]]

We have redrawn our rocket, but this time we define a square boundary around it, which encloses the rocket around the nozzle exit on the right and at the head on the left. If we presume that there is some ambient pressure $P_a$ outside the rocket, and we only consider the $x$-direction, we can say that the ambient pressure exerts a force on the nose of the rocket which is proportional to the area.
$$ F_{nose} = P_a A_{nose} = P_a A_e \tag{r1}$$


```ad-warning
title: Assumption 1
color: 200,80,225

Here we have assumed that the projected area of the nose is equal to the area of the nozzle:
$$A_{nose} = A_e$$
```

At the nozzle exit, we have a similar situation: the outside pressure exerts a force equal to pressure at the nozzle times nozzle area. The pressure at the nozzle is **not** the ambient pressure, but the pressure of the exhaust gases that are being expelled:
$$F_{e} = P_e A_e  \tag{r2}$$

Now we can return to applying [[Newtonian Mechanics#Newton's second law|Newton's second law]], like in the [[Derivation - Ideal rocket equation|previous derivation]]. However, we should not forget that when we did this, we made two assumption, which we slightly modify now:

```ad-warning
title: Assumption ~~1~~ 2
color: 200,80,225

We assume that the depicted system ~~is **closed** and **no external forces**, such as drag, gravity, etcetera are present~~ **only** has forces due to pressure, but not due to drag, gravity, etc.
```

```ad-warning
title: Assumption ~~2~~ 3
color: 200,80,225

We assume that the depicted situation happens over an infinitesimally small unit of time: $$\Delta t \rightarrow 0$$

This means that we can also assume the ejected propellant mass to be much smaller than the total rocket mass:
$$m_P << m_R$$
```

Applying Newton's second law, we get:
$$\sum \bar{F} = \dfrac{d\bar{p}}{dt} = \dot{p} \tag{r3}$$

$$ F_{e} - F_{nose} =  \dfrac{d}{dt}(p) \tag{r4}$$

$$ P_e A_e - P_a A_e =  \dfrac{d}{dt}(m_R V_R  -m_P V_P) \tag{r5}$$

$$ P_e A_e - P_a A_e = m_R \dot{V}_R + \dot{m}_R V_R - (m_P \dot{V}_P  + \dot{m}_P V_P) \tag{r6}$$

We make the same assumption that we made before to simplify things somewhat:
```ad-warning
title: Assumption ~~3~~ 4
color: 200,80,225

Since the instantaneous propellant mass $\dot{m}_P$ is small and the acceleration of the propellant after exhaust $\dot{V}_P$ is small too, we assume that its product is negligible:
$$\dot{m}_P \dot{V}_P \approx 0$$

```

$$ P_e A_e - P_a A_e = m_R \dot{V}_R + \dot{m}_R V_R - \dot{m}_P V_P \tag{r7}$$
$$ P_e A_e - P_a A_e = m_R \dot{V}_R - \dot{m}_P V_R - \dot{m}_P V_P \tag{r8}$$
$$ P_e A_e - P_a A_e = m_R \dot{V}_R - \dot{m}_P (V_R + V_P) \tag{r9}$$
$$ A_e (P_e - P_a) =  m_R \dot{V}_R - \dot{m}_P V_e \tag{r10}$$
$$ m_R \dot{V}_R = \dot{m}_P V_e + A_e (P_e - P_a) \tag{r11}$$

During some of these steps we used a number of  recycled a number of equations from the [[Derivation - Ideal rocket equation|previous derivation]]:
 - For $\text{r8}$ we used: $\dot{m}_R = - \dot{m}_P$
 - For $\text{r10}$ we used: $V_{e} = V_R + V_P$

And since mass times acceleration equals force, by virtue of Newton's second law, we can write the ideal rocket thrust equation in a form which you can frequently encounter [elsewhere](https://en.wikipedia.org/wiki/Rocket_engine#Net_thrust):
$$ F_T = \dot{m}_P V_e + A_e (P_e - P_a) \tag{r12}$$

___

