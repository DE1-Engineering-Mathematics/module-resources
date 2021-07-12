<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/javascript" src="tutorialSheetScripts.js"> </script>
<link rel="stylesheet" type="text/css" media="all" href="styles.css">

# Sequence, Series, Limits and Convergence Tutorial Sheet, Sheet #5B

### Learning targets
* Suggest formulae for the $n$th term of given sequences
* Use the binomial distribution
* Calculate the sum of a series
* Use the standard summation formulae 
* Identify the limiting values of sequence 
* Determine when/whether a series is (absolutely) convergent

### Additional Resources
* [SJC - Sequence, Series](https://youtu.be/kUbzTJ1UDy4)
* [SJC - Power Series](https://youtu.be/Y2Yfq-IR9iQ)

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Suggest a formula for the $n$th term of the following sequences:

(a) $3, -5, 7, -9, 11,...$
<div class = "answer"> 
This is an Arithmetic Series, with $a_1=3$ and $d=2$.
<br>
Because the numbers alternate from positive to negative we need to include $(-1)^{n+1}$.
<br>
$\Rightarrow\boxed{a_n=(-1)^{n+1}.(2n+1)}$ </div>

(b) $2,\frac{3}{2},\frac{4}{3},\frac{5}{4},\frac{6}{5},...$
<div class = "answer"> 
The numerator of this fraction is an Arithmetic Series, with $a_1=2$ and $d=1$. 

The denominator is also an Arithmetic Series, but with $a_1=1$ and $d=1$.
<br>
$a_n=\frac{2 + (n-1)}{1+(n-1)}$
<br>
$\Rightarrow\boxed{a_n=\frac{n+1}{n}}$ </div>

(c) $\frac{2}{3},\frac{3}{2\times{}4},\frac{4}{3\times{}5},\frac{5}{4\times{}6},\frac{6}{5\times{}7},...$
<div class = "answer">$\Rightarrow\boxed{a_n=\frac{n+1}{n(n+2)}}$</div>

(d) $1, 0,-e^2,0,e^4,...$
<div class = "answer">
$\Rightarrow\boxed{a_n=e^{n-1}\sin\left(\frac{n\pi}{2}\right)}$</div>

-----------------------------------------------------------------------------------

### Problem 2.
Find the third, sixth and ninth term of the sequence given by the formula:

(a) $  \sum_{n=1}^{\infty}\ \left(\frac{n^2-n-6}{n+2}\right) $


<div class = "answer">$\Rightarrow a_3 = \frac{3^2-3-6}{3+2} = \boxed{0} ,
\\ \\ \Rightarrow a_6=\frac{6^2-6-6}{6+2}= \frac{24}{8}=\boxed{3},
\\ \\ \Rightarrow a_9=\frac{9^2-9-6}{9+2}=\frac{66}{11}=\boxed{6}$</div>

(b) $ \sum_{n=1}^{\infty}\ \left(\text{sin⁡}[ \left(n+1\right)\frac{\pi{}}{3}]\right) $

<div class = "answer">$\Rightarrow a_3=\sin(3+1)\frac{\pi{}}{3}=\sin(\frac{4\pi{}}{3})=\boxed{-\frac{\sqrt{3}}{2}},
\\ \\ \Rightarrow a_6=\sin(6+1)\frac{\pi{}}{3}=\sin(\frac{7\pi{}}{3})=\boxed{\frac{\sqrt{3}}{2}},
\\ \\ \Rightarrow a_9=\sin(9+1)\frac{\pi{}}{3}=\sin(\frac{10\pi{}}{3})=\boxed{-\frac{\sqrt{3}}{2}}$</div>

(c) $ \sum_{n=3}^{\infty}\ \left(\binom{n}{2}-\binom{n}{3} \right)$  

Tip: Use the binomial coefficient  $\binom{n}{k}=\frac{n!}{k!(n-k)!}$

<div class = "answer">
In this series, the first term is at $n=3$, so the third term is at $n=5$, the sixth at $n=8$ and the ninth at $n=11$.
$ \Rightarrow a_3=\frac{5!}{2!(5-2)!} - \frac{5!}{3!(5-3)!}=\frac{120}{2\cdot 6} - \frac{120}{3! \cdot 2!}=10-10=\boxed{0},
\\ \\ \Rightarrow a_6=\frac{8!}{2!(8-2)!} - \frac{8!}{3!(8-3)!}=\frac{40320}{2\cdot 720} - \frac{40320}{6 \cdot 120}=28-56=\boxed{-28},\ 
\\ \\ \Rightarrow a_9=\frac{11!}{2!(11-2)!}-\frac{11!}{3!(11-3)!}= 55-165=\boxed{-110}$</div>


-----------------------------------------------------------------------------------

### Problem 3.
Evaluate the following:

(a) $\sum_{n=1}^{20}\left(0.2n+5\right)$
<div class = "answer">
The Sum of an Arithmetic Sequence: <br>
$\Rightarrow S_n= \frac{n}{2}(2a + d(n - 1))
\\ = \frac{20}{2}(2(0.2+5) + (0.2)(20 - 1)) 
\\ = 10*14.2
\\ = \boxed{142}$</div>

(b) $\sum_{n=1}^8n\left(3+2n+n^2\right)$
<div class = "answer">Break down into smaller sequences and use polynomial series identities: <br> 
$\Rightarrow 3\sum_{n=1}^8n \ + \ 2\sum_{n=1}^8n^2 \ +\ \sum_{n=1}^8n^3\ 
\\ = 3(\frac{8(8+1)}{2}) + 2(\frac{8(8+1)(16+1)}{6}) + \frac{64(8+1)^2}{4} 
\\ = 108 + 408 + 1296 \\= \boxed{1812}$</div>

(c) $\sum_{r=1}^nr\left(r+3\right)$
<div class = "answer">Break down into smaller sequences and use polynomial series identities: <br> 
$\Rightarrow \sum_{r=1}^nr^2 \ + 3\sum_{r=1}^nr \\ \\ 
= \frac{n(n+1)(2n+1)}{6} + 3(\frac{n(n+1)}{2}) \\ \\
= \frac{n}{6}((n+1)(2n+1) +9(n+1)) \\ \\
= \frac{n}{6}(2n^2+12n+10) \\ \\
= \frac{n}{3}(n^2+6n+5) \\ \\
=\boxed{\frac{n}{3}\left(n+1\right)\left(n+5\right)}$</div>

(d) $\sum_{r=1}^n{\left(r+1\right)}^3$
<div class = "answer">Break down into smaller sequences and use polynomial series identities: <br> 
$\Rightarrow \sum_{r=1}^nr^3 \ + 3\sum_{r=1}^nr^2 \ +3\sum_{r=1}^nr \ +\sum_{r=1}^n1 \\ \\
= \frac{n^2(n+1)^2}{4} + \frac{n(n+1)(2n+1)}{2} + 3(\frac{n(n+1)}{2}) + n \\ \\
= \frac{n}{4}(n(n+1)^2 + 2(n+1)(2n+1) + 6(n+1) + 4) \\ \\
= \frac{n}{4}(n^3 + 2n^2 + n + 4n^2 + 6n + 2 + 6n + 6 + 4) \\ \\
= \boxed{\frac{n}{4}(n^3 + 6n^2 + 13n + 12)}$</div>

-----------------------------------------------------------------------------------

### Problem 4.
Find the sum of $n$ terms of the following:

(a) $S_n=1^2+3^2+5^2+ . . . +{\left(2n-1\right)}^2$
<div class = "answer">Use the sum of polynomial series identities:
$= 4\sum_{n=1}^nn^2 \ -4\sum_{n=1}^nn \ + \sum_{n=1}^n1 \\ 
= 2(\frac{n(n+1)(2n+1)}{3}) - 4(\frac{2n(n+1)}{2}) + n \\ 
= \frac{n}{3}(2(n+1)(2n+1) - 6(n+1) +3) \\ 
= \frac{n}{3}(4n^2 + 6n + 2 - 6n - 6 + 3) \\ 
\Rightarrow\boxed{S_n=\frac{n}{3}\left(4n^2-1\right)}$</div>

(b) $S_n=5-\frac{5}{2}+\frac{5}{4}-\frac{5}{8}+ . . . +\frac{ {\left(-1\right) }^{n-1}5}{2^{n-1}}$
<div class = "answer"> Use the sum of a Geometric Series, with $a_1=5$ and $r=\frac{-1}{2}$: <br>
$= 5\frac{1-(\frac{-1}{2})^n}{1-(\frac{-1}{2})} \\
= 5\frac{1+\frac{\left(-1\right)^{n+1}}{2^n}}{\frac{3}{2}} \\
\Rightarrow\boxed{S_n=\frac{10}{3}\left\{1+\frac{\left(-1\right)^{n+1}}{2^n}\right\}\ }$</div>

-----------------------------------------------------------------------------------

### Problem 5.
Find the limiting values of the following:

(a) $\frac{ {3x}^2+5x-4}{ {5x}^2-x+7}\ \text{as} \ x\rightarrow{}\infty{}$
<div class = "answer">
As $x$ tends to infinity, $\frac{ {3x}^2+5x-4}{ {5x}^2-x+7}$ tends to the highest powers of $x$, which is $\frac{3x^2}{5x^2}$. Since the $x^2$ terms cancel out, $\frac{3}{5}$ is left. <br>
$\boxed{\frac{ {3x}^2+5x-4}{ {5x}^2-x+7}\rightarrow{}\frac{3}{5}, \text{ as } x\rightarrow{}\infty{}}$</div>

(b) $\frac{x^2+5x-4}{ {2x}^2-3x+1}\ \text{as}\ x\rightarrow{}\infty{}$
<div class = "answer">As $x$ tends to infinity, $\frac{x^2+5x-4}{ {2x}^2-3x+1}$ tends to the highest powers of $x$, which is $\frac{x^2}{2x^2}$. Since the $x^2$ terms cancel out, $\frac{1}{2}$ is left. <br>
$\boxed{\frac{x^2+5x-4}{ {2x}^2-3x+1}\rightarrow{}\frac{1}{2}, \text{ as } x\rightarrow{}\infty{}}$</div>

-----------------------------------------------------------------------------------

### Problem 6.

(a) Using the standard summation formulae, find an expression for $S=\sum_{r=1}^{n}\ (2-4r)^2$ in terms of $n$. Give your answer in a fully factorised form.
<div class = "answer">
$= \sum_{r=1}^{n}\ (2-4r)^2 = \sum_{r=1}^{n}\ 4 - 16\sum_{r=1}^{n}\ r + 16\sum_{r=1}^{n}\ r^2   \\
            = 4n - 8n(n+1) + \frac{8}{3}n(n+1)(2n+1) \\
            = \frac{4}{3}n(3-6(n+1)+2(n+1)(2n+1)) \\ 
            = \frac{4}{3}n(4n^2 -1) \\
            \Rightarrow \boxed{\frac{4}{3}n(2n-1)(2n+1)}$</div>

(b) Hence evaluate $S=\sum_{r=20}^{60}\ (2-4r)^2$
<div class = "answer">
$S=\sum_{r=20}^{60}\ (2-4r)^2 \\
= \frac{4}{3}(60)(119)(121) - \frac{4}{3}(19)(37)(39) \\
        \Rightarrow \boxed{1115364}$</div>

-----------------------------------------------------------------------------------

### Problem 7.

(a) Show that $S=\sum_{r=1}^{n}\ (4r-2) = 2n^2$
<div class = "answer">
$\sum_{r=1}^{n}\ (4r-2) \\ 
            = 4\sum_{r=1}^{n}\ r - 2n \\ 
            =2n(n+1)-2n \\
            \Rightarrow \boxed{2n^2}$
</div>

(b) Show that $\frac{ \sum_{r=1}^{n}\ (2r-1)}{\sum_{r=n+1}^{2n}\ (2r-1)} = k$, where $k$ is constant to be determined. 
<div class = "answer">$\frac{ \sum_{r=1}^{n}\ (2r-1)}{\sum_{r=n+1}^{2n}\ (2r-1)} \\
            = \frac{n^2}{(2n)^2 -n^2} \\
            =\frac{n^2}{3n^2}\\
            \Rightarrow \boxed{ \frac{1}{3} = k}$</div>

(c) Use standard series formulae to show that $\sum_{r=1}^{n}\ r^2(6-8r) = n(n+1)(1-2n^2)$
<div class = "answer">
$\sum_{r=1}^{n}{r^2(6-8r)}\ = 6\sum_{r=1}^{n}{r^2}\ - 8\sum_{r=1}^{n}{r^3} \\
       = \frac{6}{6} n(n+1)(2n+1) - \frac{8}{4}n^2(n+1)^2 \\
       = n(n+1)[(2n+1)-2n(n+1)]\\
       \Rightarrow \boxed{n(n+1)(1-2n^2)}$
</div>

-----------------------------------------------------------------------------------

### Problem 8.
Determine whether each of the following series converges or diverges:

(a) $\sum_{n=1}^{\infty{}}\frac{n}{n^2+1}$
<div class = "answer">$\boxed{\text{Diverges}}$ <br>
Solution: <br>
Using $n^{th}$ term test (or "Test for Divergence" as written in the notes), it is indicated that as $n$ goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Note: Here it is not possible to apply the ratio test as $\lim_{n\rightarrow\infty}{\frac{a_{n+1}}{a_n}}=1$.

$$
\lim_{n\rightarrow\infty}{\frac{(n+1)(n^2+1)}{((n+1)^2+1)(n)}}=\lim_{n\rightarrow\infty}{\frac{n^3+n^2+n+1}{n^3+2n^2+2n}}=1 
$$

Instead, we can use the "Limit Comparison Test". We choose an arbitrary $b_n$ in which for all $n=1,2,3, ...,\infty$, $b_n>0$. Then if $\lim_{n\rightarrow\infty}{\frac{a_n}{b_n}=c>0}$: 
$$ \text{either } b_n \text{ converges, so then } a_n \text{ converges} $$
$$ \text{or } b_n \text{ diverges, so then } a_n \text{ diverges} $$

Here, let $b_n=\frac{1}{n}$. Note that we can also pick other functions for $\ b_n $ but choosing $\frac{1}{n}$ or $\frac{1}{n^2}$ is a common and a safe option for this test.<br>
$$
\lim_{n\rightarrow\infty}{\frac{\frac{n}{n^2+1}}{\frac{1}{n}}}=\frac{n^2}{n^2+1}=1>0.
$$
Hence, since $\sum_{n=1}^{\infty}{b_n}$ diverges, $\sum_{n=1}^{\infty}{a_n}$ also diverges.
<br><br>
Note: if it's unclear to you why $\sum_{n=1}^{\infty}{b_n}$ is divergent this can be verified using the p-series test which says: if $a_n = n^{-p}$, and $p > 1$ then the series converges.
<br>
$b_n = \frac{1}{n} = n^{-1}$
<br>
In this case $p$ isn't greater than 1 so the series does not converge: it diverges.
</div>

(b) $\sum_{n=0}^{\infty{}}\frac{1}{\left(2n+1\right)!}$
<div class = "answer">
$\boxed{\text{Converges}}$

Solution:

Using $n^{th}$ term test (or "Test for Divergence" as written in the notes), it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

We can use the ratio test:

$$
\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}}
=\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{1}{\left(2\left(n+1\right)+1\right)!}\times{}\frac{\left(2n+1\right)!}{1}\right\vert{}=\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{\left(2n+1\right)!}{\left(2n+3\right)!}\right\vert{}=0}}
$$

