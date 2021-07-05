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
Suggest a formula for the $n$th term of the following sequences.

(a) $3, -5, 7, -9, 11,...$
<div class = "answer"> $\Rightarrow\boxed{a_n=(-1)^{n+1}.(2n+1)}$ </div>

(b) $2,\frac{3}{2},\frac{4}{3},\frac{5}{4},\frac{6}{5},...$
<div class = "answer"> $\Rightarrow\boxed{a_n=\frac{n+1}{n}}$ </div>

(c) $\frac{2}{3},\frac{3}{2\times{}4},\frac{4}{3\times{}5},\frac{5}{4\times{}6},\frac{6}{5\times{}7},...$
<div class = "answer">$\Rightarrow\boxed{a_n=\frac{n+1}{n(n+2)}}$</div>

(d) $1, 0,-e^2,0,e^4,...$
<div class = "answer">$\Rightarrow\boxed{a_n=e^{n-1}\sin\left(\frac{n\pi}{2}\right)}$</div>

(e) Find the third, sixth and ninth term of the sequence given by the formula. 

$$ \left\{ \frac{n^2-n-6}{n+2} \right\}_{n=1}^\infty $$

<div class = "answer">$\Rightarrow \boxed{a_3 = \frac{3^2-3-6}{3+2} = 0 ,\ \ a_6=\frac{6^2-6-6}{6+2}= \frac{24}{8}=3,\ \ \ a_9=\frac{9^2-9-6}{9+2}=\frac{66}{11}=6}$</div>

(f) Find the third, sixth and ninth term of the sequence given by the formula: 

$$\left\{\binom{n}{2}-\binom{n}{3}\right\}_{n=3}^\infty$$  

using the binomial coefficient  $\binom{n}{k}=\frac{n!}{k!(n-k)!}$
<div class = "answer">
In this series, the first term is at $n=3$, so the third term is at $n=5$, the sixth at $n=8$ and the ninth at $n=11$.
$a_3=\frac{5!}{2!(5-2)!} - \frac{5!}{3!(5-3)!}=\frac{120}{2\cdot 6} - \frac{120}{3! \cdot 2!}=10-10=\boxed{0} 
\\ \\ a_6=\frac{8!}{2!(8-2)!} - \frac{8!}{3!(8-3)!}=\frac{40320}{2\cdot 720} - \frac{40320}{6 \cdot 120}=28-56=\boxed{-28,}\ 
\\ \\ a_9=\frac{11!}{2!(11-2)!}-\frac{11!}{3!(11-3)!}= 55-165=\boxed{-110}$</div>

(g) Find the third, sixth and ninth term of the sequence given by the formula: 

$$\left\{\sin⁡[ \left(n+1\right)\frac{\pi{}}{3}] \right\}_{n=1}^\infty$$

<div class = "answer">$\boxed{a_3=\sin(3+1)\frac{\pi{}}{3}=\sin(\frac{4\pi{}}{3})=-\frac{\sqrt{3}}{2},
\\ \\ a_6=\sin(6+1)\frac{\pi{}}{3}=\sin(\frac{7\pi{}}{3})=\frac{\sqrt{3}}{2},
\\ \\ a_9=\sin(9+1)\frac{\pi{}}{3}=\sin(\frac{10\pi{}}{3})=-\frac{\sqrt{3}}{2}}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 2.
Evaluate the following.

(a) $\sum_{n=1}^{20}\left(0.2n+5\right)$
<div class = "answer">$\Rightarrow{}\quad$
The Sum of an Arithmetic Sequence: <br>
$S_n= \frac{n}{2}(2a + d(n - 1))=\frac{20}{2}(2(0.2+5) + (0.2)(20 - 1)) = (10)(14.2)= \boxed{142}$</div>

