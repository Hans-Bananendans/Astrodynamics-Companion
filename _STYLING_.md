## General styling rules
See [markdown cheat sheet](https://www.markdownguide.org/cheat-sheet)


1. Sections are to be separated with a horizontal rule (`___`).
2. Pages that contain multiple sections must have an index at the top for quick navigation.
3. If a page has an index, the end of every section should feature a quick shortcut back to the index. Syntax: `[[<page name>#Index|^]]`
4. Equations must numbered. They can be numbered in two ways:
	1. Equations that appear in the Wakker reader must be referenced with the equation number from Wakker.
	2. Equations that do not appear in Wakker (such as for intermediate math) can be annotated with a relative numbering (EID#1)
	The standard tagging formatting is:
	$$
  \tag{14.2}
  y = ax + b
  $$
5. Examples, worked-out exercises, extra math, code examples, assumptions, warnings, etc. should go in their own Admonition blocks for cleanliness and to prevent burying them in walls of text.
6. Media (images, videos, etc) go in the media folder (`./media/`), which may be sorted or unsorted itself.
7. Footnotes can be applied in the standard Markdown way (`[^1]`). The Markdown renderer automatically puts them at the very bottom of the page, and they cannot be easily sorted by section. However, each footnote has a clickable reference in the text, and a clickable return button at the footnote, so navigation is painless enough for this to be a problem.

## Figure styling
Figures should be set up such that they can be completely understood on both light and dark backgrounds. Ideally, a figure consists of a clear arrangement of coloured elements, with a transparent background. Png and other image formats that have an alpha channel are therefore preferable (and not jpgs, etc.).

To ensure sufficient colour contrast on both light and dark backgrounds, you can use the colour chart defined below.
![[styling.png]]
A note regarding the neons: Each figure should be easily readable and simple to understand. Do not cram in as many things as you can, and if you have to use the neons to distinguish things, it could be an indication that you could be arranging your figures better. The more colours you use, the less distinct they appear to the reader. Therefore, try to use the neons as little as possible (they're ugly af anyway).

## Standard Admonition elements
[FontAwesome icon repo](https://fontawesome.com/v6.0/icons?q=construction&s=solid%2Cbrands) (not all icons work!).

Note block
```ad-note
title: Note


```

Example block
```ad-example
title: Example


```

Tip block
```ad-tip
title: Tip
icon: lightbulb


```

Question/exercise
```ad-question
title: 
color: 215,30,30


```

Warning block
```ad-warning
title: 


```

Assumption block
```ad-warning
title: 
color: 200,80,225


```

Math block (open/close based on situation)
```ad-note
title: Title
icon: paperclip
collapse: open
color: 180,180,180


```

Generic code block
````ad-abstract
title: Title
icon: file-code
collapse: open

```js

```

````

Python code block
````ad-abstract
title: Title
icon: python
collapse: open
color: 45,215,60

```py

```

````

Under construction notice
```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25


```

hammer
toolbox
shovel
wrench

---

## Standard Admonition elements - Examples
Note block
```ad-note
title: Note

Soylent green is people.

```

Example block
```ad-example
title: Example 1

Strange women lying in ponds distributing swords is no basis for a system of government.

```

Tip block
```ad-tip
title: Tip
icon: lightbulb

Do not lick lantern posts when it is freezing outside. 

```

Question/exercise
```ad-question
title: Question
color: 215,30,30

How long is a piece of string?

```

Warning block
```ad-warning
title: Warning!

There is a snake in my boot!
```

Assumption block
```ad-warning
title: Assumption 1
color: 200,80,225

Assume the Earth is flat.
```

Math block (open/close based on situation)
```ad-note
title: Derivation
icon: paperclip
collapse: open
color: 180,180,180

This can be rewritten as:
$$ g = g_0 \dfrac{R_e^2}{(R_e+h)^2} = \dfrac{g_0}{\left(1+\dfrac{h}{R_e}\right)^2}$$

We can substitude this in the equation given earlier:
$$ g_0 dz = g dh = \dfrac{g_0}{\left(1+\dfrac{h}{R_e}\right)^2} dh $$

We can now integrate this equation. The left hand we integrate from $0$ to $z$, whilst we integrate the right hand side from $0$ to $h$:

$$ \int^z_0 dz^* = \int^h_0 \dfrac{1}{\left(1+\dfrac{h^*}{R_e}\right)^2} dh^*$$

The left hand side can be reworked to a slightly easier to integrate form:
$$ \dfrac{1}{\left(1+\dfrac{h^*}{R_e}\right)^2} = \dfrac{1}{\left(\dfrac{1}{R_E}\left(R_E+h^*\right)\right)^2} = \dfrac{1}{\dfrac{1}{R_E^2}\left(R_E+h^*\right)^2} = \dfrac{R_E^2}{\left(R_E+h^*\right)^2} $$

```

Generic code block
````ad-abstract
title: HelloWorld.java
icon: file-code
collapse: open

```js
public class HelloJava {
	public static void main(String args[]) {
		System.out.println("Hello World!");
	}
}
```

````

Python code block
````ad-abstract
title: filename.py
icon: python
collapse: open
color: 45,215,60

```py
import numpy as np

rE = 6371 # [km]
h1 = 320 # [km]
r1 = rE+h1
r2 = 384400 # [km]

# Eccentricity of transfer orbit
et = (r2-r1)/(r1+r2)

# Semi-major axis of transfer orbit
at = 0.5*(r1+r2)
```

````

Under construction notice
```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25

- [ ] Improve this
- [ ] Also improve this
- [ ] And let's not forget about this
- [ ] Maybe this improvement too

```