$\therefore$ The series is convergent.
<br><br>
Note: when testing for convergence the ratio test is the most common test to try first after the $n^{th}$ term test (or "Test for Divergence" as written in the notes). If that test fails then try another one.</div>

(c) $\frac{x}{1\times{}2}+\frac{x^2}{2\times{}3}+\frac{x^3}{3\times{}4}+…,\ \text{for}\ -1 < x < +1$
<div class = "answer">
$\boxed{\text{Converges}}$

Solution:

The equation for sum of the series is:

$$
\sum_{n=1}^{\infty{}}\frac{x^n}{n(n+1)}
$$

Using $n^{th}$ term test (or "Test for Divergence" as written in the notes), it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Using the ratio test:

$$
\lim_{x\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}=}\lim_{x\rightarrow{}\infty{}}{\left\vert{}\frac{ {(x}^{n+1}). [ n(n+1) ] }{\left[ \left(n+1\right)(n+2) \right] .x^n}\right\vert{}}=\left\vert{}x\right\vert{}
$$

Therefore, the series converges for $\left\vert{}x\right\vert{}<1$. 
<br>
i.e. since the limit isn't equal to 1, then as long as $\left\vert{}x\right\vert{}$ is less than one the series converges.
</div>

(d) $\sum_{n=1}^{\infty{}}\frac{ {1+3n}^2}{ {1+n}^2}$
<div class = "answer">
$\boxed{\text{Diverges}}$


