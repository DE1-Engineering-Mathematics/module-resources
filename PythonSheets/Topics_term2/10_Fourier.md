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

# Fourier series

Once again we will by using the sympy module.

## Compute fourier expansion

`sympy.fourier_series(f, (x, a, b))` can be used to calculate the fourier series of the function `f` for `x` ranging from `a` to `b`.

For example, $f\left(x\right)=x^3, \ \ for\ \left[ -1,1\right]$ for n=5 can be computed with: 

```python
from sympy import fourier_series, pi
from sympy.abc import x
f = x**3
s = fourier_series(f, (x, -1, 1))
s1 = s.truncate(n=5) # only return first 5 nonzero terms of the series
```

## Plot fourier series

Sympy can also be used to plot a fourier series, here is a step-by-step guide on how to do this.

1. Import module

```python
from sympy import fourier_series, pi, plot
from sympy.abc import x
```

2. Define function

Here we create the function f(x)=x

```python
f = x
```

3. Calculate fourier series

We can now calculate the fourier series for x between -pi and pi

```python
s = fourier_series(f, (x, -pi, pi))
```

4. Calculate approximations

Let's calculate the 3th, 5th and 7th term approximations

```python
s1 = s.truncate(n = 3)
s2 = s.truncate(n = 5)
s3 = s.truncate(n = 7)
```

5. Plot the graphs

```python
p = plot(f, s1, s2, s3, (x, -pi, pi), show=False, legend=True)

p[0].line_color = (0, 0, 0)
p[0].label = 'x'
p[1].line_color = (0.7, 0.7, 0.7)
p[1].label = 'n=3'
p[2].line_color = (0.5, 0.5, 0.5)
p[2].label = 'n=5'
p[3].line_color = (0.3, 0.3, 0.3)
p[3].label = 'n=7'

p.show()
```