(b) $\sum_{n=1}^8n\left(3+2n+n^2\right)$
<div class = "answer">Break down into smaller sequences <br> 
$\Rightarrow 3\sum_{n=1}^8n \ + \ 2\sum_{n=1}^8n^2 \ +\ \sum_{n=1}^8n^3\ 
\\ = 3(\frac{8(8+1)}{2}) + 2(\frac{8(8+1)(16+1)}{6}) + \frac{64(8+1)^2}{4} 
\\ = 108 + 408 + 1296 \\= \boxed{1812}$</div>

(c) $\sum_{r=1}^nr\left(r+3\right)$
<div class = "answer">Break down into smaller sequences
$\Rightarrow \sum_{r=1}^nr^2 \ + 3\sum_{r=1}^nr \\ \\ 
= \frac{n(n+1)(2n+1)}{6} + 3(\frac{n(n+1)}{2}) \\ \\
= \frac{n}{6}((n+1)(2n+1) +9(n+1)) \\ \\
= \frac{n}{6}(2n^2+12n+10) \\ \\
= \frac{n}{3}(n^2+6n+5) \\ \\
=\boxed{\frac{n}{3}\left(n+1\right)\left(n+5\right)}$</div>

(d) $\sum_{r=1}^n{\left(r+1\right)}^3$
<div class = "answer">Break down into smaller sequences
$\Rightarrow \sum_{r=1}^nr^3 \ + 3\sum_{r=1}^nr^2 \ +3\sum_{r=1}^nr \ +\sum_{r=1}^n1 \\ \\
= \frac{n^2(n+1)^2}{4} + \frac{n(n+1)(2n+1)}{2} + 3(\frac{n(n+1)}{2}) + n \\ \\
= \frac{n}{4}(n(n+1)^2 + 2(n+1)(2n+1) + 6(n+1) + 4) \\ \\
= \frac{n}{4}(n^3 + 2n^2 + n + 4n^2 + 6n + 2 + 6n + 6 + 4) \\ \\
= \boxed{\frac{n}{4}(n^3 + 6n^2 + 13n + 12)}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 3.
Find the sum of $n$ terms of the following.

(a) $S_n=1^2+3^2+5^2+ . . . +{\left(2n-1\right)}^2$
<div class = "answer">Use the sum of polynomial series identities
$\Rightarrow 4\sum_{n=1}^nn^2 \ -4\sum_{n=1}^nn \ + \sum_{n=1}^n1 \\ 
= 2(\frac{n(n+1)(2n+1)}{3}) - 4(\frac{2n(n+1)}{2}) + n \\ 
= \frac{n}{3}(2(n+1)(2n+1) - 6(n+1) +3) \\ 
= \frac{n}{3}(4n^2 + 6n + 2 - 6n - 6 + 3) \\ 
\Rightarrow\boxed{S_n=\frac{n}{3}\left(4n^2-1\right)}$</div>

(b) $S_n=5-\frac{5}{2}+\frac{5}{4}-\frac{5}{8}+ . . . +\frac{ {\left(-1\right) }^{n-1}5}{2^{n-1}}$
<div class = "answer">$\Rightarrow\boxed{S_n=\frac{10}{3}\left\{1+\frac{ {\left(-1\right)}^{n+1}}{2^n}\right\}\ }$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 4.
Find the limiting values of the following:

(a) $\frac{ {3x}^2+5x-4}{ {5x}^2-x+7}\ as\ x\rightarrow{}\infty{}$
<div class = "answer">
As $x$ tends to infinity, $\frac{ {3x}^2+5x-4}{ {5x}^2-x+7}$ tends to the highest powers of $x$, which is $\frac{3x^2}{5x^2}$ Since the $x^2$ terms cancel out, $\frac{3}{5}$ is left. <br>
$\boxed{\frac{ {3x}^2+5x-4}{ {5x}^2-x+7}\rightarrow{}\frac{3}{5}, \text{ as } x\rightarrow{}\infty{}}$</div>