Solution:


Using $n^{th}$ term test (or "Test for Divergence" as written in the notes), it is indicated that as $n$  index goes to infinity, the terms go to non-zero value (i.e. the series is divergent at this stage).

We can use the ratio test to verify that it diverges as well:

$$
\lim_{n\rightarrow{}\infty{}}{\frac{1+3n^2}{1+n^2}=3}
$$
</div>


-----------------------------------------------------------------------------------

### Problem 9.
Find the range of values of $X$ for which the following series are
absolutely convergent:

(a) $\frac{X}{27}+\frac{X^2}{125}+...+\frac{X^n}{ {\left(2n+1\right)}^3}+...$

<div class = "answer">
Answer: $\boxed{\text{Convergent for } -1\leq{}X\leq{}1}$. <br><br>

Solution:

Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Using the ratio test:

$$
\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}}
$$

$$
=\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{X^{(n+1)}}{ {(2\left(n+1\right)+1)}^3}\times{}\frac{ {(2n+1)}^3}{X^n}\right\vert{}}
$$

$$
=\left\vert{}X\right\vert{}\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{ {(2n+1)}^3}{ {(2n+3)}^3}\right\vert{}=\vert{}X\vert{}}
$$

Convergent for $-1 < X < 1$.

Now check if the endpoints are converging:

