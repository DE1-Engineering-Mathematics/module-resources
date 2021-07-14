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

# Power Series Tutorial Sheet, Sheet #5A

### Learning targets
* Find the coefficients for a given power series
* Find both the Maclaurin and Taylor series expansion for the given function
* Sketch truncated Taylor polynomial of a Taylor series expansion
* Work with limits when evaluating a given series

### Additional Resources
* [SJC - Sequence, Series](https://youtu.be/kUbzTJ1UDy4)
* [SJC - Power Series](https://youtu.be/Y2Yfq-IR9iQ)

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Compute the coefficients of the following power series:

(a) $f(x)=\sin{x}\quad\quad\quad(x=0,n=6)$
<div class = "answer"> 
Maclaurin series (x=0) in the form:
$$\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n$$
Table of $f^{(n)}(0)$ coefficients for this series:
$$\begin{align*}
        & n&    f&^{(n)}(x)&       f&^{(n)}(0)&  \\
        \hline
        & 0&     &\sin{x}&       &0&             \\
        & 1&    & \cos{x}&   &1&\\
        & 2&   -&\sin{x}&  &0&   \\
        & 3&   -&\cos{x}&  -&1&    \\
        & 4&   &\sin{x}&  &0&    \\
        & 5&   &\cos{x}&  &1&    \\
        & 6&   -&\sin{x}&  &0&    \\
        \hline
        \end{align*}$$
Coefficients only exist for odd values of n. In addition, the sign of the coefficients will alternate. Thus, the resulting power series is:
$$f(x)=f(0)+f^{'}(0)x+f^{''}(0)\frac{x^2}{2!}+f^{'''}(0)\frac{x^3}{3!}+f^{''''}(0)\frac{x^4}{4!}+...$$
$$\boxed{f(x)=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+...}$$
</div>

(b) $f(x)=e^{-x^2}\quad\quad\quad(x=0,n=3)$
<div class = "answer">
Table of $f^{(n)}(0)$ coefficients for this series (Maclaurin, x=0):
$$\begin{align*}
        & n&    f&^{(n)}(x)&       f&^{(n)}(0)&  \\
        \hline
        & 0&     e&^{-x^2}&       &1&             \\
        & 1&    -&2xe^{-x^2}&     &0& \\
        & 2&   (4&x^2-2)e^{-x^2}&   -&2&   \\
        & 3&   -&4(2x^3-3x)e^{-x^2}&  &0&    \\
        \hline
        \end{align*}$$
Thus, the resulting power series is:
$$\boxed{f(x)=1-x^2+...}$$
</div>

(c) $f(x)=\frac{1}{2+x}\quad\quad\quad (x=0,n=3)$
<div class = "answer">
Table of $f^{(n)}(0)$ coefficients for this series (Maclaurin, x=0):
$$\begin{align*}
        & n&    f&^{(n)}(x)&       f&^{(n)}(0)&  \\
        \hline
        & 0&     &\frac{1}{x+2}&       &\frac{1}{2}&             \\
        & 1&    -&\frac{1}{(x+2)^2}&     -&\frac{1}{4}& \\
        & 2&   &\frac{2}{(x+2)^3}&   &\frac{1}{4}&   \\
        & 3&   -&\frac{6}{(x+2)^4}&  -&\frac{3}{8}&    \\
        \hline
        \end{align*}$$
Thus, the resulting power series is:
$$\boxed{f(x)=\frac{1}{2}-\frac{x}{4}+\frac{x^2}{8}-\frac{x^3}{16}+...}$$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 2.
Write the general equation of the $n^{th}$ order term for function $f(x)$ from $n=0$ to infinity:

(a) $f(x)=e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+...$
<div class = "answer">
Determine the $n^{th}$ term of the sequence
$$n^{th} =1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+...+\frac{x^{n}}{n!}$$
Re-express function f(x) in power series form:
$$f(x)=e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+...+\frac{x^{n}}{n!}=\boxed{\sum_{n=0}^{\infty}\frac{x^n}{n!}}$$
</div>

(b) $f(x) =e^x= e+e(x-1)+\frac{e}{2}(x-1)^2+\frac{e}{3!}(x-1)^3+\frac{e}{4!}(x-1)^4+...$
<div class = "answer">
Determine the $n^{th}$ term of the sequence 
$$n^{th}=e+e(x-1)+\frac{e}{2}(x-1)^2+\frac{e}{3!}(x-1)^3+\frac{e}{4!}(x-1)^4+...+\frac{e(x-1)^n}{n!}$$
Re-express function f(x) in power series form:
$$f(x)=e+e(x-1)+\frac{e}{2}(x-1)^2+\frac{e}{3!}(x-1)^3+\frac{e}{4!}(x-1)^4+...+\frac{e(x-1)^n}{n!}=\boxed{\sum_{n=0}^{\infty}\frac{e(x-1)^n}{n!}}$$
</div>

(c) $f(x)=\frac{1}{1+x}=1-x+x^2-x^3+x^4+...$
<div class = "answer">
Determine the $n^{th}$ term of the sequence
$$n^{th}=\frac{1}{1+x}=1-x+x^2-x^3+x^4+...+(-1)^nx^n$$
Re-express function f(x) in the form of power series:
$$f(x)=\frac{1}{1+x}=1+(-x)+x^2-x^3+x^4+...+(-1)^nx^n= \boxed{\sum_{n=0}^{\infty}(-1)^nx^n}$$
</div>

(d) $f(x) =\frac{1}{(1-x)^2}=1+2x+3x^2+4x^3+...$
<div class = "answer">
Determine the $n^{th}$ term of the sequence
$$n^{th}=\frac{1}{(1-x)^2}=1+2x+3x^2+4x^3+...+nx^{n-1}$$
Re-express function f(x) in the form of power series:
$$f(x)=\frac{1}{(1-x)^2}=1+2x+3x^2+4x^3+...+nx^{n-1}=\boxed{\sum_{n=0}^{\infty}nx^{n-1}}$$</div>

(e) $f(x)=\cos{x}=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+...$
<div class = "answer">
Determine $n^{th}$ term of the sequence	
$$n^{th}=\cos{x}=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+...+(-1)^n\frac{x^{2n}}{(2n)!}$$
Re-express function f(x) in the form of power series:
$$f(x)=\cos{x}=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+...+(-1)^n\frac{x^{2n}}{(2n)!}=\boxed{\sum_{n=0}^{\infty}(-1)^n\frac{x^{2n}}{(2n!)}}$$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 3.

(a) Find the Maclaurin series for : $$\int_0^x\cos(t^3)dt$$
<div class = "answer">
Consider the Maclaurin series for $\mathrm{\cos}(x)$ is
$$1-\frac{x^2}{2!}+\frac{x^4}{4!}-...=\sum^{\infty}_{n=0}(-1)^n\frac{x^{2n}}{(2n)!},$$
But for $t^3$: $x$ can be replaced with $t^3$ to get the Maclaurin series for $\mathrm{cos}(t^3)$:
$$1-\frac{t^6}{2!}+\frac{t^{12}}{4!}-...=\sum^{\infty}_{n=0}(-1)^n\frac{t^{6n}}{(2n)!},$$
Therefore, by integrating the sum:
$$\int^{x}_{0}\cos(t^3)dt=\int_{0}^{x}\sum^{\infty}_{n=0}(-1)^n\frac{t^{6n}}{(2n)!}dt=\Bigg[\sum^{\infty}_{n=0}(-1)^n\frac{t^{6n+1}}{(6n+1)(2n)!}\Bigg]^{x}_{0}=$$
$$=\sum^{\infty}_{n=0}(-1)^n\frac{x^{6n+1}}{(6n+1)(2n)!}$$
Where the integral can be evalutated term-by-term. The first four terms of this series are:
$$\boxed{x-\frac{x^{7}}{14}+\frac{x^{13}}{312}-\frac{x^{19}}{13680}+...}$$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 4.
Find the Maclaurin Series expansion (up to and including the 4th term) near some value $x=a$  for:

(a) $f(x)=\mathrm{sin}(x)\quad\quad\quad\quad{}x=0$
<div class = "answer">
Find the Maclaurin Series expansion near $x =0$ for $\displaystyle f(x)=\mathrm{sin}x$, by finding the first, second, third, etc derivatives and evaluating them at $x = 0$. 
Table of $f^{(n)}(0)$ coefficients for this series (Maclaurin, x=0):
        \begin{align*}
        & n&    f&^{(n)}(x)&       f&^{(n)}(0)&  \\
        \hline
        & 0&    &\mathrm{sin}x&     &0&\\
        & 1&    &\mathrm{cos}x&     &1&\\
        & 2&    -&\mathrm{sin}x&    &0& \\
        & 3&    -&\mathrm{cos}x&    -&1&    \\
        & 4&    &\mathrm{sin}x&     &0&    \\
        \hline
        \end{align*}
As this function can be differentiated infinitely, $n$ will continue forever. <br>
Substituting the values of the derivatives into the Maclaurin series:
$$f(x)\approx{f(0)+f{'}(0)x+\frac{f{''}(0)}{2!}x^2+\frac{f{'''}(0)}{3!}x^3+\frac{f{''''}(0)}{4!}x^4+...}$$
Resulting in:
$$\mathrm{sin}x=0+(1)(x)+0+\frac{-1}{3!}x^3+0+\frac{1}{5!}x^5+0+\frac{-1}{7!}x^7+...$$
Giving:
$$\boxed{\mathrm{sin}x=x-\frac{1}{6}x^3+\frac{1}{120}x^5-\frac{1}{5040}x^7+...}$$

Plotting the polynomial to check if it is a good approximation to $f(x)=\mathrm{sin}x$:

<iframe src="https://www.desmos.com/calculator/0755usqlzv" width="100%" height="400px"></iframe>

Once again, it can be observed that our polynomial (in blue) is a good approximation to $\displaystyle f(x)=\mathrm{sin}x$ (in red) between $[-\pi,+\pi]$.
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 5.
Compute the following limits using Taylor and Maclaurin expansions:

(a) $\lim\limits_{x\rightarrow0}\big(\frac{e^x -\mathrm{sin}x-\mathrm{cos}x}{e^{x^2}-e^{x^3}}\big)$
<div class = "answer">
Note: $O(x^n)$ denotes all terms with powers greater or equal to $n$, which can be considered negligible):
$$e^x-\mathrm{sin}x-\mathrm{cos}x=	$$
$$=\Big(1+x+\frac{1}{2}x^2+O(x^3)\Big)-\Big(x+O(x^3)\Big)-\Big(1-\frac{1}{2}x^2+O(x^3)\Big)=x^2+O(x^3),$$

Similarly, the function in the denominator can be written as:
$$e^{x^{2}}-e^{x^{3}}=\Big(1+x^2+O(x^3)\Big)-\Big(1+x^3+O(x^4)\Big)=x^2+O(x^3)$$
Note: Given $e^x \approx{} (1+x+\frac{1}{2}x^2+O(x^3))$

Replace $x$ with $x^n$ in the Maclaurin series above to get:
$$e^{x^n} \approx{} (1+x^{n}+\frac{1}{2}(x^n)^2+O((x^n)^3))$$

Hence:
$$\lim\limits_{x\rightarrow0}\frac{e^x-\mathrm{sin}x-\mathrm{cos}x}{e^{x^{2}}-e^{x^{3}}}=\lim\limits_{x\rightarrow0}\frac{x^2+O(x^3)}{x^2+O(x^3)}=$$

Ignoring all negligible summands:
$$\boxed{\lim\limits_{x\rightarrow0}\frac{x^2}{x^2}=1.}$$
</div>

(b) $\lim\limits_{x\rightarrow0}\big(\frac{(\sqrt[5]{1-5x^2+x^4}-1+x^2)}{x^4}\big)$
<div class = "answer">
Find the Maclaurin series for $\sqrt[5]{1+x}$, $x$ will be substituted for $(-5x^2+x^4)$ later:
        
\begin{align*}
& n&    f&^{(n)}(x)&       f&^{(n)}(0)&  \newline
\hline
& 0&    &(1+x)^\frac{1}{5}&     &1&    \\\ 
& 1&    \frac{1}{5}&(1+x)^{-\frac{4}{5}}&     &\frac{1}{5}&    \\\ 
& 2&    -\frac{4}{25}&(1+x)^{-\frac{9}{5}}&     -&\frac{4}{25}& \newline
\hline
\end{align*}

As a result:
$$\sqrt[5]{1+x}\approx1+\frac{1}{5}x-\frac{2}{25}x^2$$
Therefore:
$$\sqrt[5]{1-5x^2+x^4}=\sqrt[5]{1+(-5x^2+x^4)}\approx1+\frac{1}{5}(-5x^2+x^4)-\frac{2}{25}(-5x^2+x^4)^2+...$$

Thus the numerator can be rewritten as:
$$\sqrt[5]{1-5x^2+x^4}-1+x^2=$$
$$\big(1+\frac{1}{5}(-5(x^2+x^4)\big)-\frac{2}{25}(-5x^2+x^4)^2+O(x^5))-1+x^2)=$$
$$=1-x^2+\frac{1}{5}x^4+-2x^4+O(x^5)-1+x^2=-\frac{9}{5}x^4+O(x^5)$$

Hence:
$$
\lim\limits_{x\rightarrow0}\frac{\sqrt[5]{1-5x^2+x^4}-1+x^2}{x^4}=\lim\limits_{x\rightarrow0}\frac{-\frac{9}{5}x^4+O(x^5)}{x^4}=
$$

Ignoring all negligible summands:
$$=\boxed{\lim\limits_{x\rightarrow0}\frac{-\frac{9}{5}x^4}{x^4}=-\frac{9}{5}}$$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 6.
(c) Study the local behaviour of function:
$$f(x) = 	1-(x-2)^2+\frac{1}{4}(x-2)^3+O((x-2)^4),\quad x\rightarrow 2$$
in a neighbourhood of $x_0=2$, discuss whether it is a stationary point, and, if yes, of which type.

<div class = "answer">
Rewriting Taylor expansion for $f(x)$ of order $3$ centered at $x_0=2$ as:
\begin{equation*}
f(x)=f(2)+f'(2)(x-2)+\frac{1}{2!}f''(2)(x-2)^2+\frac{1}{3!}f'''(2)(x-2)^3+O\big((x-2)^4\big),\quad x\rightarrow2
\end{equation*}	

Then by comparing the coefficients of the rewritten form for f(x) to the f(x) in the question: 

\begin{align*}
&\textrm{Coefficient  for}&    &\textrm{Question}&       &\textrm{Rewritten}&  \newline 
\hline
& f(x-2)&    &1&                 &f(2)&    \\\ 
& f'(x-2)&   &0&                 &f'(2)&    \\\ 
& f''(x-2)&  -&1&                &\frac{1}{2!}f''(2)& \\\ 
& f'''(x-2)& &\frac{1}{4}&       &\frac{1}{3!}f'''(2)&  \newline
\hline
\end{align*}

Comparing the coefficients of the various degrees of $(x-2)$ in $f(x)$ and solving for each $f^{n}(2)$:
\begin{equation*}
f(2)=1,\quad f'(2)=0,\quad f''(2)=-1\times2!=-2,\quad f'''(2)=\frac{1}{4}\times3!=\frac{3}{2}.
\end{equation*}	
After finding the values of f'(2) and f''(2), it can be concluded that \ans{$x_0=2$ is a stationary point and, in particular, it is a local maximum of $f$.
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

## Exam Style Questions
### Problem 7.

(a) Evaluate the first five truncated Taylor polynomials (i.e. $0^{th}$, $1^{st}$...$5^{th}$) for:  $f(x)=\mathrm{\ln}(x),$ around ${}x=10$
<div class = "answer">
Find the Taylor Expansion of $f(x)=lnx$ near $x=10$ by finding the first, second, third, etc derivatives and evaluate them at $x = 10$.

Table of $f^{(n)}(0)$ coefficients for this series (Taylor, x=10):
\begin{align*}
& n&    f&^{(n)}(x)&       f&^{(n)}(10)&  \newline
\hline
& 0&    &\mathrm{ln}x&     &2.302585093&    \\\ 
& 1&    &\frac{1}{x}&     &\frac{1}{10}&    \\\ 
& 2&    -&\frac{1}{x^2}&    -&\frac{1}{100}& \\\ 
& 3&    &\frac{2}{x^3}&    &\frac{2}{1000}&    \\\ 
& 4&    &\frac{6}{x^4}&     -&\frac{6}{10000}&  \newline
\hline
\end{align*}

This function can be differentiated infinitely so the pattern in the table will continue forever. Substituting these values into the Taylor Series:
\begin{equation*}
f(x)\approx{f(a)+f{'}(a)(x-a)+\frac{f{''}(a)}{2!}(x-a)^2+\frac{f{'''}(a)}{3!}(x-a)^3+\frac{f{''''}(a)}{4!}(x-a)^4+...}
\end{equation*}

Results in:

\begin{equation*}
f(x)\approx{f(10)+f{'}(10)(x-10)+\frac{f{''}(10)}{2!}(x-10)^2+\frac{f{'''}(10)}{3!}(x-10)^3+\frac{f{''''}(10)}{4!}(x-10)^4+...} 
\end{equation*}

$$f(x)\approx{2.302585093+0.1(x-10)-\frac{0.01}{2!}(x-10)^2+\frac{0.002}{3!}(x-10)^3}$$
$$-\frac{0.0006}{4!}(x-10)^4+...$$
Expanding this all out and collecting like terms, we obtain the polynomial which approximates $lnx$:

\begin{equation*}
f(x)\approx0.21925+0.4x-0.03x^2+0.00133x^3-0.000025x^4+..
\end{equation*}

We see from the graph that our polynomial (in blue) is a good approximation for the graph of the natural logarithm function $f(x)=\mathrm{ln}x$ (in red) in the region near $x=10.$

<iframe src="https://www.desmos.com/calculator/4bdppcsgtv" width="100%" height="400px" style="border: 1px solid #ccc" frameborder=0></iframe>
</div>

(b) Sketch $f(x)$ and the first two truncated Taylor polynomials for the function expanded around the point $c=10$

<div class = "answer">
<iframe src="https://www.desmos.com/calculator/yuoqesic9a" width="100%" height="400px" style="border: 1px solid #ccc"></iframe>
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>


### Problem 8.
The first five terms of the Maclaurin series of function$f(x)=\frac{sin(\pi x)}{x}$ are
<br>
 $g_{4}(x)=\pi -\frac{\pi ^{3}x^{2}}{6}+\frac{\pi ^{5}x^{4}}{120}-\frac{\pi ^{7}x^{6}}{5040}+\frac{\pi ^{9}x^{8}}{362880}$<br><br>
(a) Find an expression for the term containing $x^{n}$ of the above series.
<br><br>
<div class = "answer">
$(-1)^{\frac{n}{2}}\frac{\pi ^{n+1}x^{n}}{(n+1)!}$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(b) Use the series above to help you sketch this function in the region $-3\leq x\leq 3$.
<div class = "answer">
<iframe src="https://www.desmos.com/calculator/eglb4hlnxb?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

<br><br>
(c)Add sketches of the zeroth, second, and fourth order truncated series approximations to your graph.
<div class = "answer">
<iframe src="https://www.desmos.com/calculator/g5jrscawf9?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------

## Challenging Questions
### Problem 9.

Find power series of $\frac{1}{x^{2}+4x+3}$ in term of $(x-1)$.
<br>
<div class = "answer">
$\frac{1}{x^{2}+4x+3}=\frac{1}{\left ( x+1 \right )\left ( x+3 \right )}= \frac{1}{2\left ( 1+x \right )}-\frac{1}{2\left ( 3+x \right )}$
<br><br>
write $x$ in form of $(x-1)$, knowing that $\left | x-1 \right |< 2$
<br><br>
$\Rightarrow \quad \frac{1}{4\left ( 1+\frac{x-1}{2} \right )}-\frac{1}{8\left ( 1+\frac{x-1}{4} \right )}$
<br><br>
$\Rightarrow \quad \frac{1}{4}\left [ 1-\frac{x-1}{2}+\frac{\left ( x-1 \right )^{2}}{2^{2}} +...+\left ( -1 \right )^{n}\frac{\left ( x-1 \right )^{n}}{2^{n}}+...\right ]-\frac{1}{8}\left [ 1-\frac{x-1}{4}+\frac{\left ( x-1 \right )^{2}}{4^{2}} +...+\left ( -1 \right )^{n}\frac{\left ( x-1 \right )^{n}}{4^{n}}+...\right ] $
<br><br>
$\Rightarrow \quad \sum_{n=0}^{\infty }\left ( -1 \right )^{n}\left ( \frac{1}{2^{n+2}} - \frac{1}{2^{2n+3}}\right )\left ( x-1 \right )^{n}$ for $-1< x< 3$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

### Problem 10.
(a)  Write the Maclaurin series expansion of the function up to the $4^{th}$ power:

$$f(x) = 	x \cos \left(\frac{x}{\sqrt{3}}\right)-(\alpha-x^3)\sin x \text{ for all } \alpha\in\mathbb{R}$$

Using this expansion, find for which $\alpha$ values of the point $x = 0$ is stationary for $f$ and specify of which type.

<div class = "answer">
Using the Maclaurin expansion of functions $\cos x$ and $\sin x$ we get that as
$x\rightarrow0$
\begin{equation*}
f(x)=x \cos \left( \frac{x}{\sqrt{3}}-(\alpha-x^3) \right) \sin x=
\end{equation*}
\begin{equation*}
x\left(1-\frac{1}{6}x^2+O(x^4)\right)-(\alpha-x^3)\big(x-\frac{1}{6}x^3+O(x^5)\big)=
\end{equation*}
\begin{equation*}
x-\frac{1}{6}x^3+O(x^5)-\alpha{x}+\frac{1}{6}\alpha{x^3}+x^4+O(x^5)=(1-\alpha)x-\frac{1}{6}(1-\alpha)x^3+x^4+O(x^5).
\end{equation*}

Hence the Maclaurin expansion of order $4$ of $f(x)$ is:
\begin{equation*}
f(x)=(1-\alpha)x-\frac{1}{6}(1-\alpha)x^3+x^4+O(x^5).
\end{equation*}

Since the Maclaurin expansion of order $4$ of $f$ is
\begin{equation*}
f(x)=f(0)+f'(0)x+\frac{1}{2}f''(0)x^2+\frac{1}{6}f'''(0)x^3+\frac{1}{24}f^{(4)}(0)x^4+O(x^5),
\end{equation*}

comparing the coefficients of each of the same order:
\begin{equation*}
f(0)=0,\quad f'(0)=1-\alpha,\quad f''(0)=0,\quad f'''(0)=\alpha-1,\quad f^{(4)}(0)=24.
\end{equation*}

For $x=0$ to be a stationary point, $\alpha=1$ so that $f'(0)=0$: 
$$f''(0) = f'''(0) = 0 \text{ and } f^{(4)}(0) = 24$$

It follows that $\boxed{\text{if } \alpha = 1 \text{ then } x = 0 \text{ is a local minimum of } f}$.
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>


## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>
<br><br>
### For Printing
<button type="button" onclick="prepareForPrint('block')">Add whitespace</button>
<button type="button" onclick="prepareForPrint('none')">Remove whitespace</button>

<br><br>

# Next week, ODEs!
