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

## [Return to Contents](notes-contents)

<img src="figs/xkcdFourierCat.jpg" width="200"/>

# Chapter 11 - The Laplace Transform

## <a id="origins-of-laplace"></a>11.1 Origins of the Laplace transform
To understand what Laplace transforms are and where they come from, it's useful to think back to power series. In the following equation, we simply state the generic power series formulation, which is the infinite sum of terms containing powers of $x^n$, each with it's own corresponding coefficient $a_n$. This polynomial will return us a number if we feed it a value of $x$, so we can say that it is equal to some function of $x$, which we will call $A(x)$. <br><br>

$$a_0+a_1x+a_2x^2+a_3x^3+...\equiv\sum_{0}^{\infty}a_nx^n=A(x)$$

<br><br>
We can now make a small modification to the notation and replace the subscript notation, $a_n$, with a totally equivalent functional notation, where $a(n)$ is a function which takes a natural number $n=0,1,2,3...$ and returns another number $a(n)$. So we can now write the near identical expression:<br><br>

$$\sum_{0}^{\infty}a(n)x^n=A(x)$$

<br><br>
However, this expression allows us to see the power series in a new light, where we are really just *associating* (wiggly arrow) the two functions $a(n)$ and $A(x)$, via the power series. <br><br>

$$a(n)\rightsquigarrow A(x)$$

<br><br>
So, if you are given a function $a(n)$, which returns coefficients as a function of $n$,  what you get back through this power series association is a function $A(x)$ describing the sum of that power series as a function of $x$. For example, consider the simple function $a(n)=1$, which is just the case where for *any* value of $n$, $a(n)$ will always equal 1. Our power series simply becomes

$$1+x+x^2+x^3+...\equiv\sum_{0}^{\infty}x^n=A(x)$$

<br><br>
Thinking back to our chapter on sequence and series, the above expression is simply a geometric series, where the first term is 1 and the common ratio is $x$, so substituting this into our expression for the summation of a geometric series to $m$ terms, we get,<br><br>

$$S_m   =a_1\frac{1-r^{m}}{1-r} \qquad\qquad\Rightarrow{\text{substitute}}\qquad\qquad
A(x)   =\lim_{n\to \infty}\left( \frac{1-x^{n}}{1-x}\right)$$

<br><br>

By analysing the convergence of the above expression, we can see that this summation can only be evaluated when $|x|<1$ (in which case $\lim_{n\to\infty}(x^n)=0)$. So we can now say that
<br><br>

$$\sum_{0}^{\infty}x^n=\frac{1}{1-x}\ , \qquad |x|<1$$

<br><br>

Bringing all of the above together,  we have just found our first example of an association, where in general $a(n)\rightsquigarrow A(x)$ and in our specific case described above $1\rightsquigarrow \frac{1}{1-x}\ ,\quad |x|<1$.
<br><br>

Let's try another example, think of the case where $a(n)=\frac{1}{n!}$.<br><br>

$$1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+...\equiv\sum_{0}^{\infty}\frac{1}{n!}x^n=A(x)$$

<br><br>
We saw from our power series chapter that this series converges to $e^x$ for all $x$, so we've now found our second association.<br><br>

$$\frac{1}{n!}\rightsquigarrow e^x$$

<br><br>

### 11.1.1 Discrete to continuous
This is now where the magic happens... Our function $a(n)$ took a natural number as its input, but what if instead we used a function $a(t)$ that would take any positive real number $0\leq t<\infty$ (ie we are going from discrete to continuous). We can now no longer use the discrete sum operation, but instead we must use its continuous analogue, integration.<br><br>

$$\sum_{0}^{\infty}a_nx^n=A(x)\ ,\quad |x|<1
\qquad\quad\Rightarrow{\text{discrete to continuous}}\qquad\quad
\int_{0}^{\infty}a(t)x^t\textrm{d}t=A(x)\ ,\quad 0<x<1$$

<br><br>

Similar to the summation case, for this integral to stand any chance of converging, we will need $x<1$ so that evaluating the limit $t=\infty$ will not cause it to explode. Also, to ensure that the answer is real (as opposed to complex), we must now also keep $x$ positive, so $0<x<1$. <br><br>

Although the integral expression above is a valid form of the variable transformation we are looking for, very often it's more convenient to integrate '$e$ to the power of something' rather than '$x$ to the power of something'. So, we simply use our rule of logs and remember that $x=e^{\ln(x)}$ and therefore $x^t=e^{t\ln(x)}$.<br><br> 