$$
At\ X=1,\lim_{x\rightarrow{}1}{\sum_{n=1}^{\infty{}}\frac{X^n}{ {(2n+1)}^3}\Rightarrow{}\text{convergent}}
$$

$$
At\ X=-1,\\
\lim_{x\rightarrow{}-1}{\sum_{n=1}^{\infty{}}\frac{X^n}{ {(2n+1)}^3}\Rightarrow{}\text{convergent}}
$$

</div>

(b) $ \sum_{n=1}^{\infty{}}\frac{(n+1)}{n^3}X^n $
<div class = "answer">
Answer: $\boxed{\text{Convergent for }-1\leq{}X\leq{}1}$. <br><br>

Solution:

Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Using the ratio test:

$$
\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}}=\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{\left(n+2\right)X^{(n+1)}}{ {(n+1)}^3}\times{}\frac{n^3}{\left(n+1\right)X^n}\right\vert{}}
$$

$$
=\left\vert{}X\right\vert{}\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{n^4+2n^3}{n^4+{4n}^3+{6n}^2+4n+1}\right\vert{}=\vert{}X\vert{}}
$$

Convergent for $-1< X < 1$.

Now check if the endpoints are converging:

$$
At\ X=1,\\
\lim_{x\rightarrow{}1}{\sum_{n=1}^{\infty{}}\frac{\left(n+1\right)*X^n}{n^3}}
\Rightarrow{}\text{convergent}
$$

