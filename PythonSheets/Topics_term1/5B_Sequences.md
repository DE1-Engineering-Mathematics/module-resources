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

# Sequences

Python's built in `for` loops are a great tool at solving these kinds of problems. Let's take a look.

## Evaluating series

This can be solved with a simple `for` loop.

For example $\sum_{r=1}^{20}{\left(r+1\right)}^3$ can be solved with the following code:

```python
s_sum=0

for r in range(1,20+1):
    s_sum += (r+1)**3

print("The sum of series is", s_sum)
```


<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/73292bc573?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

</details>

## Writing sequences

Sequences can be written in sympy with the `sequence(x, (x, a, b))` function. Here x represents a mathematical symbol and this is declared with `x = Symbol('x')`, whilst `a` and `b` define the [a, b] interval which the terms of the series are in.

Here is an example to write the sequence n^2 for n bigger than 0:

```python
from sympy import *
from sympy.abc import n

s = SeqFormula(n**2, (n, 0, oo)) # oo is infinity
```

The following functions are useful when using sequences in sympy:

- `s.coeff(i)` returns the ith term of the sequence s
- `s.formula` shows the formula used in the sequence s

<details>
<summary>Try it out</summary>

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@JackBeaumont/writingsequences?lite=true"></iframe></iframe>
</details>

## Divergence test

Sympy is also a great tool to easily check if a series is convergent or divergent.

Let's check if $\sum_{n=1}^{\infty{}}\frac{n}{n^2+1}$ and $\sum_{n=0}^{\infty{}}\frac{1}{\left(2n+1\right)!}$ are divergent or absolutely convergent.

```python
from sympy import Sum, oo
from sympy.abc import n

Sum((-1)**n, (n, 1, oo)).is_absolutely_convergent() # returns false
Sum(1/factorial(2*n+1), (n, 1, oo)).is_absolutely_convergent() # returns true
```

<details>
<summary>Try it out</summary>

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@JackBeaumont/divergencetest?lite=true"></iframe>
</details>
