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