$$
At\ X=-1,\\
\lim_{x\rightarrow{}-1}{\sum_{n=1}^{\infty{}}\frac{\left(n+1\right)*X^n}{n^3}}
\Rightarrow{} \text{convergent}
$$

</div>

(c) $ \sum_{n=1}^{\infty{}}(\ln{n)}X^n $

<div class = "answer">
Answer: $\boxed{\text{Convergent for } \left\vert{}X\right\vert{} < 1 }$. <br><br>


Solution:


Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Using the ratio test:

$$
\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}=}\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{ {\ln{\left(n+1\right)}.X}^{n+1}}{\ln{\left(n\right)}{.X}^n}\right\vert{}}=\left\vert{}X\right\vert{}
$$

Therefore, converges for $\left\vert{}X\right\vert{}<1$.

Now check if the endpoints are converging:

$$
At\ X=1,\\
\lim_{x\rightarrow{}1}{\sum_{n=1}^{\infty{}}\ln{\left(n\right)}}\Rightarrow{} \text{divergent}
$$

$$
At\ X=-1,\\
\lim_{x\rightarrow{}-1}{\sum_{n=1}^{\infty{}}}
{(-1)}^n\ln{\left(n\right)}\Rightarrow{} \text{divergent}
$$

Note: The $n^{th}$ term test showed that 
$\lim_{n\to\infty}$ of $a_n$ goes to zero only for $-1 < X <1$. However, the test only shows whether the function diverges and does not test the convergency. Hence, the ratio test must be conducted.  
</div>