(b) $\frac{x^2+5x-4}{ {2x}^2-3x+1}\ as\ x\rightarrow{}\infty{}$
<div class = "answer">As $x$ tends to infinity, $\frac{x^2+5x-4}{ {2x}^2-3x+1}$ tends to the highest powers of $x$, which is $\frac{x^2}{2x^2}$ Since the $x^2$ terms cancel out, $\frac{1}{2}$ is left. <br>
$\boxed{\frac{x^2+5x-4}{ {2x}^2-3x+1}\rightarrow{}\frac{1}{2}, \text{ as } x\rightarrow{}\infty{}}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 5.
Determine whether each of the following series converges or diverges.

(a) $\sum_{n=1}^{\infty{}}\frac{n}{n^2+1}$
<div class = "answer">$\boxed{\text{Diverges}}$ <br>
Solution: <br>
Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Note: Here it is not possible to apply the ratio test as $\lim_{n\rightarrow\infty}{\frac{a_{n+1}}{a_n}}=1$.

$$
\lim_{n\rightarrow\infty}{\frac{(n+1)(n^2+1)}{((n+1)^2+1)(n)}}=\lim_{n\rightarrow\infty}{\frac{n^3+n^2+n+1}{n^3+2n^2+2n}}=1 
$$

Instead, we use the 'Limit Comparison Test'. We choose an arbitrary $b_n$ in which for all $n=1,2,3, ...,\infty$, $b_n>0$. Then if $\lim_{n\rightarrow\infty}{\frac{a_n}{b_n}=c>0}$: 
$$ \text{Either } b_n \text{ converges, so then } a_n \text{ converges} $$
$$ \text{or } b_n \text{ diverges, so then } a_n \text{ diverges} $$

Here, let $b_n=1/n$. <br>
$$
\lim_{n\rightarrow\infty}{\frac{\frac{n}{n^2+1}}{\frac{1}{n}}}=1>0.
$$
Hence, the $\sum_{n=1}^{\infty}{b_n}$ is divergent, the
$\sum_{n=1}^{\infty}{a_n}$ also diverges.
</div>

(b) $\sum_{n=0}^{\infty{}}\frac{1}{\left(2n+1\right)!}$
<div class = "answer">
$\boxed{\text{Converges}}$

Solution:

Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Using the ratio test:

$$
\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}}=\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{1}{\left(2\left(n+1\right)+1\right)!}\times{}\frac{\left(2n+1\right)!}{1}\right\vert{}=\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{\left(2n+1\right)!}{\left(2n+3\right)!}\right\vert{}=0}}\
\rightarrow{}\text{converges}
$$</div>

(c) $\frac{x}{1\times{}2}+\frac{x^2}{2\times{}3}+\frac{x^3}{3\times{}4}+…,\ for-1 < x < +1$
<div class = "answer">
$\boxed{\text{Converges}}$

Solution:

Equation for sum of the series is:

$$
\sum_{n=1}^{\infty{}}\frac{x^n}{n(n+1)}
$$

Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

{Using the ratio test:}

$$
\lim_{x\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}=}\lim_{x\rightarrow{}\infty{}}{\left\vert{}\frac{ {(x}^{n+1}). [ n(n+1) ] }{\left[ \left(n+1\right)(n+2) \right] .x^n}\right\vert{}}=\left\vert{}x\right\vert{}
$$

Therefore, converge for $\left\vert{}x\right\vert{}<1$.</div>

(d) $\sum_{n=1}^{\infty{}}\frac{ {1+3n}^2}{ {1+n}^2}$
<div class = "answer">
$\boxed{\text{Diverges}}$


Solution:


Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to non-zero value (i.e. the series is divergent at this stage).

Using the ratio test:

$$
\lim_{n\rightarrow{}\infty{}}{\frac{1+3n^2}{1+n^2}=3}
$$
</div>


