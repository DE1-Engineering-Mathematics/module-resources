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

# Partial Differential Equations

PDEs can be also solved with the sympy module and the `pdsolve` function.

Here is how this can be done, step by step to solve the PDE 1 + (2*(ux/u)) + (3*(uy/u)):

1. Import sympy

```python
from sympy.solvers.pde import pdsolve
from sympy import Function, Eq
```

2. Create symbols

We need to tell sympy that the letters `x` and `y` represents a symbol whilst `f` is a function..

```python
from sympy.abc import x, y
f = Function('f')
```

3. Calculate derivatives and define equation

```python
u = f(x, y)
ux = u.diff(x)
uy = u.diff(y)

eq = Eq(1 + (2*(ux/u)) + (3*(uy/u)), 0)
```

4. Solve the PDE.

```python
pdsolve(eq)
```