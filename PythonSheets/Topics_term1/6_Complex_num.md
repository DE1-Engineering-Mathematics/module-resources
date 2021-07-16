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

# Complex numbers

Once again the sympy module will be used. We only need to import part of the module to manipulate complex numbers:

```python
from sympy import Abs, Symbol, S, I
```

## Manipulating complex numbers

Complex numbers can be written like this `2*I+3`.

Here is a list of the essential functions:

- `re(x)` returns the real part of a complex number x
- `im(x)` returns the imaginary part of a complex number x
- `abs(x)` returns the absolute value of the argument of a complex number x
- `arg(x)` returns the argument (in radians) of a complex number x
- `conjugate(x)` returns the conjugate of a complex number x