(e) Find the range of values of $X$ for which the following series is
absolutely convergent. 
$$
\frac{X}{27}+\frac{X^2}{125}+...+\frac{X^n}{ {\left(2n+1\right)}^3}+...
$$

-----------------------------------------------------------------------------------
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

### Problem 6.
(a) Find the range of values of $X$ for which the following series is
absolutely convergent. 

$$
\frac{X}{27}+\frac{X^2}{125}+...+\frac{X^n}{ {\left(2n+1\right)}^3}+...
$$

<div class = "answer">
Answer: $\boxed{\text{Convergent for } -1\leq{}X\leq{}1.}$ <br><br>

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
\rightarrow{}At\
X=1,\lim_{n\rightarrow{}1}{\sum_{x=1}^{\infty{}}\frac{X^n}{ {(2n+1)}^3}\Rightarrow{}\text{convergent}}\
$$

$$
At\ X=-1,\ \
\lim_{n\rightarrow{}-1}{\sum_{x=1}^{\infty{}}\frac{X^n}{ {(2n+1)}^3}\Rightarrow{}\text{convergent}}\
$$</div>

(b) Find the range of values of $x$ for which the following series is
absolutely convergent. 
$$ \sum_{n=1}^{\infty{}}\frac{(n+1)}{n^3}X^n $$
<div class = "answer">
Answer: $\boxed{\text{Convergent for }-1\leq{}x\leq{}1}$. <br><br>

Solution:

Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Using the ratio test:

$$
\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}}=\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{\left(n+2\right).X^{(n+1)}}{ {(n+1)}^3}\times{}\frac{n^3}{\left(n+1\right).X^n}\right\vert{}}
$$

$$
=\left\vert{}x\right\vert{}\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{n^4+2n^3}{n^4+{4n}^3+{6n}^2+4n+1}\right\vert{}=\vert{}x\vert{}}
$$

Convergent for $-1< x < 1$.

Now check if the endpoints are converging:

$$
\rightarrow{}At\ x=1,\
\lim_{x\rightarrow{}1}{\sum_{n=1}^{\infty{}}\frac{\left(n+1\right).X^n}{n^3}}\
\Rightarrow{}\text{convergent}
$$

$$
At\ x=-1,\
\lim_{x\rightarrow{}-1}{\sum_{n=1}^{\infty{}}\frac{\left(n+1\right).X^n}{n^3}}\
\Rightarrow{} \text{convergent, therefore, Convergent for} -1\leq{}x\leq{}1.
$$</div>

(c) Find the range of values of $x$ for which the following series is
absolutely convergent. 
$$ \sum_{n=1}^{\infty{}}(\ln{n)}X^n $$
<div class = "answer">
Answer: $\boxed{\text{Convergent for } \left\vert{}x\right\vert{} < 1 }$. <br><br>


Solution:


Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Using the ratio test:

$$
\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}=}\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{ {\ln{\left(n+1\right)}.x}^{n+1}}{\ln{\left(n\right)}{.x}^n}\right\vert{}}=\left\vert{}x\right\vert{}
$$

Therefore, converge for $\left\vert{}x\right\vert{}<1$.

Now check if the endpoints are converging:

$$
\rightarrow{}At\ x=1,\ \
\lim_{x\rightarrow{}1}{\sum_{n=1}^{\infty{}}\ln{\left(n\right)}}\Rightarrow{}diverges
$$


$$\rightarrow{}At x=-1,\ \ \lim_{x\rightarrow{}-1}{\sum_{n=1}^{\infty{}}}
{(-1)}^n\ln{\left(n\right)}\Rightarrow{}diverges$$

Note: The $n^{th}$ term test showed that 
$\lim_{n\to\infty}$ of $a_n$ goes to zero only for $-1 < X <1$. However, the test only shows whether the function diverges and does not test the convergency. Hence, the ratio test must be conducted.  
</div>

