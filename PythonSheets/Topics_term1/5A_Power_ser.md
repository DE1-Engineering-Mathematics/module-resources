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

### Taylor series expansion

The amazing sympy module has the ability to expand a function into a taylor series.

This is done by calling the `series(x, n)` function on a mathematical function. Here x represents a mathematical symbol and this is declared with `x = Symbol('x')`, whilst `n` is point to expand around.

Here is a code snippet of the expansion of sin(x) around 2:

```python
from sympy import *
x = Symbol('x')
sin(x).series(x, 2)
```

### Plotting maclaurian series

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

<iframe src="https://trinket.io/embed/python3/d4e1a637d3?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

</details>
