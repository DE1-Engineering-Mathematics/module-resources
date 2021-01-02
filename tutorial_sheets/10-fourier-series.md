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
<script src="https://www.desmos.com/api/v1.5/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
<script type="text/javascript" src="tutorialSheetScripts.js"> </script>
<link rel="stylesheet" type="text/css" media="all" href="styles.css">

# Fourier series, Tutorial sheet 10


### Additional resources
*insert links*

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
State the time period and formula of the following periodic functions.

(a)
<!-- Calculator using the desmos API woooo -->
<div id="prob1a" style="width: 600px; height: 300px;"></div>
<script>
    latex = "x-2\\pi\\operatorname{floor}\\left(\\frac{x}{2\\pi}+0.5\\right)"
    makeSimpleGraph("prob1a", latex, piOptions);
</script>

<div class = "answer">
$\boxed{\text{Period} =2\pi \qquad f(x)=x, \space \text{for} -\pi < x < \pi}$
</div>

(b)
<div id="prob1b" style="width: 600px; height: 300px;"></div>
<script>
    latex = "\\frac{\\pi}{2}\\left(\\left(2\\operatorname{floor}\\left(\\frac{x}{2\\pi}\\right)-\\frac{x}{\\pi}+1\\right)+\\operatorname{abs}\\left(2\\operatorname{floor}\\left(\\frac{x}{2\\pi}\\right)-\\frac{x}{\\pi}+1\\right)\\right)"
    makeSimpleGraph("prob1b", latex, piOptions);
</script>

