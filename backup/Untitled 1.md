Start with:

$$a_d = G m_d \sqrt{\dfrac{1}{r_{id}^4} + \dfrac{1}{r_{d}^4} - \dfrac{2 \cos{\beta}}{r_{id}^2 r_{d}^2}} \tag{w4.10}$$

and 

$$
\gamma = r_i / r_d
\hspace{2em} , \hspace{2em} 
\cos{\beta} = \dfrac{r_d - r_i \cos{\alpha}}{r_{id}} 
\hspace{2em} , \hspace{2em} 
r_{id}^2 = r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha \tag{r1}$$

Simply substitute the equations $\text{r1}$ into $\text{w4.10}$:

$$a_d = G m_d \sqrt{\dfrac{1}{r_{id}^4} + \dfrac{1}{r_{d}^4} - \dfrac{2 (r_d - r_i \cos{\alpha})}{r_{id}^3 r_{d}^2}} \tag{r2}$$


$$ = G m_d \sqrt{\dfrac{1}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2} + \dfrac{1}{r_{d}^4} - \dfrac{2 (r_d - r_i \cos{\alpha})}{r_{d}^2 [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}} \tag{r3}$$

For our first trick, we will multiply everything inside the square root by $r_{d}^4$ divided by itself. The numerator we will use to manipulate the fractions, whilst the denominator we will extract from the square root:
$$ a_d = G m_d \sqrt{ \dfrac{r_{d}^4}{r_{d}^4} \left\{ \dfrac{1}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2} + \dfrac{1}{r_{d}^4} - \dfrac{2 (r_d - r_i \cos{\alpha})}{r_{d}^2 [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}} \right\} }  \tag{r4}$$

$$ = G \dfrac{m_d}{r_{d}^2} \sqrt{  \dfrac{r_{d}^4}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2} + 
\dfrac{r_{d}^4}{r_{d}^4} - 
\dfrac{2 (r_d - r_i \cos{\alpha}) r_{d}^4}{r_{d}^2 [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}} }  \tag{r5}$$

The middle term inside the square root is easy to deal with, but the two others look pretty hairy. Let's look at them separately:
$$ \text{SQRT TERM \#1} = \dfrac{r_{d}^4}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2} \hspace{8em}$$

$$= \dfrac{1/r_{d}^4}{1/r_{d}^4} \cdot \dfrac{r_{d}^4}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2}$$

$$ = \dfrac{1}{1/r_{d}^4 \cdot[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^2}$$

$$ = \dfrac{1}{[1/r_{d}^2 \cdot (r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha)]^2}$$

$$ = \dfrac{1}{[r_{i}^2/r_{d}^2 + r_{d}^2/r_{d}^2 - 2 \cdot r_{i}/r_{d} \cdot r_{d}/r_{d} \cdot \cos \alpha]^2}$$

$$ = \dfrac{1}{[\gamma^2 + 1 - 2 \gamma \cos \alpha]^2}$$

And for the other term:
$$ \text{SQRT TERM \#3} = \dfrac{2 (r_d - r_i \cos{\alpha}) r_{d}^4}{r_{d}^2 [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}} \hspace{8em}$$

$$ = \dfrac{2 (r_d - r_i \cos{\alpha}) r_{d}^2}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}$$

$$ = \dfrac{1/r_{d}}{1/r_{d}} \cdot \dfrac{1/r_{d}^2}{1/r_{d}^2} \cdot \dfrac{2 (r_d - r_i \cos{\alpha}) r_{d}^2}{[r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}$$

$$ = \dfrac{1/r_{d}}{1/r_{d}} \cdot \dfrac{2 (r_d - r_i \cos{\alpha}) }{1/r_{d}^2 \cdot [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}$$

$$ = \dfrac{2 (r_d - r_i \cos{\alpha}) \cdot 1/r_{d} }{1/r_{d}^3 \cdot [r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha]^{3/2}}$$

$$ = \dfrac{2 (r_d/r_d - r_i/r_d \cdot \cos{\alpha}) }{[1/r_{d}^2 \cdot (r_{i}^2 + r_{d}^2 - 2 r_{i} r_{d} \cos \alpha)]^{3/2}}$$

$$ = \dfrac{2 (r_d/r_d - r_i/r_d \cdot \cos{\alpha}) }{[r_{i}^2/r_{d}^2 + r_{d}^2/r_{d}^2 - 2 \cdot r_{i}/r_{d} \cdot r_{d}/r_{d} \cdot \cos \alpha]^{3/2}}$$

$$ = \dfrac{2 (1 - \gamma \cos{\alpha}) }{[\gamma^2 + 1 - 2 \gamma \cos \alpha]^{3/2}}$$


If we substitute $\text{SQRT TERM \#1}$ and $\text{SQRT TERM \#3}$ back into equation $\text{r5}$, we get:

$$a_d = G \dfrac{m_d}{r_d^2} 
\sqrt{
1 +
\dfrac{1}{[1+\gamma^2 - 2 \gamma \cos(\alpha)]^2} -
\dfrac{2(1-\gamma \cos(\alpha))}{[1+\gamma^2 - 2 \gamma \cos(\alpha)]^{3/2}}
}  
\tag{w4.11}$$