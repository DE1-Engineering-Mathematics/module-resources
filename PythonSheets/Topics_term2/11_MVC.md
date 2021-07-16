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

# Multivariate Calculus

MVCs are an integral part of mathematics and they can be easily calculated with the sympy module in python.

## Calculating partial derivatives

Partial derivatives can be calculated with the `sympy.diff(f, x)` function. The function will differentiate the function `f` once with respect to `x`.

To take multiple derivatives, pass the variable as many times as you wish to differentiate.

For instance, if we were to derive `f` with respect to `x` and then to `y` we would write `sympy.diff(f, x, y)`.

Let's illustrate this by calculating $\frac{\partial (xy^3+x^2y^2)}{\partial x \partial y}$

```python3
import sympy

sympy.diff(x*y**3+x**2*y**2, x, y)
```