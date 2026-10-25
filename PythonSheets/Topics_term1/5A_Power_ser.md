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

# Power series

## Taylor series expansion

The amazing sympy module has the ability to expand a function into a taylor series.

This is done by calling the `series(x, n)` function on a mathematical function. Here x represents a mathematical symbol and this is declared with `x = Symbol('x')`, whilst `n` is point to expand around.

Here is a code snippet of the expansion of sin(x) around 2:

```python
from sympy import *
x = Symbol('x')
sin(x).series(x, 2)
```

<details>
<summary>Try it out</summary>

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@JackBeaumont/powerseriesexpansion?lite=true"></iframe></iframe>
</details>

## Plotting maclaurian series

Scipy has some brilliant features when it comes to estimating maclaurian series of functions.

Here is a code snippet of how to do this:

```python

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

# create array of x coordinates
x = np.linspace(-10.0, 10.0, num=100)

# function to plot
def func(x):
  return np.sin(x)

# plot the function
plt.plot(x, np.sin(x), label="sin curve")

# calculate maclaurian to 5th degree
for degree in np.arange(1, 5, step=1): # for each degree
  sin_taylor = approximate_taylor_polynomial(np.sin, 0, degree, 1,
                                                order=degree + 1) # calculate taylor at x=0 with specified degree
  plt.plot(x, sin_taylor(x), label=f"degree={degree}") # plot the curve
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
            borderaxespad=0.0, shadow=True)
plt.tight_layout()
plt.axis([-5, 5, -5, 5]) # set axis
plt.show()

```

<details>
<summary>Try it out</summary>

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKZnJvbSBzY2lweS5pbnRlcnBvbGF0ZSBpbXBvcnQgYXBwcm94aW1hdGVfdGF5bG9yX3BvbHlub21pYWwKCiMgY3JlYXRlIGFycmF5IG9mIHggY29vcmRpbmF0ZXMKeCA9IG5wLmxpbnNwYWNlKC0xMC4wLCAxMC4wLCBudW09MTAwKQoKIyBmdW5jdGlvbiB0byBwbG90CmRlZiBmdW5jKHgpOgogIHJldHVybiBucC5zaW4oeCkKCiMgcGxvdCB0aGUgZnVuY3Rpb24KcGx0LnBsb3QoeCwgbnAuc2luKHgpLCBsYWJlbD0ic2luIGN1cnZlIikKCiMgY2FsY3VsYXRlIG1hY2xhdXJpYW4gdG8gNXRoIGRlZ3JlZQpmb3IgZGVncmVlIGluIG5wLmFyYW5nZSgxLCA1LCBzdGVwPTEpOiAjIGZvciBlYWNoIGRlZ3JlZQogIHNpbl90YXlsb3IgPSBhcHByb3hpbWF0ZV90YXlsb3JfcG9seW5vbWlhbChucC5zaW4sIDAsIGRlZ3JlZSwgMSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb3JkZXI9ZGVncmVlICsgMSkgIyBjYWxjdWxhdGUgdGF5bG9yIGF0IHg9MCB3aXRoIHNwZWNpZmllZCBkZWdyZWUKICBwbHQucGxvdCh4LCBzaW5fdGF5bG9yKHgpLCBsYWJlbD1mImRlZ3JlZT17ZGVncmVlfSIpICMgcGxvdCB0aGUgY3VydmUKcGx0LmxlZ2VuZChiYm94X3RvX2FuY2hvcj0oMS4wNSwgMSksIGxvYz0ndXBwZXIgbGVmdCcsCiAgICAgICAgICAgIGJvcmRlcmF4ZXNwYWQ9MC4wLCBzaGFkb3c9VHJ1ZSkKcGx0LnRpZ2h0X2xheW91dCgpCnBsdC5heGlzKFstNSwgNSwgLTUsIDVdKSAjIHNldCBheGlzCnBsdC5zaG93KCkK&credit=0" width="100%" height="560" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
```

</details>
