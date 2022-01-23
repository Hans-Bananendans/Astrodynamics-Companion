# The Clohessy-Wiltshire equations
```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25
```

<!-- Wakker section 9.1-9.2 -->
## Introduction
In this section, we are going to look at the relative motion between two orbiting spacecraft. In particular, we want to consider the chase where these spacecraft are very close to one another, and may want to dock.

If you are anything like me, you enjoy a good sci-fi movie set in space. There are many sci-fi movies that have a space ship approach another space ship. However, the way this motion occurs in the movie and how it occurs in reality does not always match up. Let's imagine the depicted situation, where a red spacecraft wants to board with an orbiting blue spacecraft. In-keeping with the terminology of [[Wakker]], we will call the red spaceship the **chaser** and the blue spaceship the **target**. In this case, the chaser has matched orbit with the target, following it at some distance.

![[cw_problem1.png]]

How can the chaser catch up with the target? From your intuition, you may reason as follows:

_"Both spacecraft are orbiting the planet in zero gravity. If the chaser wants to catch up with the target, it has to accelerate towards it rectilinearly, which is described by Newton's second law, $F=ma$. Since the chaser wants to accelerate towards the target, it fires its thruster in the opposite direction, and then drifts along until it arrives at the target."_

![[cw_problem2.png]]

Indeed, this is what many sci-fi movies will have you believe. But the crew of the chaser are in for a nasty surprise: In reality, this is **NOT** what will happen after they perform their thruster burn. Instead, what will happen is something like this:

![[cw_problem3.png]]

So not only do they get no closer to their target, they actually end up **farther away** from it, and have wasted some fuel in the process. Not ideal. So what happened here?

The main problem with the "naive reasoning" above is that it ignores the fact that although the space ships are in free-fall, they are still moving in a region of space with a gravity potential, because they are orbiting a large body. And this **cannot** simply be ignored.
```ad-note
title: **To do: Reference to section describing gravity potential**
icon: hammer
color: 240,200,25
```
To help build an intuition for why the motion of the chaser looks like it does in the figure above, consider this: By firing its thruster along the orbital velocity vector, the chaser increases its orbital velocity, which raises the apoapsis of its orbit. Raising the apoapsis increases the semi-major axis $a$ of the orbit, and we know from [[Kepler's Laws#Kepler's third law|Kepler's third law]] that increasing the semi-major axis increases the orbital period. 

So in a nutshell, by firing its thrusters forward, the chaser ends up in an orbit with a longer period than the target, and so it will fall behind. It turns out that the dynamics of this whole situation can be described fairly well by something called the **Clohessy-Wiltshire equations**, a general formulation of which looks like this:

$$
\hspace{-6em} % Pull equation closer to the left
\begin{cases}
\begin{matrix}
	x \quad = \quad \left( 4 x_0 + \dfrac{2 \dot{y_0}}{n} \right) + 
	\dfrac{\dot{x_0}}{n} \sin(nt) - 
	\left( 3 x_0 + \dfrac{2 \dot{y_0}}{n} \right) \cos(nt) 
	\\
	+\dfrac{f_x}{n^2}(1-\cos(nt)) + 
	\dfrac{2 f_y}{n^2}(nt - \sin(nt))
	\hspace{-4em}
\end{matrix}
\\
\begin{matrix}
	y \quad = \quad \left( y_0 - \dfrac{2 \dot{x_0}}{n} \right) - 
	3 \left( 2 x_0 + \dfrac{\dot{y_0}}{n} \right) nt +
	2 \left( 3 x_0 + \dfrac{2 \dot{y_0}}{n} \right) \sin(nt) +
	\dfrac{2 \dot{x}_0}{n} \cos(nt)
	\\
	- \dfrac{2 f_x}{n^2}(nt - \sin(nt)) +
       \dfrac{2 f_y}{n^2}(2-\dfrac{3}{4}n^2 t^2 - 2\cos(nt))
\end{matrix}
\\
	z \quad = \quad z_0 \cos(nt) +
	\dfrac{\dot{z_0}}{n} \sin(nt) +
	\dfrac{f_z}{n^2}(1-\cos(nt))
\end{cases}
\tag{w9.12}
$$
and their derivatives:
$$
\hspace{-8.5em} % Pull equation closer to the left
\begin{cases}
	\dot{x} \quad = \quad
	\dot{x_0} \cos(nt) + 
	\left( 3 n x_0 + 2 \dot{y_0} \right) \sin(nt) 
	+\dfrac{f_x}{n}\sin(nt) + 
	\dfrac{2 f_y}{n}(1 - \cos(nt))
\\
\begin{matrix}
	\dot{y} \quad = \quad - 
	6 n x_0 - 3 \dot{y_0} +
	\left( 6 n x_0 + 4 \dot{y_0} \right) \cos(nt) -
	2 \dot{x}_0\sin(nt)
	\\
	- \dfrac{2 f_x}{n}(1 - \cos(nt)) +
       \dfrac{2 f_y}{n}(\dfrac{3}{2}n t + 2\sin(nt))
	\hspace{-7.7em}
\end{matrix}
\\
	z \quad = \quad - z_0 n \sin(nt) +
	\dot{z_0} \cos(nt) +
	\dfrac{f_z}{n}(\sin(nt))
\end{cases}
$$
Well, that escalated quickly. What does all this crap even mean? But [[dont_panic.jpg|don't panic]]; for our purposes these equations can often be simplified significantly, and it turns out that by studying these equations analytically, the dynamics become pretty easy to understand.

You may have noticed that the Clohessy-Wiltshire equations return three cartesian coordinates. To get started, we have to start at the beginning: by defining the coordinate system used by the CW equations and what assumptions they're based on.

```ad-note
title: Note

While I don't find [[Wakker]] particularly helpful in building insight into this part of the theory, the lecuturer has put together some fantastic lecture videos that do a much better job. In fact, since this companion is limited by the fact that it is text-based, there is little that I can offer to improve on those videos. So go watch them.

Instead, this section will focus on **supplementing** this lecture, particularly with some math blocks, coding exercises, and examples.
```
___
## Title
___
## Sketch (delete afterwards)
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

$$
\hspace{-6em} % Pull equation closer to the left
\begin{cases}
\begin{matrix}
	x \quad = \quad \left( 4 x_0 + \dfrac{2 \dot{y_0}}{n} \right) + 
	\dfrac{\dot{x_0}}{n} \sin(nt) - 
	\left( 3 x_0 + \dfrac{2 \dot{y_0}}{n} \right) \cos(nt) 
	\\
	+\dfrac{f_x}{n^2}(1-\cos(nt)) + 
	\dfrac{2 f_y}{n^2}(nt - \sin(nt))
	\hspace{-4em}
\end{matrix}
\\
\begin{matrix}
	y \quad = \quad \left( y_0 - \dfrac{2 \dot{x_0}}{n} \right) - 
	3 \left( 2 x_0 + \dfrac{\dot{y_0}}{n} \right) nt +
	2 \left( 3 x_0 + \dfrac{2 \dot{y_0}}{n} \right) \sin(nt) +
	\dfrac{2 \dot{x}_0}{n} \cos(nt)
	\\
	- \dfrac{2 f_x}{n^2}(nt - \sin(nt)) +
       \dfrac{2 f_y}{n^2}(2-\dfrac{3}{4}n^2 t^2 - 2\cos(nt))
\end{matrix}
\\
	z \quad = \quad z_0 \cos(nt) +
	\dfrac{\dot{z_0}}{n} \sin(nt) +
	\dfrac{f_z}{n^2}(1-\cos(nt))
\end{cases}
\tag{w9.12}
$$