$$\int_{0}^{\infty}a(t)x^t\textrm{d}t=A(x)\ ,\quad 0<x<1 
\quad\Rightarrow{\text{rearrange}}\quad
\int_{0}^{\infty}a(t)e^{t\ln(x)}\textrm{d}t=A(x)\ ,\quad \ln(x)<0$$

<br><br>
At this point we are going to make one more adjustment, just to clean everything up. Rather than having this annoying '$\ln(x)$' term (because of the range of $x$, we also know '$\ln(x)$' is going to be negative), we are simply going to make a substitution. We will introduce a new variable $s=-\ln(x)$ <br><br>

$$\int_{0}^{\infty}a(t)e^{t\ln(x)}\textrm{d}t=A(x)\ ,\quad \ln(x)<0
\qquad\Rightarrow{\text{substitute $s$}}\qquad
\int_{0}^{\infty}a(t)e^{-st}\textrm{d}t=A(s)\ ,\quad s>0$$

<br><br>
The final thing left for us to do is just to make the expression look more familiar. Currently, we have the function $a(t)$, but more typically, we call functions $f(t)$ (not that this makes any difference, but this is how you will see it written elsewhere). We now have the final expression. <br><br>

$$\textbf{Laplace Transform:} \qquad\qquad \int_{0}^{\infty}f(t)e^{-st}\textrm{d}t=F(s)\ ,\quad s>0$$

<br><br>

### 11.1.2 Definitions and details
It's worth noting here that you can now see for yourself the difference between a transform and an operator. The majority of the maths you'll have met so far deals with operators \eg differentiation), transforms change the variable. It's typical, when transforming a function, $f(t)$, to use the upper case letter $F$ to represent the equivalent transformed function, in order to highlight the link between the two. You will also sometimes see $\tilde{f}(s)$, instead of $F(s)$, as the upper case may already have been used for something else. <br><br>

$$f(t)\quad\Rightarrow{\text{Transform}}\quad F(s)
\qquad\qquad\qquad\qquad
f(t)\quad\Rightarrow{\text{Operator}}\quad g(t)$$

