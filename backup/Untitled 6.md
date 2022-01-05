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

Now, in the double summation that we are considering, we have an extra condition that ensures that for one of the summations $j\neq i$. The question is now: Are we still allowed exchange indices for this double summation? Or do the indices now dependent on each other in such a way that we will get a different answer?

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