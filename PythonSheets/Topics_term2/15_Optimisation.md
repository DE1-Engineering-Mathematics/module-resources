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

# Optimisation

The numpy module has some useful functions to calculate polynomial fits

## Least squares polynomial fit

This can be accomplished with the `numpy.polyfit(x, y, deg)` function where `x` and `y` are two arrays and `deg` is the degree of the polynomial.

Here is an example where we fit [1,6], [3,3], [5,9] and [7,5] to a polynomial of degree 1:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 5, 7])
y = np.array([ 6, 3, 9, 5 ])

m, b = np.polyfit(x, y, 1)

print(m)
print(b)

plt.plot(x, y, 'o') # plot data points
plt.plot(x, m*x + b) # plot line of best fit

plt.show()
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/a7935efb5e?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

</details>