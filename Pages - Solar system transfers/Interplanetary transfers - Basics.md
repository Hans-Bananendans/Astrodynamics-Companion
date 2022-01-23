# Interplanetary transfers - Basics

```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25
```

<!-- Wakker section 18.1, 18.3 -->

Basic assumptions for most interplanetary transfer calculations:
 - Assume departure body is Earth
 - Use Keplerian trajectories: permits two-body problem assumptions.

Sequence of events:
1. **Escape** the graviatational field of the departure planet
2. **Patch** the planetocentric to the heliocentric trajectory
3. Follow a **transfer trajectory** from departure to target planet
4. **Patch** the heliocentric to the planetocentric trajectory
5. **Enter** the graviational fields of the target planets
6. **Impact**, **capture**, or **flyby**

Patched conics assumptions:
 - Assume planetary orbits are **circular** (Mercury ($e\approx0.2$) and Pluto ($e\approx0.25$) being outliers)
 - Assume planetary obits are **coplanar** (Mercury ($i\approx7^\circ$) and Pluto ($i\approx17^\circ$) being outliers)

```ad-note
title: Title
icon: paperclip
collapse: open
color: 180,180,180
$$\dfrac{1}{r_{Earth}} \cdot \dfrac{r_{Earth}+r_{Mars}}{r_{Earth}+r_{Mars}} - \dfrac{1}{r_{Earth}+r_{Mars}} \cdot \dfrac{r_{Earth}}{r_{Earth}}$$
$$ = \dfrac{r_{Earth}+r_{Mars}}{r_{Earth}(r_{Earth}+r_{Mars})} - \dfrac{r_{Earth}}{r_{Earth}(r_{Earth}+r_{Mars})} = \dfrac{r_{Mars}}{r_{Earth}(r_{Earth}+r_{Mars})}$$

```

Baby's first interplanetary trajectory -> Hohmann transfer

\<image of whole transfer>
\<image of departure situation>
\<image of target situation>
\<image of synodics>


![[transfer_planetary_coplanar_generic.png]]