<div class = "answer">
$\boxed{\text{Period} =2\pi \quad f(x)=\left\{
\begin{array}{ll}
\pi-x, &\quad 0 < x < \pi{} \\
0, &\quad \pi{} < x < 2\pi
\end{array}\right.
}$
</div>

(c)
<div id="prob1c" style="width: 600px; height: 300px;"></div>
<script>
    latex = "\\left(x-2\\pi\\operatorname{floor}\\left(\\frac{x}{2\\pi}+0.5\\right)\\right)^{2}"
    calc = makeSimpleGraph("prob1c", latex, piOptions);
    calc.setMathBounds({
        left: -9,
        right: 9,
        bottom: -1,
        top: 10,
    })
</script>

<div class = "answer">
$\boxed{\text{Period} = 2\pi \qquad f(x)=x^2, \text{ for } -\pi < x < \pi}$
</div>

-----------------------------------------------------------------------------------

### Problem 2.
Sketch the following periodic functions, stating their period:

(a) $f(x) = 3\sin\left(\frac{x}{2}\right)$, over the interval $-\pi < x < 2\pi$ for $-4\pi < x < 4\pi.$

<div class = "answer">
$\Rightarrow{} \text{Period} = 3\pi$

<div id="prob2a" style="width: 600px; height: 300px;"></div>
<script>
    latex = "3\\sin\\left(\\frac{\\left(x-3\\pi\\operatorname{floor}\\left(\\frac{x}{3\\pi}+\\frac{1}{3}\\right)\\right)}{2}\\right)"
    calc = makeSimpleGraph("prob2a", latex, piOptions);
    calc.setExpression({ 
        id: 'graph2', 
        latex: "x=-4\\pi"
    });
    calc.setExpression({ 
        id: 'graph3', 
        latex: 'x=4\\pi'
    });
</script>

</div>


(b) 
$f(t) = \left\\{ 
\begin{array}{ll}
-t &\quad -\pi < t < 0 \newline
t &\quad 0 < t < \pi \end{array}\right.$
for  $-3\pi< t < 3\pi$

<div class = "answer">
$\Rightarrow{} \text{Period} = 2\pi$

<div id="prob2b" style="width: 600px; height: 300px;"></div>
<script>
    latex = "\\operatorname{abs}\\left(x-2\\pi\\operatorname{floor}\\left(\\frac{x}{2\\pi}+\\frac{1}{2}\\right)\\right)"
    calc = makeSimpleGraph("prob2b", latex, piOptions);
    calc.setExpression({ 
        id: 'graph2', 
        latex: "x=-3\\pi"
    });
    calc.setExpression({ 
        id: 'graph3', 
        latex: 'x=3\\pi'
    });
</script>

</div>

(c) $f\left(p\right)=\left\\{\begin{array}{l}\frac{p^2}{2}\ \ \ \ \ 0 < p <4 \newline
    8\ \ \ \ \ \ 4 < p < 6 \newline
    0\ \ \ \ \ \ 6 < p < 8 \end{array}\right.
    $
    for $-16<p<16$
 
<div class = "answer">
$\Rightarrow{} \text{Period} = 8\pi$

<div id="prob2c" style="width: 600px; height: 300px;"></div> 
<script>
    latex = "\\min\\left(\\max\\left(\\frac{\\operatorname{sign}\\left(\\left(x-8\\operatorname{floor}\\left(\\frac{x}{8}+\\frac{1}{4}\\right)\\right)\\right)\\left(x-8\\operatorname{floor}\\left(\\frac{x}{8}+\\frac{1}{4}\\right)\\right)^{2}}{2},0\\right),8\\right)";
    calc = makeSimpleGraph("prob2c", latex, defaultGraphOptions);
    calc.setMathBounds({
        left: -16,
        right: 16,
        bottom: -1,
        top: 9,
    })
    calc.setExpression({ 
        id: 'graph2', 
        latex: "x=-16"
    });
    calc.setExpression({ 
        id: 'graph3', 
        latex: 'x=16'
    });
</script>
</div>

(d) $f\left(q\right)=2q-q^2\ \ \ \ \ \ \ 0< q < 2$, for $-8 < q < 8$
 
<div class = "answer">
$\Rightarrow{} \text{Period} = 8\pi$

<div id="prob2d" style="width: 600px; height: 300px;"></div> 
<script>
    latex = "2\\left(x-2\\operatorname{floor}\\left(\\frac{x}{2}\\right)\\right)-\\left(x-2\\operatorname{floor}\\left(\\frac{x}{2}\\right)\\right)^{2}";
    calc = makeSimpleGraph("prob2d", latex, defaultGraphOptions);
    calc.setMathBounds({
        left: -8,
        right: 8,
        bottom: -1,
        top: 2,
    })
    calc.setExpression({ 
        id: 'graph2', 
        latex: "x=-8"
    });
    calc.setExpression({ 
        id: 'graph3', 
        latex: 'x=8'
    });
</script>
</div>

------------------------------------

### Problem 3.
State whether the following functions are periodic, and if so, find their period:

(a) $\cos(x) + \sin(2x)$
<div class = "answer">
Periodic: Summing two periodic functions results in a function that is still periodic.

$\Rightarrow{} \boxed{ \text{Period } =2\pi}$
</div>

(b) $\sin{\left(x\right)}\cos{\left(x\right)}$

<div class = "answer">
Periodic: Multiplying two periodic functions results in a function that is still periodic

$\Rightarrow{} \boxed{ \text{Period } = \pi}$
</div>

(c) $e^x\sin^2(x)$

<div class = "answer">
Not periodic: Multiplying a periodic function, $sin^2(x)$, with a non periodic function, $\me^x$, results in a non periodic function. If you're struggling to show that $sin^2(x)$ is periodic, try writing it in terms of functions of $2x$.

$\Rightarrow{} \boxed{ \text{Not periodic }}$
</div>



-----------------------------------

## Exam Style Questions
### Problem 4.
**(a)** Given the real Fourier series expansion for a periodic function, $f(x)$, with a $2\pi{}$ period,
$$
f\left(x\right) = \frac{1}{2}a_0+\sum_1^{\infty{}}(a_n\cos{\left(nx\right)}+b_n \sin{(nx)}) \space ,
$$
find an expression for the coefficients, $C_n$, of the complex Fourier series,
$$
f\left(x\right) = \sum_{n=-\infty}^{\infty} C_n e^{i n x}
\space .
$$
Give your answer in terms of the real coefficients $a_0$, $a_n$, and $b_n$.

Next express $C_n$ in terms of $f(x)$.

Comment on the relationship between $C_n$ and $C_{-n}$ for real functions.

<div class = "answer">
Looking at the complex Fourier series, there are three differences from the real series:
there is a complex exponential instead of sines and cosines;
the sum is from $-\infty$ to $\infty$ rather than $1$ to $\infty$;
and there is an $a_0$ term.
Let's treat these in order.

First, use Euler's identity to convert the complex exponential to trig functions,

$$f\left(x\right) = \sum_{n=-\infty}^{\infty} C_n \left(
  \cos(n x) + i \sin(n x) \right)
\space .$$

Next, split out the sum into three parts, negative, zero, positive,
\begin{align*}
f\left(x\right) &=
\sum_{n=-1}^{-\infty} C_n \left( \cos(n x) + i \sin(n x) \right) \newline
&+ C_0 \newline
&+ \sum_{n=1}^{\infty} C_n \left( \cos(n x) + i \sin(n x) \right)
\;.
\end{align*}
For the negative sum, we can substitute $n$ for $-n$ as it is a variable within the sum (being summed over). Changing the limits and the coefficient to represent the same negative sum. Noting that $\cos$ is an even function and $\sin$ is odd so that $i \sin(n x)$ becomes $-i \sin(n x)$.
\begin{align*}
f\left(x\right) &=
\sum_{n=1}^{\infty} C_{-n} \left( \cos(n x) - i \sin(n x) \right) \newline
&+ C_0 \newline
&+ \sum_{n=1}^{\infty} C_n \left( \cos(n x) + i \sin(n x) \right)
\;.
\end{align*}
Now the sums are over the same range, they can be combined,
\begin{align*}
f\left(x\right) &= C_0 +
\sum_{n=1}^{\infty} \left( (C_n + C_{-n}) \cos(n x) + i(C_n - C_{-n}) \sin(n x) \right)
\;.
\end{align*}
By inspection, we can now compare terms from our expression to the real Fourier series,
\begin{align*}
    a_0 &= 2 C_0 \newline
    a_n &= C_n + C_{-n} \newline
    b_n &= i C_n -i C_{-n}
\end{align*}
Then to solve this part, rearrange these simultaneous equations in terms of $a_n$, $b_n$
\begin{align*}
    C_0 &= \frac{a_0}{2} \newline
    C_n &= \frac{a_n - i b_n}{2} \newline
    C_{-n} &= \frac{a_n + i b_n}{2}
\end{align*}

For the next part, we'll take our expression for $C_n$ and write the $a$ and $b$ terms as their integral forms.
\begin{align*}
C_n &= \frac{a_n - i b_n}{2} \newline
&= \frac{1}{2}\left(\frac{1}{\pi}\int_{-\pi}^{\pi} f(x) \cos(n x)- i \frac{1}{\pi}\int_{-\pi}^{\pi} f(x) \sin(n x) \right) \newline
&= \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x) \left( \cos(n x)- i \sin(n x) \right) \newline
C_n &= \frac{1}{2\pi}\int_{-\pi}^{\pi} f(x) e^{-i n x}
\end{align*}

Finally for the comment,
given $C_n = (a_n - i b_n) / 2$
and $C_{-n} = (a_n + i b_n) / 2$,
then for real functions, $a$ and $b$ are real,
so $C_{-n} = C_n^*$

</div>

**(b)** Find the real Fourier series to the following function.
$$\left(3+4i\right)e^{-2ix}+{\left(3-4i\right)e}^{2ix}$$

<div class = "answer">

$$
\Rightarrow{}\left(3+4i\right)\left\[\cos{\left(2x\right)-i\sin{\left(2x\right)}}\right]+\left(3-4i\right)\left\[\cos{\left(2x\right)+i\sin{\left(2x\right)}}\right] \\\\
$$

$$
=\left(3+4i\right)\cos{\left(2x\right)+}\left(4-3i\right)\sin{\left(2x\right)+}\left(3-4i\right)\cos{\left(2x\right)+\left(4+3i\right)\sin{\left(2x\right)}} \\\\
$$

$$
=\left\[\left(3+4i\right)+\left(3-4i\right)\right]\cos{\left(2x\right)+\left\[\left(4-3i\right)+\left(4+3i\right)\right\]\sin{\left(2x\right)}} \\\\
$$

$$
=6\cos{(2x)}+8\sin{(2x)} \\\\
$$

In second line, we must use the fact that $\left(3+4i\right)i=\ -4+3i$ and $\left(3-4i\right)i=4+3i$ in finding the coefficients in front of the $\sin{(2x)}$ term.
</div>


-----------------------------------

## Challenging Questions
### Problem 6.
For the following functions
(I) Find the Fourier coefficients and series in the given interval,
(II) Plot the function and the given partial sum over the given interval.

(a) $f\left(x\right)=x^3,\ \ \ for\ \left\[-1,1\right]$, with n = 5

<div class = "answer">
The first step is to work out whether the function $f\left(x\right)=x^3$ is odd, even, or both. This can be done by eye for a simple function like $x^3$. To check, or for harder functions, the formulae found in the notes can be used:

$$
f_{\textrm{even}}(x)=\frac{f(x)+f(-x))}{2} \qquad \qquad
f_{\textrm{odd}}(x)=\frac{f(x)-f(-x))}{2}
$$

