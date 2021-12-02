# Derivation - Ideal rocket equation
```ad-note
title: Note: The lecturer has an awesome video guide for this derivation on Brightspace
```

In this derivation, we will derive the famous or [Tsiolkovsky rocket equation](https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation). To start it, we start with a very simple model of a rocket that is throwing out propellant reactants at a significant speed, as depicted.
![[ideal_rocket_equation1.png]]

We make a couple of assumptions first, to simplify our work.
```ad-warning
title: Assumption 1
color: 200,80,225

We assume that the depicted system is **closed** and **no external forces**, such as drag, gravity, etcetera are present. 
```

```ad-warning
title: Assumption 2
color: 200,80,225

We assume that the depicted situation happens over an infinitesimally small unit of time: $$\Delta t \rightarrow 0$$

This means that we can also assume the ejected propellant mass to be much smaller than the total rocket mass:
$$m_P << m_R$$
```

### Step 1 - Define the exhaust velocity
With these assumptions under our belt, let's first get an expression for the exhaust velocity:
$$\bar{V}_P = \bar{V}_R + \bar{V}_{P/R} \tag{r1}$$
$$-V_P \hat{x} = V_R \hat{x} - V_{P/R} \hat{x} \tag{r2}$$
$$V_{e} = V_{P/R} = V_R + V_P \tag{r3}$$

Note the definition we have used for the positive $x$-direction, as well as the definition of $V_{P/R}$, which is the velocity of the propellant with respect to the rocket:
![[ideal_rocket_equation2.png]]

### Step 2 - Set up the momentum
Ideally, we would like to use the [[Newtonian Mechanics#Newton's second law|Newton's second law]] here. However, to do so, we would need an expression of the momentum, as Newton's second law says that the net force is equal to the time derivative of the momentum. The momentum is defined as mass times velocity, which we can set up both as vectors or as scalars:
$$\bar{p} = m_R \bar{V}_R + m_P \bar{V}_P \tag{r4}$$

$$p\hat{x} = m_R V_R\hat{x} -m_P V_P\hat{x} \tag{r5}$$
$$p = m_R V_R  -m_P V_P \tag{r6}$$

### Step 3 - Apply Newton's second law
Now it is time to apply Newton's second law:
$$\sum \bar{F} = \dfrac{d\bar{p}}{dt} = \dot{p} \tag{r7}$$

By virtue of assumption 1, we have no external forces, which means that $\sum \bar{F} = 0$, and as a result:
$$\dot{p} =0\tag{r8}$$

### Step 4 - Differentiate the momentum
We do not have an expression yet for the time derivative of the momentum, so let us try to find one. We can do this by using the [product rule](https://en.wikipedia.org/wiki/Product_rule):
$$\dot{p} = m_R \dot{V}_R + \dot{m}_R V_R - (m_P \dot{V}_P  + \dot{m}_P V_P) =0\tag{r9}$$

### Step 5 - Integrate
```ad-warning
title: Assumption 3
color: 200,80,225

Since the instantaneous propellant mass $\dot{m}_P$ is small and the acceleration of the propellant after exhaust $\dot{V}_P$ is small too, we assume that its product is negligible:
$$\dot{m}_P \dot{V}_P \approx 0$$

```
This allows us to rewrite $\text{r9}$ as:
$$ m_R \dot{V}_R + \dot{m}_R V_R - \dot{m}_P V_P = 0 \tag{r10}$$

The system is closed, so any mass that is added to the depicted cloud in the time interval $\Delta t$ **must** also have been removed from the rocket in that time. So the mass flows are equal, albeit opposite in sign:

$$\dot{m}_R = -\dot{m}_P \tag{r11}$$

Substituting this in equation $\text{r10}$ gives:
$$m_R \dot{V}_R + \dot{m}_R V_R + \dot{m}_R V_P = 0 \tag{r12}$$
$$m_R \dot{V}_R = -( V_R + V_P) \dot{m}_R \tag{r13}$$
Using equation $\text{r3}$, we can reduce this to:
$$m_R \dot{V}_R = -V_e \dot{m}_R \tag{r14}$$
$$\dot{V}_R = -V_e \dfrac{\dot{m}_R}{m_R} \tag{r15}$$
Integrate:
$$\int_{V_1}^{V_2}dV_R = -\int_{m_1}^{m_2} V_e \dfrac{dm_R}{m_R} \tag{r16}$$

We now make another assumption which allows us to exclude $V_e$ from the integral:
```ad-warning
title: Assumption 4
color: 200,80,225

We assume that the exhaust velocity is constant, regardless of rocket mass:
$$\dfrac{dV_e}{dm_R} = 0$$

```

$$\int_{V_1}^{V_2}dV_R = -V_e \int_{m_1}^{m_2}  \dfrac{dm_R}{m_R} \tag{r17}$$

$$V_2 - V_1 = -V_{e} \left[ \ln(m_R) \right]^{m_2}_{m_1} = -V_{e} \left[ \ln(m_2) - \ln(m_1) \right] \tag{r18}$$

Using [one of the properties of logarithms](https://en.wikipedia.org/wiki/Logarithm#Product,_quotient,_power,_and_root), and by substituting $\Delta V = V_2 - V_1$, we get:

$$\Delta V = -V_{e} \ln \left( \dfrac{m_2}{m_1} \right) \tag{r19}$$
___

