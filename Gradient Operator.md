# The Gradient Operator

The gradient is a differential operator that when applied to a quantity, it finds the direction in which this quantity changes most rapidly. If you would take the gradient of a quantity $f$, it will return a vector with the partial derivative of $f$ with respect to every dimension of the manifold that $f$ operates in. For most Astrodynamics problem, the manifold is either 2D or 3D for Newtonian descriptions, or 4D when using the space-time manifold.

The gradient operator is also referred to as the nabla operator, and is denoted by $\bar{\nabla}$.

```ad-example

For a quantity $f$ operating in 3D space, the gradient is:

$$\text{grad} f = \bar{\nabla} f = \dfrac{\partial f}{\partial x} \hat{i} + \dfrac{\partial f}{\partial y} \hat{j} + \dfrac{\partial f}{\partial z} \hat{k} =
\begin{bmatrix}
\dfrac{\partial f}{\partial x} \\
\dfrac{\partial f}{\partial y} \\
\dfrac{\partial f}{\partial z}
\end{bmatrix}
$$
```
___