the function $f\left(x\right)=x^3$ is odd, so the Fourier series representation will only contain sine terms.

The sine coefficients can be found using:

$$
b_n = \frac{1}{L} \int_{-L}^{L}f(x)\sin\left(\frac{n\pi x}{L}\right) dx
$$


where $L=1$. Due to the fact that $x^3$ is an odd function, integrating it between $\pm1$ will give a resultant area of 0. We can get around this by:

\begin{align*}
b_n &=\frac{1}{1} \int_{-1}^{1}x^3\sin\left(\frac{n\pi x}{1}\right) dx
\newline \newline
&=
\int_{0}^{1}x^3\sin\left(n\pi{}x\right) dx + \int_{-1}^{0}x^3\sin\left(n\pi{}x\right) dx
\newline \newline
&=
2\int_{0}^{1}x^3\sin\left(n\pi{}x\right) dx
\end{align*}

Using integration by parts: $\int f^{'}g=fg-\int fg^{'}$

\begin{align*}
b_n &= -\frac{2x^3\cos{\left(n\pi{}x\right)}}{n\pi{}}+\frac{{6x}^2\sin{\left(n\pi{}x\right)}}{n^2{\pi{}}^2}+\frac{12x\cos{\left(n\pi{}x\right)}}{n^3{\pi{}}^3}-\left.\frac{12\
\sin(n\pi{}x)}{n^4{\pi{}}^4}\right\vert{}\binom{1}{0}
\newline
&=\
-\frac{2\cos{\left(n\pi{}\right)}}{n\pi{}}+\frac{12\cos{\left(n\pi{}\right)}}{n^3{\pi{}}^3}={(-1)}^n\frac{2(6-n^2{\pi{}}^2)}{n^3{\pi{}}^3}
\end{align*}

