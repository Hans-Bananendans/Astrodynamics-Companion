# The Clohessy-Wiltshire equations
```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25
```

<!-- Wakker section 9.1-9.2 -->

How altered frame layout is made (compared to CR3BP layout)

Equations of motion in terms of prime frame

Linearized equations of motion ($1/r^3 \approx 1-3x'$)

Re-introducing physical units (orbital period of satellite 1)

Drop prime notation and warn clearly.

Solving these equations of motion using method of undetermined coefficients on $z$-equation and coupled $x,y$-system.

Present CW equations with their particular solutions (perturbed motion)

See if you can do better job at explaining the various characteristics of the CW equations (probably not, lecture 7b is excellent). Add math block with proof of phase difference of pi/2 (only shown visually in lecture).

Warning about the linearized nature of CW equations -> outcome in reality will diverge from this model as time increases.

Coding example of relative motion with an initial relative state vector (r,V) and plot. This important because the motion can be quite counter-intuitive. Play is key.

Parking space for CW equation:
$$
\hspace{-6em} % Pull equation closer to the left
\begin{cases}
x \quad = \quad \left( 4 x_0 + \dfrac{2 \dot{y_0}}{n} \right) + 
\dfrac{\dot{x_0}}{n} \sin(nt) - 
\left( 3 x_0 + \dfrac{2 \dot{y_0}}{n} \right) \cos(nt)
\\
y \quad = \quad \left( y_0 - \dfrac{2 \dot{x_0}}{n} \right) - 
3 \left( 2 x_0 + \dfrac{\dot{y_0}}{n} \right) nt +
2 \left( 3 x_0 + \dfrac{2 \dot{y_0}}{n} \right) \sin(nt) +
\dfrac{2 \dot{x}_0}{n} \cos(nt)
\\
z \quad = \quad z_0 \cos(nt) +
\dfrac{\dot{z_0}}{n} \sin(nt)
\end{cases}
\tag{w15.1}
$$