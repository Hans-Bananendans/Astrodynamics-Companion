# Derivation - N-body constant total energy

```ad-note
title: Note: A less detailed derivation can be found on page 29 of the [[Wakker|Wakker book]].
```

First, let's keep equation $\text{w2.3}$ close on hand, as we will need it in a moment:
$$m_i \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \bar{r}_{ij} \tag{w2.3}$$

According to the [[N-body problem - Integrals of Motion#Derivation recipe|derivation recipe]], we start this derivation by taking the scalar product between $d\bar{r}_i/dt$ and equation $\text{w2.3}$, and sum over $i$:

$$\sum_i m_i \dfrac{d\bar{r}_i}{dt} \cdot \dfrac{d^2 \bar{r}_i}{dt^2} = \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \dfrac{d\bar{r}_i}{dt} \cdot \bar{r}_{ij} \tag{w2.15a}$$

We can manipulate both sides of this equation until we receive a form that is convenient for us. So grab a drink, strap in, and let's see if we can get through this.
___
## Manipulating the left-hand side
$$\sum_i m_i \dfrac{d\bar{r}_i}{dt} \cdot \dfrac{d^2 \bar{r}_i}{dt^2} $$

By virtue of the [chain rule](https://en.wikipedia.org/wiki/Chain_rule), we can also write this like so:

$$\dfrac{d}{dt} \left( \sum_i \dfrac{1}{2} m_i \dfrac{d \bar{r}_i}{dt} \cdot \dfrac{d \bar{r}_i}{dt} \right)$$

```ad-note
title: I want more details!
icon: paperclip
collapse: closed
color: 180,180,180

To show you why we can write this:

$$\sum_i m_i \dfrac{d\bar{r}_i}{dt} \cdot \dfrac{d^2 \bar{r}_i}{dt^2}  = \dfrac{d}{dt} \left( \sum_i \dfrac{1}{2} m_i \dfrac{d \bar{r}_i}{dt} \cdot \dfrac{d \bar{r}_i}{dt} \right) \tag{r1}$$

remember the chain rule:
$$\dfrac{d}{dt} f(y) = f'(y) \cdot \dfrac{dy}{dt} \tag{r2}$$

where $y$ is some function of $t$. Suppose you wish to know the derivative of the function $1/2 y^2$. Using the chain rule, its derivative looks like this:

$$\dfrac{d}{dt} \left( \dfrac{1}{2}y^2 \right) = y \cdot \dfrac{dy}{dt} \tag{r3}$$

Keep this in mind. Now we are going to make a substitution to equation $\text{r1}$; We will replace every term $d\bar{r}_i/dt$ with $y$. The left-hand side of $\text{r1}$ then becomes:

$$\sum_i m_i y \cdot \dfrac{dy}{dt} \tag{r4}$$

Compare $\text{r3}$ and $\text{r4}$. Can you see that they contain the same term? If we substitute expression $\text{r3}$ into $\text{r4}$, we get:

$$\sum_i m_i y \cdot \dfrac{dy}{dt} = \sum_i m_i\dfrac{d}{dt} \left( \dfrac{1}{2}y^2 \right) = \dfrac{d}{dt} \left(\sum_i \dfrac{1}{2} m_i y \cdot y \right)\tag{r5}$$

If we now substitute $d\bar{r}_i/dt$ back in for $y$:

$$\sum_i m_i \dfrac{d\bar{r}_i}{dt} \cdot \dfrac{d^2 \bar{r}_i}{dt^2}  = \dfrac{d}{dt} \left( \sum_i \dfrac{1}{2} m_i \dfrac{d \bar{r}_i}{dt} \cdot \dfrac{d \bar{r}_i}{dt} \right) \tag{r6}$$

And [there it is](../media/there_it_is.gif). Remember equation $\text{r3}$ well, it will likely not be the last time you see this trick being used to manipulate differential operators.
```

Remember that the derivative of the position vector $\bar{r}_i$ is equal to the velocity of $i$. With this, we can write the above as:

$$\dfrac{d}{dt} \left( \sum_i \dfrac{1}{2} m_i \bar{V}_i \cdot \bar{V}_i \right)$$

and by using [[Vector Identities#Vector identity 1|Vector identity 1]] from the list, we get:
$$\dfrac{d}{dt} \left( \sum_i \dfrac{1}{2} m_i V_i^2 \right)$$
___
## Manipulating the right-hand side
To remain consistent with the [[Wakker|Wakker book]], we're going to give this side a nickname $K$:
$$K = \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \dfrac{d\bar{r}_i}{dt} \cdot \bar{r}_{ij}$$

We first rewrite the relative position vector $\bar{r}_{ij}$ as $\bar{r}_{j} - \bar{r}_{i}$:

$$K = \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \dfrac{d\bar{r}_i}{dt} \cdot (\bar{r}_{j} - \bar{r}_{i})$$

Because [differentiation is linear](https://en.wikipedia.org/wiki/Differentiation_rules#Differentiation_is_linear), it is true that:
$$\dfrac{d(\bar{r}_j-\bar{r}_i)}{dt} = \dfrac{d\bar{r}_j}{dt} - \dfrac{d\bar{r}_i}{dt}$$

This allows us to rewrite $K$ to:
$$K = -\sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \dfrac{d(\bar{r}_j-\bar{r}_i)}{dt} \cdot (\bar{r}_{j} - \bar{r}_{i}) + \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \dfrac{d\bar{r}_j}{dt} \cdot (\bar{r}_{j} - \bar{r}_{i})$$

The second part of this equation can actually be written as $-K$. Why this is is not so obvious, but of course the book skips right over the details. See this block for these details:

```ad-note
title: Why that term is indeed equal to $-K$
icon: paperclip
collapse: closed
color: 180,180,180

Why are we allowed to write:

$$\sum_{i=1}^n \sum_{\substack{j=1\\j\neq i}}^n \dfrac{m_i m_j}{r_{ij}^3} \dfrac{d\bar{r}_i}{dt} (\bar{r}_j - \bar{r}_i)
=
- \sum_{i=1}^n \sum_{\substack{j=1\\j\neq i}}^n \dfrac{m_i m_j}{r_{ij}^3} \dfrac{d\bar{r}_j}{dt} (\bar{r}_j - \bar{r}_i)
\tag{r1}$$

The secret lies in the fact that when we have double summations, we can exchange the indices:
$$
\sum_{i=1}^m \sum_{j=1}^n a_{i,j}
=
\sum_{j=1}^m \sum_{i=1}^n a_{i,j}
\tag{r2}$$

Or equivalently:
$$
\sum_{i=1}^m \sum_{j=1}^n a_{i,j}
=
\sum_{i=1}^m \sum_{j=1}^n a_{j,i}
\tag{r3}$$

However, we may generally only do so when the summation indices are **independent**. So for example, in the following case the indices may **not** be exchanged:


$$
\sum_{i=1}^m \sum_{j=1}^i a_{i,j}
\neq
\sum_{i=1}^m \sum_{j=1}^i a_{j,i}
\tag{r4}$$

because the second summation has $i$ as its upper boundary. Now, in the double summation that we are considering, we have an extra condition that ensures that for one of the summations $j\neq i$. The question is now: Are we still allowed exchange indices for this double summation? Or do the indices now dependent on each other in such a way that we will get a different answer?

The answer is that **yes**, we are indeed still allowed to exchange the indices. To show why this is, we're going to visualize all the terms for the following summation: 
$$
\sum_{i=1}^n \sum_{j=1}^n a_{i,j}
\quad \rightarrow \quad
\begin{matrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots  & \vdots  & \ddots & \vdots  \\
a_{n,1} & a_{n,2} & \cdots & a_{n,n} 
\end{matrix} \tag{r5}$$

Note that the summation operators are almost identical to those of $\text{r1}$, even though we are just counting terms $a_{i,j}$. We are just missing the condition $j\neq i$. Let's add it:

$$ 
\sum_{i=1}^n \sum_{\substack{j=1\\j\neq i}}^n a_{i,j}
\quad \rightarrow \quad \bcancel{
\begin{matrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots  & \vdots  & \ddots & \vdots  \\
a_{n,1} & a_{n,2} & \cdots & a_{n,n} 
\end{matrix}}  \tag{r6}$$

The condition $i \neq j$ on the summation essentially ensures that all terms $a_{i,j}$ for which $i=j$ are not counted in the summation. So we have crossed them out (they are all on the diagonal), and we will only sum the remaining terms.

Now let's change the indices of summation by exchanging $a_{i,j}$ for $a_{j,i}$. Will we still sum the same terms?

$$ 
\sum_{i=1}^n \sum_{\substack{j=1\\j\neq i}}^n a_{j,i}
\quad \rightarrow \quad \bcancel{
\begin{matrix}
a_{1,1} & a_{2,1} & \cdots & a_{n,1} \\
a_{1,2} & a_{2,2} & \cdots & a_{n,2} \\
\vdots  & \vdots  & \ddots & \vdots  \\
a_{1,n} & a_{n,2} & \cdots & a_{n,n} 
\end{matrix}} \tag{r7}$$

Yes. Even though the array of numbers is transposed, the terms that we are adding up is still the same. So indeed, exchanging the indices on the double summation with the $i \neq j$ condition seems to work fine. 

So let's try exchanging all the indices for the left-hand side of $\text{r1}$:

$$\sum_{i=1}^n \sum_{\substack{j=1\\j\neq i}}^n \dfrac{m_i m_j}{r_{ij}^3} \dfrac{d\bar{r}_i}{dt} (\bar{r}_j - \bar{r}_i)
=
\sum_{i=1}^n \sum_{\substack{j=1\\j\neq i}}^n \dfrac{m_j m_i}{r_{ji}^3} \dfrac{d\bar{r}_j}{dt} (\bar{r}_i - \bar{r}_j)
\tag{r8}$$

$$=
- \sum_{i=1}^n \sum_{\substack{j=1\\j\neq i}}^n \dfrac{m_i m_j}{r_{ij}^3} \dfrac{d\bar{r}_j}{dt} (\bar{r}_j - \bar{r}_i)
\tag{r9}$$

The last step is possible because of three reasons:
- Multiplication is [commutative](https://en.wikipedia.org/wiki/Commutative_property), so we can write: $$m_j m_i = m_i m_j$$ 

- The length of vectors $\bar{r}_{ij}$ and $\bar{r}_{ji}$ are identical, so: $$r_{ij}=r_{ji}$$
- Subtraction is [anticommutative](https://en.wikipedia.org/wiki/Anticommutative_property), so we can swap the bracketed term around if we introduce a minus sign:
$$(\bar{r}_i - \bar{r}_j) = -(\bar{r}_j - \bar{r}_i)$$

So I hope that based on this you understand why $\text{r1}$ is true.

```

Anyway, now we have:
$$K = -\sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \dfrac{d(\bar{r}_j-\bar{r}_i)}{dt} \cdot (\bar{r}_{j} - \bar{r}_{i}) - K$$

$$2K = -\sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \dfrac{d(\bar{r}_j-\bar{r}_i)}{dt} \cdot (\bar{r}_{j} - \bar{r}_{i})$$

Now we divide by 2, and we re-introduce relative position vector $\bar{r}_{ij}$:

$$K = - \dfrac{1}{2} \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}} \dfrac{d\bar{r}_{ij}}{dt} \cdot \bar{r}_{ij}$$

$$ = \dfrac{d}{dt} \left( - \dfrac{1}{2} \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}}  \bar{r}_{ij} \cdot \bar{r}_{ij} \right)$$

Once again employing [[Vector Identities#Vector identity 1|Vector identity 1]], we can rewrite this further:

$$K = \dfrac{d}{dt} \left( - \dfrac{1}{2} \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r^3_{ij}}  r^2_{ij} \right)$$
$$ = \dfrac{d}{dt} \left( - \dfrac{1}{2} \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r_{ij}} \right) \tag{w2.16}$$

```ad-note
title: ## ** !!! This section is still under construction !!! **
icon: hammer
color: 240,200,25
In equation 2.16 in Wakker, the minus sign has disappeared. Where the fuck did it go???
```
___
## Re-combining the two sides
Now we once again write $\text{w2.15a}$, but with the new expressions we obtained for each side:

$$\dfrac{d}{dt} \left( \sum_i \dfrac{1}{2} m_i V_i^2 \right) = \dfrac{d}{dt} \left(\dfrac{1}{2} \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r_{ij}} \right)$$

Integrating both sides yields:

$$ 
\begin{align}
\sum_i \dfrac{1}{2} m_i V_i^2 
\hspace{1.5em} - \hspace{1.5em}
\dfrac{1}{2} \sum_i \sum_{j \neq i} G \dfrac{m_i m_j}{r_{ij}} \hspace{2.5em} = \hspace{2.5em} 
C 
\hspace{3.5em} \tag{w2.17}
\\
\hspace{0em} 
\begin{matrix} \text{total kinetic} \\ \text{energy} \end{matrix}
\hspace{5em} 
\begin{matrix} \text{total potential} \\ \text{energy} \end{matrix}
\hspace{5em} 
\begin{matrix} \text{total mechanical} \\ \text{energy} \end{matrix}
\end{align}
$$

This equation has two terms, one of which corresponds to the total **kinetic** energy in the system, and the other to the total **potential** energy of the system. So as the bodies move closer to each other, their relative velocity will increase, trading potential energy for kinetic energy. And vice versa when moving away from each other. However, equation $\text{w2.17}$ shows that the total amount of (mechanical) energy remains constant.

This last piece of information forms the tenth integral of motion:
$$\mathcal{E}_{kin} + \mathcal{E}_{pot} = C$$
___