(d) $ \sum_{n=0}^{\infty{}}\frac{3^nX^n}{n!} $

<div class = "answer">
Answer: $\boxed{\text{Convergent for all values of } X}$. <br><br>

Solution:

Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Using the ratio test:

$$ \lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}=}\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{3^{n+1}X^{n+1}}{\left(n+1\right)!}\times{}\frac{n!}{3^nX^n}\right\vert{}}=
\frac{3\left\vert{}X\right\vert{}}{n+1}=0 $$

The function will always converge no matter what the value of $X$ is.
</div>

-----------------------------------------------------------------------------------

## Exam Style Questions
### Problem 10.
An investment fund offers three  investment strategy packages to its clients if they invest exactly £500,000. The first option is an annual return of 16%, but this is not compounded each year (i.e. the profit from each year is not reinvested). The second option offers a compounded daily return of 0.03%. The third option simply pays you an increasing dividend of £1 on the first day, followed by £2 on the second, £3 on the third and so on.

(a) Calculate the profit after 4 years for each of the three options.
<div class = "answer">

 <b> Option 1: </b> <br>

The annual return will be: $ \frac{16}{100} \times  £500,000 = £80,000 $

So the profit after four years will be: $ 4 \times £80,000 \Rightarrow \boxed{£320,000} $ <br>

 <b> Option 2: </b> <br>

To calculate compound interest we use: $P[(1+i)^{n} - 1] \\
P = \text{initial balance, } i = \text{interest rate, and } n = \text{number of compounding periods.}
\\ £500,000 \times (1.0003^{4 \times 365} − 1) \Rightarrow \boxed{£274,751.56}
\\$ 

 <b> Option 3: </b> <br>

