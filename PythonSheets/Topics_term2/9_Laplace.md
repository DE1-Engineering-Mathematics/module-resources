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

# Laplace transforms

Once again we will by using the sympy module.

## Calculating laplace transforms

Laplace transforms can be computed using the `laplace_transform(f, t,s )` function where `t` and `s` are sympy symbols and `f` is a function.

For example, the laplace of $f(t)=6e^{-5t}+e^{3t}-5t^{3}-9$ can be calculated with:

```python
import sympy
t, s = sympy.symbols('t, s')
f = 6*sympy.exp(-5*t)+sympy.exp(3*t)-5*t**3-9
sympy.laplace_transform(f, t, s)
```

## Calculating inverse laplace transforms

Likewise inverse laplace transforms can be computed using the `sympy.inverse_laplace_transform(F, s, t)` function where `t` and `s` are sympy symbols and `F` is a function.