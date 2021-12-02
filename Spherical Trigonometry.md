# Spherical Trigonometry - a refresher
Often when we do trigonometry, our triangles have nice, straight lines because they are mapped to a flat plane. In [spherical trigonometry](https://en.wikipedia.org/wiki/Spherical_trigonometry), the triangles are instead mapped to a sphere, and our nice cosine rules no longer apply. Instead, we need new formulas to relate sides and angles. This page lists a few.

![[spherical_trigonometry.png]]

Consider the triangle above. It is mapped to a sphere, and as such its sides are curved. There are three laws from spherical trigonometry that we can use to relate the angles and the sides, which will pop up in Astrodynamics as well.
1. **The law of sines**: $$\dfrac{\sin(A)}{\sin(\alpha)} = \dfrac{\sin(B)}{\sin(\beta)} = \dfrac{\sin(C)}{\sin(\gamma)}$$
2. **The law of cosines for sides**: 
$$\cos(A) = \cos(B)\cos(C) + \sin(B)\sin(C)\cos(\alpha)$$ 
$$\cos(B) = \cos(A)\cos(C) + \sin(A)\sin(C)\cos(\beta)$$
$$\cos(C) = \cos(A)\cos(B) + \sin(A)\sin(B)\cos(\gamma)$$
3. **The law of cosines for angles**: 
$$\cos(\alpha) = -\cos(\beta)\cos(\gamma) + \sin(\beta)\sin(\gamma)\cos(A)$$ 
$$\cos(\beta) = -\cos(\alpha)\cos(\gamma) + \sin(\alpha)\sin(\gamma)\cos(B)$$
$$\cos(\gamma) = -\cos(\alpha)\cos(\beta) + \sin(\alpha)\sin(\beta)\cos(C)$$
___