(d) Find the range of values of $x$ for which the following series is absolutely convergent.
$$ \sum_{n=0}^{\infty{}}\frac{3^nX^n}{n!} $$
<div class = "answer">
Answer: $\boxed{\text{Convergent for all values of } x}$. <br><br>

Solution:

Using $n^{th}$ term test, it is indicated that as $n$  index goes to infinity, the terms go to zero (i.e. the series is not divergent at this stage).

Using the ratio test:

$$ \lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{a_{n+1}}{a_n}\right\vert{}=}\lim_{n\rightarrow{}\infty{}}{\left\vert{}\frac{3^{n+1}X^{n+1}}{\left(n+1\right)!}\times{}\frac{n!}{3^nX^n}\right\vert{}}=\
\frac{3\left\vert{}x\right\vert{}}{n+1}=0 $$

Converges for all values of $x$.
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><P style="page-break-before: always"></div>

-----------------------------------------------------------------------------------

## Exam Style Questions
### Problem 7.

(a) Using the standard summation formulae, find an expression for $S=\sum_{r=1}^{n}\ (2-4r)^2$ in terms of $n$. Give your answer in a fully factorised form.
<div class = "answer">
$\Rightarrow \sum_{r=1}^{n}\ (2-4r)^2 = \sum_{r=1}^{n}\ 4 - 16\sum_{r=1}^{n}\ r + 16\sum_{r=1}^{n}\ r^2   \\
            = 4n - 8n(n+1) + \frac{8}{3}n(n+1)(2n+1) \\
            = \frac{4}{3}n(3-6(n+1)+2(n+1)(2n+1)) \\ 
            = \frac{4}{3}n(4n^2 -1) \\
            = \boxed{\frac{4}{3}n(2n-1)(2n+1)}$</div>

(b) Hence evaluate $S=\sum_{r=20}^{60}\ (2-4r)^2$
<div class = "answer">
$S=\sum_{r=20}^{60}\ (2-4r)^2 = \frac{4}{3}(60)(119)(121) - \frac{4}{3}(19)(37)(39) \\
        = \boxed{1115364}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><P style="page-break-before: always"></div>

-----------------------------------------------------------------------------------

### Problem 8.

(a) Show that $S=\sum_{r=1}^{n}\ (4r-2) = 2n^2$
<div class = "answer">
$\boxed{\sum_{r=1}^{n}\ (4r-2) \\ 
            = 4\sum_{r=1}^{n}\ r - 2n \\ 
            =2n(n+1)-2n \\
            = 2n^2}$
</div>

(b) Show that $\frac{ \sum_{r=1}^{n}\ (2r-1)}{\sum_{r=n+1}^{2n}\ (2r-1)} = k$, where $k$ is constant to be determined. 
<div class = "answer">$\frac{ \sum_{r=1}^{n}\ (2r-1)}{\sum_{r=n+1}^{2n}\ (2r-1)} \\
            = \frac{n^2}{(2n)^2 -n^2} \\
            =\frac{n^2}{3n^2}\\
            = \boxed{\frac{1}{3} = k}$</div>

(c) Use standard series formulae to show that $\sum_{r=1}^{n}\ r^2(6-8r) = n(n+1)(1-2n^2)$
<div class = "answer">
$\sum_{r=1}^{n}{r^2(6-8r)}\ = 6\sum_{r=1}^{n}{r^2}\ - 8\sum_{r=1}^{n}{r^3} \\
       = \frac{6}{6} n(n+1)(2n+1) - \frac{8}{4}n^2(n+1)^2 \\
       = n(n+1)[(2n+1)-2n(n+1)]\\
       = \boxed{n(n+1)(1-2n^2)}$
</div>

-----------------------------------------------------------------------------------
<br><br>

## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>
<br><br>
### For Printing
<button type="button" onclick="prepareForPrint('block')">Add whitespace</button>
<button type="button" onclick="prepareForPrint('none')">Remove whitespace</button>

<br><br>

# Next week, Taylor Series and Complex Numbers!