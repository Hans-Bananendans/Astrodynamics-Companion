# The Vis-viva Equation
![[visviva.png]]

If you're a budding astrodynamicist, you've just found your new best friend; the vis-viva equation ("_vis viva_" from Latin: "_living force_"). Seriously, I cannot overstate how mind-bogglingly useful this equation is for dealing with any restricted two-body system.

In simple terms, the vis-viva equation tells us that the internal energy of any restricted two-body system consists of kinetic energy and potential energy, and that the total amount is some constant value $\mathcal{E}$:

$$\dfrac{1}{2}V^2 - \dfrac{\mu}{r} = \mathcal{E}$$

We call $\mathcal{E}$ the **specific orbital energy**. Note that for elliptical orbits, the value of $\mathcal{E}$ is always **negative** by definition, and always positive for hyperbolic trajectories. For the special case of the parabolic orbit, the internal energy is zero.

If considering an **elliptical orbit**, the specific orbital energy $\mathcal{E}$ equals a constant $-\mu/2a$, and in that case the vis-viva equation can be reformulated to:
$$\dfrac{1}{2}V^2 - \dfrac{\mu}{r} = -\dfrac{\mu}{2a}$$

___

```ad-note
title: Note: When are you allowed to use the vis-viva equation?

You are allowed to use the vis-viva equation:
 - So long as the system contains **two bodies**.
 - So long as the mass of one of the bodies is so small that it can be ignored (restricted two-body problem).
 - So long as the orbit is a **Kepler orbit**.
 - So long as the only sources of internal energy are **kinetic and potential energy** (i.e. only point masses, no relativistic effects, etc.)

```