Method 1: We can calculate the total profit by creating a formula for the sum of the profit each day for 4 years.

$\sum_{n=0}^{4 \times 365}{n} \Rightarrow \boxed{£1,066,530} \\$
<br>

Method 2: We can calculate the sum of the profit using the formula for the sum of an arithmetic series.
$\text{The sum of this series is: } \quad S_n = \frac{n}{2}(2a + (n - 1)d) = \frac{n(n+1)}{2}
\\ \therefore (4 \times 365)\frac{(4 \times 365 + 1)}{2} \Rightarrow \boxed{£1,066,530}$</div>

(b) Which option offers the best return after 40 years?
<div class = "answer">
We use the same method as in part (a) but replacing the year 4 with 40.
<br>

 <b> Option 1:  </b> <br>

The return will be: $ £3,200,000 $

 <b> Option 2: </b> <br>

The return will be: $ £39,392,804 $

 <b> Option 3: </b> <br>

The return will be: $ £106,587,300 $

So the option with the best return is $\Rightarrow \boxed{\text{Option 3}}$
</div>

(c) Draw a graph showing the profit vs. time for the three options over 40
years.
<div class = "answer">
Insert graph.</div>

(d) Write down an expression for the difference between the profits of the
second and third options as a function of the number of days since
investing, 𝑁.
<div class = "answer">
$\frac{N(N+1)}{2} = 1.0003^N - 1
\\ \Rightarrow \boxed{f(N) = 1.0003^N - 1 - \frac{N(N+1)}{2}}$
</div>

(e) Give an interpretation of the roots of this function.
<div class = "answer">
$\Rightarrow$ The days of investment after which it would be more profitable to have adopted the other strategy.
$\\$
</div>

-----------------------------------------------------------------------------------

## Challenging Questions
### Problem 11.

Let $ \ S_n \ $ be a sequence given by $ \ S_n = \frac{1}{n+1} +  \frac{1}{n+2} + ... + \frac{1}{2n}$.$\ \$ Show that the sequence is increasing. 

<div class = "answer">
For a sequence to be increasing: $ S_{n+1} - S_n > 0
\\ S_{n+1} - S_n = (\frac{1}{n+2} +  \frac{1}{n+3} + ... +  \frac{1}{2n} +  \frac{1}{2n + 1} +  \frac{1}{2n + 2}) - (\frac{1}{n+1} + \frac{1}{n+2} +  \frac{1}{n+3} + ... +  \frac{1}{2n})
\\ \qquad \quad \quad \ = \frac{1}{2n + 1} +  \frac{1}{2n + 2} - \frac{1}{n+1}
\\ \qquad \quad \quad \ = \frac{4n+3}{(2n + 1)(2n+2)} - \frac{2}{2n+2}
\\ \qquad \quad \quad \ = \frac{(4n+3) - 2(2n+1)}{(2n + 1)(2n+2)}
\\ \qquad \quad \quad \ = \frac{1}{(2n + 1)(2n+2)} > 0 \Rightarrow \text{The sequence is increasing}$

</div>

### Problem 12.

Fid the missing number in the following sequence: 
$\ \ 61, \ 52, \ 63, \ 94, \ ?, \ 18,... $ 

<div class = "answer">
This is a bit of a trick question: you should read the numbers backwards!
<br>
i.e. read the number from right to left. The sequence then becomes:
<br>
$16, \ 25, \ 36, \ 49, \ ?, \ 81,... $ 
<br>
Now you just have a sequence of the squared numbers starting at 4:
<br>
$4^2, \ 5^2, \ 6^2, \ 7^2, \ ?, \ 9^2,... $
<br>
so the missing number will be $8^2 = 64$ and if we reverse the digits we have our final answer
$\Rightarrow\boxed{46}$

</div>
<br><br>

## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>

<br><br>

# Next week, Taylor Series and Complex Numbers!