<br><br>
Other notation conventions include the use of the swirly `$\mathcal{L}$' symbol to denote a Laplace transform. So we can write  $\mathcal{L}\{f(t)\} = F(s)$, often (but not always) using 'braces' $\{\}$ instead of brackets $()$. Finally, we can also still use the wiggly arrow for this purpose, writing $f(t)\rightsquigarrow\tilde{f}(s)$.<br><br>

Another detail that we have not discussed yet is the improper integral $\int_{0}^{\infty}$, which needs special treatment. The integral of a function over an infinite interval is the limit of the integral over a finite interval as the bound on the interval tends to infinity. In symbols:<br><br>

$$\int_{0}^{\infty}{f(t)}\textrm{d}t = \lim_{k\to\infty}\int_{0}^{k}f(t)\textrm{d}t$$

<br><br>
So, first solve the finite form of the integral then find the limiting value as we let $k$ tend to $\infty$.<br><br>

<br><br>

Finally, the Laplace transform is a *linear* transform, which means that it obeys our convenient rules of linearity. So,<br><br>

$$\begin{align}
	\mathcal{L}\{f(t)+g(t)\}&=\mathcal{L}\{f(t)\}+\mathcal{L}\{g(t)\}\\
	\mathcal{L}\{cf(t)\}&=c\mathcal{L}\{f(t)\}
\end{align}$$

<br><br>
This will be very handy when we want to transform long expressions, as we can now break them up into parts.

## <a id="what-does-it-mean"></a>11.2 But what does it mean?
You know where Laplace transforms come from, how to calculate one and how to write them down, but what do they mean?  It's easy enough to formally state what a Laplace transform is, but less easy to explain exactly what it does. One clue is that the reason for using $t$ as the variable in our original function $f(t)$ is that we often apply Laplace transforms to functions of time, which gives a small hint as to what $s$ might be. <br><br>

Formally, we can state that: 'Given $f$, a function of time, with value $f(t)$ at time $t$, the Laplace transform of $f$ gives us an average value of $f$ taken over all positive values of $t$ such that the value $\tilde{f}(s)$ represents an average of $f$ taken over all possible time intervals of length $s$.' ... Not hugely illuminating. <br><br>

 In fact Laplace transforms are strongly motivated by real engineering problems, where typically we encounter models for the dynamics of phenomena which depend on rates of change of functions, eg velocities and accelerations of particles or points on rigid bodies, prompting the use of ordinary differential equations (ODEs). We can use ordinary calculus to solve ODEs, provided that the functions are nicely behaved, which means continuous and with continuous derivatives. Unfortunately, there is much interest in engineering dynamical problems involving functions that input step change or spike impulses to systems (eg collisions of snooker balls). Now, there is an easy way to smooth out discontinuities in functions of time: simply take an average value over all time. But an ordinary average will replace the function by a constant, so we use a kind of moving average which takes continuous averages over all possible intervals of $t$. This very neatly deals with the discontinuities by encoding them as a smooth function with interval length $s$.<br><br>

The amazing thing about using Laplace Transforms is that we can convert a whole ODE initial value problem into a Laplace transformed version as functions of $s$, simplify the algebra, find the transformed solution $\tilde{f}(s)$ and then finally undo the transform to get back to the required solution $f$ as a function of $t$.<br><br>

Interestingly, it turns out that the transform of a derivative of a function is a simple combination of the transform of the function and its initial value. So a calculus problem can be converted into an algebraic problem involving polynomial functions, which is typically easier to solve.<br><br>

In this course we find some Laplace Transforms from first principles (ie from the definition equation), describe some theorems that help finding more transforms, then use Laplace Transforms to solve problems involving ODEs.<br><br>

## <a id="finding-laplace"></a>11.3 Finding Laplace Transforms
We have three methods to find $\tilde{f}(s)$ for a given $f(t)$: <br><br>

**1. From the definition**:  $\quad \mathcal{L}\{f(t)\}=\int_{0}^{\infty}f(t)e^{-st}\textrm{d}t=F(s)\ ,\quad s>0$ <br><br>

$$\begin{alignat}{2}
	\text{For}\quad f(t) &= 0,\qquad \mathcal{L}\{0\} = \int_{0}^{\infty}0\textrm{d}t = 0 \\
	\text{For}\quad f(t) &= 1,\qquad \mathcal{L}\{1\} &&= \int_{0}^{\infty}e^{-st}\textrm{d}t= \left[-\frac{1}{s}e^{-st}\right]_{0}^{\infty} = \frac{1}{s} \\
	\text{For}\quad f(t) &= t,\qquad \mathcal{L}\{t\} &&= \int_{0}^{\infty}te^{-st}\textrm{d}t = \left[-\frac{t}{s}e^{-st}\right]_{0}^{\infty} + \frac{1}{s}\int_{0}^{\infty}{e^{-st}} = \frac{1}{s^{2}} \\
	\text{For}\quad f(t) &= \frac{\textrm{d}y}{\textrm{d}t},\qquad \mathcal{L}\left\{\frac{\textrm{d}y}{\textrm{d}t}\right\} &&= \int_{0}^{\infty}e^{-st}\frac{\textrm{d}y}{\textrm{d}t}\textrm{d}t = \left[e^{-st}y\right]_{0}^{\infty} + s\int_{0}^{\infty}{e^{-st}y}\textrm{d}t = s\tilde{y}(s)-y(0) \\
	\text{For}\quad f(t) &= \frac{\textrm{d}^2y}{\textrm{d}t^2},\qquad \mathcal{L}\left\{\frac{\textrm{d}^2y}{\textrm{d}t^2}\right\} &&= \int_{0}^{\infty}e^{-st}\frac{\textrm{d}^2y}{\textrm{d}t^2}\textrm{d}t = \text{int. by parts}\times2 = s^2\tilde{y}(s)-sy(0)-y'(0) \\\\
	\text{For}\quad f(t) &= e^{at},\quad (a=\text{constant}) \\
	\mathcal{L}\{e^{at}\} &= \int_{0}^{\infty}e^{-st}e^{at}\textrm{d}t &&= \int_{0}^{\infty}e^{-(s-a)t}\textrm{d}t = \left[-\frac{1}{s-a}e^{-(s-a)t}\right]_{0}^{\infty} = \frac{1}{s-a},\quad s > a
\end{alignat}$$

<br><br>

**2. From a property**: There are a number of powerful theorems about the properties of transforms: eg <br><br>

$$\mathcal{L}\{af + bg\} = a\mathcal{L}\{f\} + b\mathcal{L}\{g\}
\qquad\Rightarrow{\text{for example}}\qquad
\mathcal{L}\{3t + 4\} = 3\frac{1}{s^2} + 4\frac{1}{s}$$

<br><br>
Also, as per De Moivre's theorem (\ie $\cos(at)+i\sin(at)=e^{iat}$):<br><br>

$$\mathcal{L}\{e^{iat}\} = \frac{1}{s - ia} 
\qquad\Rightarrow{\text{realise denominator}}\qquad
\mathcal{L}\{e^{iat}\}= \frac{s}{s^{2} + a^{2}} + \frac{ia}{s^{2} + a^{2}}$$

<br><br>
Hence, equating real and imaginary parts and using linearity,<br><br>

$$\begin{align}
	\mathcal{L}\{\cos(at)\} = \frac{s}{s^{2}+a^{2}} \qquad\qquad \& \qquad\qquad	\mathcal{L}\{\sin(at)\} = \frac{a}{s^{2} + a^{2}}
\end{align}$$

**3. From a list**: Computer algebra packages like Mathematica, Matlab and Maple know Laplace Transforms of all the functions you are likely to encounter, so you have access to these online, and the packages have also an inversion routine to find a function $f(t)$ from a given $\tilde{f}(s)$. There are books with long lists of transforms of known functions and compositions of functions; eg some that are harder to calculate:<br><br>

$$\begin{align}
&\mathcal{L}\{t^{n}\} = \frac{n!}{s^{n+1}}, \quad n = 0,1,2,\dots,\\ &\mathcal{L}\{t^{1/2}\} = \frac{1}{2}\left(\frac{\pi}{s^{3}}\right)^{1/2},\\ &\mathcal{L}\{t^{-1/2}\} = \left(\frac{\pi}{s}\right)^{1/2}\\
&\mathcal{L}\left\{\frac{\textrm{d}^ny}{\textrm{d}t^n}\right\}=s^n\tilde{y}-\sum_{k=1}^{n} s^{k-1}y^{(n-k)}(0)
\end{align}$$

<br><br>

### 11.3.1 Finding inverse transforms using partial fractions
Given a function $f$, of $t$, we denote its Laplace Transform by $\mathcal{L}\{f\} = \tilde{f}$; the inverse process is written:<br><br>

$$\mathcal{L}^{-1}\left\{\tilde{f(s)}\right\} = f(t)
%\qquad\qquad\mathcal{L}^{-1}\{\tilde{f(s)}\}=\int_{0}^{\infty}f(t)e^{-st}\dd{t}=F(s)\ ,\quad s>0$$

<br><br>
A common situation is when $\tilde{f}(s)$ is a polynomial in $s$, or more generally, a ratio
of polynomials; then we use partial fractions to simplify the expressions. Given an expression for a Laplace transform of the form $N/D$ where the numerator, $N$, and denominator, $D$, are both polynomials of $s$; use partial fractions:%possibly in the form of factors, and $N$ may be constant<br><br>

1. if $N$ has degree equal to or higher than $D$, divide $N$ by $D$ until the remainder is of lower degree than $D$
<br>

2. For every linear factor like $(as + b)$ in $D$, write a partial fraction of the form $A/(as + b)$<br>

3. For every repeated factor like $(as + b)^{2}$ in $D$ write two partial fractions of the form $A/(as + b)$ and $B/(as + b)^{2}$. Similarly for every repeated factor like $(as + b)^{3}$ in $D$ write three partial fractions of the form $A/(as + b)$, $B/(as + b)^{2}$ and $C/(as + b)^{3}$; and so on.<br>

4. For quadratic factor $(as^{2}+bs+c)$ write a partial fraction $(As+B)/(as^{2}+bs+c)$

<br><br>
For repeated quadratic factors write a series of partial fractions, but with numerators of the form $(As + B)$ and successive powers of the quadratic factor as the denominators.<br><br>

With a little more algebra you should in this way be able to write the original expression as a sum of simpler transforms, which are found in your table. You then add their inverse transforms together, to get the inverse of the original transform.<br><br>

## <a id="solving-ODE"></a>11.4 Solving ODEs and ODE Systems
The application of Laplace transforms is particularly effective for *linear* ODEs, and for systems of such ODEs. To transform an ODE, we need the appropriate initial values of the function involved and initial values of its derivatives. <br><br>

Consider the example, from our ODE chapter, of an overdamped harmonic oscillator with the equation shown below. In this case, the trolley starts with an initial displacement and an initial velocity. <br><br>

$$\ddot{x}+3\dot{x}+2x=0 \qquad\text{where, at}\qquad t=0:\quad x(0)=5\quad \&\quad \dot{x}(0)=7$$ 

<br><br>
We can Laplace transform this system by considering each term separately <br><br>

$$\left[s^2X-sx(0)-\dot{x}(0)\right]+3\left[sX-x(0)\right]+2\left[X\right]=0$$

<br><br>
Then we can factorise to<br><br> 

$$\left(s^2+3s+2\right)X-(s+3)x(0)-\dot{x}(0)=0$$

<br><br>
Substitute in our initial values<br><br>


$$\left(s^2+3s+2\right)X-(s+3)5-7=0$$

<br><br>
Rearranging for $X$<br><br>


$$X=\frac{22+5s}{s^2+3s+2}
\qquad\Rightarrow{\text{partial fractions}}\qquad
X=\frac{17}{s+1}-\frac{12}{s+2}$$

<br><br>
Finally, we can look up the inverse transform from a table and write down the solution in the time domain.<br><br>

$$x=17e^{-t}-12e^{-2t}$$

<br><br>

The example we've just worked through was a homogeneous second order ODE. We can also apply Laplace to solve **heterogeneous** ODEs (ie where the right hand side of the equation does not equal zero). Modifying our example to include a force which grows with a function of time.  <br><br>

$$\ddot{x}+3\dot{x}+2x=4t-6 \qquad\text{where, at}\qquad t=0:\quad x(0)=5\quad \&\quad \dot{x}(0)=7$$

<br><br>
We simple transform each term and grind through the algebra once again:

$$\left[s^2X-sx(0)-\dot{x}(0)\right]+3\left[sX-x(0)\right]+2\left[X\right]=\frac{4}{s^2}-\frac{6}{s}
\qquad\Rightarrow{\text{many steps...}}\qquad
x=27e^{-t}-16e^{-2t}+2t-6$$

<br><br>
Laplace transforms also allow us to solve systems that we would struggle with in the time domain, such as step inputs and impulse problems, where all we'd need to do is look up the transform of the relevant additional terms and work through the algebra. <br><br>

### Frequently used Laplace Transforms

<br>

$$\begin{alignat}{2}
	&\textbf{Function}  &&\textbf{Transformed function} \\ &f(t) && \tilde{f}(s) = \int_{0}^{\infty}e^{-st}f(t)dt \\
	&0 &&0\\
	&1 &&1/s\\
	&t^{n},\text{ for } n = 0,1,2,\dots &&n!/s^{n+1} \\
	&t^{1/2} &&\frac{1}{2}(\pi/s^{3})^{1/2} \\
	&t^{-1/2} &&\left(\frac{\pi}{s}\right)^{1/2} \\
	&e^{at} &&1/(s-a) \\
	&\sin({\omega t}) &&\omega/(s^{2}+\omega^{2}) \\
	&\cos({\omega t}) &&s/(s^{2}+\omega^{2}) \\
	&t\sin({\omega t}) &&2\omega s/(s^{2}+\omega^{2})^{2} \\
	&t\cos({\omega t}) &&(s^{2}-\omega^{2})/(s^{2}+\omega^{2})^{2} \\
	&e^{at}t^{n} &&n!/(s-a)^{n+1} \\
	&e^{at}\sin({\omega t}) &&w/((s-a)^{2} + \omega^{2}) \\
	&e^{at}\cos({\omega t}) &&(s-a)/((s-a)^{2} + \omega^{2}) \\
	&\sinh({\omega t}) &&\omega/(s^{2} - \omega^{2}) \\
	&\cosh({\omega t}) &&s/(s^{2} - \omega^{2}) \\
	&\textbf{Impulse: }(\text{Dirac }\delta): \delta(t-a) \quad \left(\neq 0\text{ at } t = a\text{, else } = 0\right) \quad &&e^{-as} \\
	&\textbf{Step function: }H_{a}(t) (=0\text{ for }t < a\text{ and } = 1, t\geq a ) &&e^{-as}/s \\
	&\textbf{Delay of g: }H_{a}(t)g(t-a) &&e^{-as}\tilde{g}(s) \\
	&\textbf{Shift of g: }e^{at}g(t) &&\tilde{g}(s-a) \\
	&\textbf{Convolution: }f(t)*g(t) =\int_{0}^{t}f(t -\tau)g(\tau)d\tau && \tilde{g}(s)\tilde{f}(s) \\
	&\textbf{Integration: }1*g(t) = \int_{0}^{t}g(\tau)d\tau &&\frac{1}{s}\tilde{g}(s) \\
	&\textbf{Derivative: }y' &&s\tilde{y}(s) - y(0) \\
	&\textbf{Derivative: }y'' &&s^{2}\tilde{y}(s) - sy(0) - y'(0)
\end{alignat}$$

<br><br><br><br><br><br>