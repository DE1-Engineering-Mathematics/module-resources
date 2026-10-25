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

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKCnggPSBucC5hcnJheShbMSwgMywgNSwgN10pCnkgPSBucC5hcnJheShbIDYsIDMsIDksIDUgXSkKCm0sIGIgPSBucC5wb2x5Zml0KHgsIHksIDEpCgpwcmludChtKQpwcmludChiKQoKcGx0LnBsb3QoeCwgeSwgJ28nKSAjIHBsb3QgZGF0YSBwb2ludHMKcGx0LnBsb3QoeCwgbSp4ICsgYikgIyBwbG90IGxpbmUgb2YgYmVzdCBmaXQKCnBsdC5zaG93KCkK&credit=0" width="100%" height="560" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
```

</details>