Note that $\sin(\textit{n$\pi$}) = 0$, and $\cos(\textit{n$\pi$}) = (-1)^n...$ if you're not sure why, try drawing the curves.

$\therefore$ the Fourier series representation is:

$$ \boxed{
f\left(x\right)=\sum_{n=1}^{\infty{}}{(-1)}^n\frac{2(6-n^2{\pi{}}^2)}{n^3{\pi{}}^3}\
\sin{(n\pi{}x)}
}$$

</div>

### Problem 7.
In the following exercises, find the complex Fourier series representation of the given function $f(x)$ over the interval [-$\pi{}$, $\pi{}$]

(a) $f(x) = x^3$

<div class = "answer">

$$
C_n=\frac{1}{2\pi{}}\int_{-\pi{}}^{\pi{}}x^3e^{-inx}dx
$$

Using the integration by parts, we have

\begin{align*}
C_n &=\frac{1}{2\pi{}}\left\[\frac{{ix}^3e^{-inx}}{n}+\frac{{3x}^2e^{-inx}}{n^2}-\frac{{i6xe}^{-inx}}{n^3}-\frac{{6e}^{-inx}}{n^4}\right]\binom{\pi{}}{-\pi{}} 
\newline \newline 
&=\
\frac{1}{2\pi{}n^4}\left\[e^{-inx}(in^3x^3+3n^2x^2-i6nx-6\right]\binom{\pi{}}{-\pi{}}
\newline \newline
&=\
\frac{1}{2\pi{}n^4}\left\[{\left(-1\right)}^n\left(-in^3{\pi{}}^3+{3n}^2{\pi{}}^2-i6n\pi{}-6\right)-{\left(-1\right)}^n(-in{\pi{}}^3+3n^2{\pi{}}^2+i6n\pi{}-6\right]
\newline \newline
&=
\frac{{(-1)}^n}{2\pi{}n^4}\left\[{2in}^3{\pi{}}^3-12in\pi{}\right]=\frac{{\left(-1\right)}^n}{n^3}\left(n^2{\pi{}}^2-6\right), \ \ \ \ for\ n\not=0 \newline \newline
\end{align*}

$$
\Rightarrow \quad C_0=\frac{1}{2\pi{}}\int_{-\pi{}}^{\pi{}}x^3dx=0,\ \ \ for\ n=0
$$

Since $x^3$ is odd on $\left\[-\pi{},\pi{}\right]$. Hence,

$$
f\left(x\right)=\
\sum_{n=-\infty{}}^{\infty{}}C_ne^{inx}=\sum_{n\not=0}\frac{{\left(-1\right)}^ni(n^2{\pi{}}^2-6)}{n^3}e^{inx}
$$

</div>

(b) $f\left(x\right)=\left\\{\begin{array}{l}0,\ \ \ -\pi{}\leq{}x<0, \newline
1,\ \ \ \ \ 0\leq{}x<\ \pi{}\end{array}\right.$

<div class = "answer">
$$
C_n=\frac{1}{2\pi{}}\int_{-\pi{}}^{\pi{}}f(x)e^{-inx}dx=\frac{1}{2\pi{}}\int_0^{\pi{}}e^{-inx}dx=\frac{1}{2\pi{}}\left[\frac{e^{-inx}}{-in}\right]\binom{\pi{}}{0} \\\\
$$

$$
=-\frac{1}{2\pi{}in}\left\[e^{-inx}-1\right]=\frac{1-{(-1)}^n}{2\pi{}in} \\\\
$$

$$
\Rightarrow{}\ \ \left\\{\begin{array}{l}0,\ \ \ \ \ \ \ \ n\ even, \newline
\frac{1}{\pi{}in},\ \ \ \ n\ odd,\ \end{array}\right.\ ,\ for\ n\not=0. \\\\
$$

$$
C_0=\frac{1}{2\pi{}}\int_{-\pi{}}^{\pi{}}f\left(x\right)dx=\frac{1}{2\pi{}}\int_0^{\pi{}}dx=\frac{1}{2},\
\ \ \ \ \
$$

Thus,

$$
f\left(x\right)\approx\sum_{n=-\infty{}}^{\infty{}}C_ne^{inx}=\frac{1}{2}+\sum_{n\
odd}\frac{1}{\pi{}in}e^{inx}
$$
</div>

## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>

<br><br>

# Next week, another topic!
![vectors](02-vectors-media/cover.png)