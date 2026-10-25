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

# Normal distribution

Python can also be used in normal distribution to plot bell curves and calculate probabilities.

## Plotting gaussian bell curves

We will be coding a solution to the following problem [(source)](https://pythonforundergradengineers.com/plotting-normal-curve-with-python.html):

At a facility that manufactures electrical resistors, a statistical sample of 1-kΩ resistors is pulled from the production line. The resistor's resistances are measured and recorded. A mean resistance of 979.8 kΩ and a standard deviation of 73.10 kΩ represents the sample of resistors. The desired resistance tolerance for the 1-kΩ resistors is ± 10%. This tolerance range means the acceptable range of resistance is 900 Ω to 1100 Ω.

Assuming a normal distribution, determine the probability that a resistor coming off the production line will be within spec (in the range of 900 Ω to 1100 Ω). Show the probability that a resistor picked off the production line is within spec on a plot.

1. Import modules

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
```

2. Define the constants

The mean is 979.8 and the standard deviation is 73.10. The lower bound is 900 and the upper bound is 1100.

```python
mu = 998.8 
sigma = 73.10
x1 = 900
x2 = 1100
```

3. Calculate upper and lower bounds

```python
z1 = ( x1 - mu ) / sigma
z2 = ( x2 - mu ) / sigma
```

4. Calculate probability

```python
x = np.arange(z1, z2, 0.001) # generate valyes of x in spec
x_all = np.arange(-10, 10, 0.001) # entire range of x, both in and out of spec

y = norm.pdf(x,0,1) # probability for x in spec
y2 = norm.pdf(x_all,0,1) # probability for all xs
```

5. Plot the result

```python
fig, ax = plt.subplots(figsize=(9,6))
ax.plot(x_all,y2)

ax.fill_between(x,y,0, alpha=0.3, color='b')
ax.fill_between(x_all,y2,0, alpha=0.1)
ax.set_xlim([-4,4])
ax.set_xlabel('# of Standard Deviations Outside the Mean')
ax.set_yticklabels([])
ax.set_title('Normal Gaussian Curve')

plt.show()
```

<details>
<summary>Try it out</summary>

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgbm9ybQoKbXUgPSA5OTguOCAKc2lnbWEgPSA3My4xMAp4MSA9IDkwMAp4MiA9IDExMDAKCnoxID0gKCB4MSAtIG11ICkgLyBzaWdtYQp6MiA9ICggeDIgLSBtdSApIC8gc2lnbWEKCnggPSBucC5hcmFuZ2UoejEsIHoyLCAwLjAwMSkgIyBnZW5lcmF0ZSB2YWx5ZXMgb2YgeCBpbiBzcGVjCnhfYWxsID0gbnAuYXJhbmdlKC0xMCwgMTAsIDAuMDAxKSAjIGVudGlyZSByYW5nZSBvZiB4LCBib3RoIGluIGFuZCBvdXQgb2Ygc3BlYwoKeSA9IG5vcm0ucGRmKHgsMCwxKSAjIHByb2JhYmlsaXR5IGZvciB4IGluIHNwZWMKeTIgPSBub3JtLnBkZih4X2FsbCwwLDEpICMgcHJvYmFiaWxpdHkgZm9yIGFsbCB4cwoKZmlnLCBheCA9IHBsdC5zdWJwbG90cyhmaWdzaXplPSg5LDYpKQpheC5wbG90KHhfYWxsLHkyKQoKYXguZmlsbF9iZXR3ZWVuKHgseSwwLCBhbHBoYT0wLjMsIGNvbG9yPSdiJykKYXguZmlsbF9iZXR3ZWVuKHhfYWxsLHkyLDAsIGFscGhhPTAuMSkKYXguc2V0X3hsaW0oWy00LDRdKQpheC5zZXRfeGxhYmVsKCcjIG9mIFN0YW5kYXJkIERldmlhdGlvbnMgT3V0c2lkZSB0aGUgTWVhbicpCmF4LnNldF95dGlja2xhYmVscyhbXSkKYXguc2V0X3RpdGxlKCdOb3JtYWwgR2F1c3NpYW4gQ3VydmUnKQoKcGx0LnNob3coKQo&credit=0" width="100%" height="560" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
```

</details>