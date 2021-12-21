# The Vis-viva Equation
![[visviva.png]]

If you're a budding astrodynamicist, you've just found your new best friend; the vis-viva equation. Seriously, I cannot overstate how mind-bogglingly useful this equation is for dealing with any two-body system.

In simple terms, this equation tells us that the internal energy of any two-body system consists of kinetic energy and potential energy, and that the total amount is some constant value $\mathcal{E}$:

$$\dfrac{1}{2}V^2 - \dfrac{\mu}{r} = \mathcal{E}$$

Note that for elliptical orbits, the value of $\mathcal{E}$ is always **negative** by definition, and always positive for hyperbolic trajectories. For the special case of the parabolic orbit, the internal energy is zero.

___

```ad-note
title: Note: When are you allowed to use the vis-viva equation?

You are allowed to use the vis-viva equation:
 - So long as the system contains **two bodies**.
 - So long as the orbit is a **conic section**.
 - So long as the only sources of internal energy are **kinetic and potential energy** (i.e. only point masses, no relativistic effects, etc.)

```