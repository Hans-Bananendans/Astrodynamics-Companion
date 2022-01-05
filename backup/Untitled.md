To find the perturbing acceleration, we look at the second term of equation $\text{w4.4}$, and modify it for the given situation. Since we have only one disturbing body, the summation is just one term.

$$ \bar{a}_d = G m_d  \left( \dfrac{\bar{r}_{d} - \bar{r}_{i}}{r_{id}^3} -  \dfrac{\bar{r}_{d} }{r_{id}^3}\right) \tag{r1}$$

Nice, but we would actually like to have a scalar form of this equation, rather than a vectorial form. This will allow us to compare the magnitude $a_d$ with $a_k$. So we simplify equation $\text{r1}$ by first substituting $\bar{r}_{id} = \bar{r}_d - \bar{r}_i$ and performing a little trick: Squaring the bracketed term, while at the same time taking the square root of it:
$$ \bar{a}_d = G  \left( \dfrac{\bar{r}_{id}}{r_{id}^3} -  \dfrac{\bar{r}_{d} }{r_{id}^3}\right) = G m_d \sqrt{\left( \dfrac{\bar{r}_{id}}{r_{id}^3} -  \dfrac{\bar{r}_{d} }{r_{id}^3}\right) \cdot \left( \dfrac{\bar{r}_{id}}{r_{id}^3} -  \dfrac{\bar{r}_{d} }{r_{id}^3}\right)} \tag{r2}$$

$$  = G m_d \sqrt{ \dfrac{\bar{r}_{id} \cdot \bar{r}_{id}}{r_{id}^6} + \dfrac{\bar{r}_{d} \cdot \bar{r}_{d} }{r_{id}^6} - 2 \dfrac{\bar{r}_d \cdot \bar{r}_{id}}{r_d^3 r_{id}^3}} \tag{r3}$$

Given [[Vector Identities#Vector identity 1|Vector identity 1]] and the definition of the [dot product](https://en.wikipedia.org/wiki/Dot_product), we can rewrite this to:

$$  = G m_d \sqrt{ \dfrac{r_{id}^2}{r_{id}^6} + \dfrac{r_{d}^2}{r_{id}^6} - 2 \dfrac{r_d r_{id} \cos\beta}{r_d^3 r_{id}^3}} = G m_d \sqrt{ \dfrac{1}{r_{id}^4} + \dfrac{1}{r_{id}^4} - \dfrac{2 \cos\beta}{r_d^2 r_{id}^2}} \tag{r4}$$

At this point we have eliminated every vector, and we may as well write $\bar{a}_d$ as $a_d$:

$$ a_d = G m_d \sqrt{ \dfrac{1}{r_{id}^4} + \dfrac{1}{r_{id}^4} - \dfrac{2 \cos\beta}{r_d^2 r_{id}^2}} \tag{r4}$$