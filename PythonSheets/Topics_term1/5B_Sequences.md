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

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=c19zdW09MAoKZm9yIHIgaW4gcmFuZ2UoMSwyMCsxKToKICAgIHNfc3VtICs9IChyKzEpKiozCgpwcmludCgiVGhlIHN1bSBvZiBzZXJpZXMgaXMiLCBzX3N1bSkK&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
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

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@JackBeaumont/writingsequences?lite=true"></iframe>
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