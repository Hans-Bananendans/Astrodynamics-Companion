# The Equation Cabinet
This page contains a (non-exhaustive) list of useful equations and relations that can be used to solve many different astrodynamical problems. The reason it exist is to save time on page-flipping through [[Wakker]] and internet surfing.
___

A medicine cabinet can be used in case of medical problems. Similarly, this page can be used in case of mathematical problems. Though useful, both should come with a warning about correct usage, so the user does not develop a substance dependence. As such, let me give you a warning:


> [!warning] Warning: Do not become dependent on this list when studying for your exam!


Instead, I suggest depending on derivations, graphical representations, and most of all, your own understanding of the theory. Try learning a minimum number of foundational equations by heart (such as [[Vis-viva Equation|vis-viva]], [[Kepler's Laws|Kepler's laws]], trajectory equation, N-body equations of motion) and learn how to derive the rest from those. Equations that have hellish derivations will not be asked on the exam; if you need them, they will probably be given. After all, the point of the exam is to test your knowledge about astrodynamics, not to do a bunch of flashy but pointless math for three hours. Moreover, you'll need to be able to recognise when you are and when you are not allowed to apply an equation, and you'll likely want to know what the underlying assumptions are. You won't do either by pulling a bunch of equations out of a hat.

Therefore, learning the equations on this page by heart is not very helpful, and it is not going to provide you with much insight or understanding. So use the Equation Cabinet at your own risk; [do not become an equation junkie](equation_junkie.gif).
___

## Two-body problem
| Name | Expression |
|:------|:------|
| Vis-viva | $\frac{1}{2}V^2 - \dfrac{\mu}{r} = \mathcal{E}$|
| Energy of ellpitical orbits | $\mathcal{E} = -\dfrac{\mu}{2a}$|
| Kepler's 2nd law | $\dfrac{dA}{dt} = \frac{1}{2} r^2 \dfrac{d\theta}{dt} = \frac{1}{2} h = \text{constant}$|
| Kepler's 3rd law | $\dfrac{a^3}{T^2} = \dfrac{\mu}{4 \pi^2}$|
| Semi-latus rectum | $p = \dfrac{h^2}{\mu} = a(1-e^2)$|
| Trajectory equation | $r = \dfrac{p}{1+e \cos\theta} = a(1-e \cos E)$|
| Eccentricity vector | $\bar{e} = \dfrac{1}{\mu}\bar{V} \times \bar{h}-\dfrac{\bar{r}}{r} = \dfrac{1}{\mu}\left[ \left(V^2-\dfrac{\mu}{r}\right)\bar{r}-(\bar{r}\cdot\bar{V})\bar{V}\right]$|
| Inclination | $i = \arccos \left( \dfrac{h_z}{\|\bar{h}\|} \right)$|
| Angular momentum | $\bar{h} = \bar{r} \times \bar{V}$|
| Gravitational acceleration | $\ddot{\bar{r}} = -\dfrac{\mu}{r^3}\bar{r}$ |
| SMA of ellpise | $a = \frac{1}{2}(r_p+r_a)$|
| SOI radius | $r_{SOI} = a\left( \frac{m_i}{m_{primary}}\right)^{2/5}$|
|  | |
|  | |
|  | |
|  | |
|  | |
|  | |
|  | |
