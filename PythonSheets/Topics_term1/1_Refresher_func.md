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

# Refresher and Functions

## Python operators

The following operators can be used to perform basic mathematical calculations in Python

| Name           | Operator |
|----------------|----------|
| Addition       | +        |
| Subtraction    | -        |
| Multiplication | *        |
| Division       | /        |
| Modulus        | &        |
| Exponentiation | **       |

## Essential mathematical functions

Here is a list of the most useful functions available in Python for maths.

To use these make sure you imported the Numpy module:

```python
import numpy as np
```

### Trigonometric functions

- `np.sin(x)` calculates the sin of x (in radians)
- `np.cos(x)` calculates the cosine of x (in radians)
- `np.tan(x)` calculates the tangent of x (in radians)
- `np.arcsin(x)` calculates the inverse sin of x (in radians)
- `np.arccos(x)` calculates the inverse cosine of x (in radians)
- `np.arctan(x)` calculates the inverse tangent of x (in radians)
- `np.degrees(x)` angles from radians to degrees
- `np.radians(x)` angles from degrees to radians

### Hyperbolic functions

- `np.sinh(x)` calculates the hyperbolic sin of x (in radians)
- `np.cosh(x)` calculates the hyperbolic cosine of x (in radians)
- `np.tanh(x)` calculates the hyperbolic tangent of x (in radians)
- `np.arcsinh(x)` calculates the inverse hyperbolic sin of x (in radians)
- `np.arccosh(x)` calculates the inverse hyperbolic cosine of x (in radians)
- `np.arctanh(x)` calculates the inverse hyperbolic tangent of x (in radians)

### Exponents and logarithms

- `np.exp(x)` calculate the exponential of all elements in the input x
- `np.sqrt(x)` calculate square root of x
- `np.log(x)` calculate the natural logarithm of x
- `np.log10(x)` calculate the base 10 logarithm of x

## Drawing functions

You can easily draw functions using the matplotlib module.

So make sure you import the module:

```python
import matplotlib.pyplot as plt  
```

Here are some essential functions needed to plot a graph:

- `plt.title(x)` input string to be graph title
- `plt.plot(x, y)` plot x and y coordinates, inputs must be arrays
- `plt.show()` show the graph

For example, to plot the function sin(x)^2 with x between -4 and 4, you could write the following code:

```matlab:Code
import numpy as np 
import matplotlib.pyplot as plt  

# Compute the x and y coordinates for points on curve 
x = np.arange(-4, 4, 0.1) # Generate array of numbers between -4 and 4 with step size of 0.1 for x coordinates
y = np.sin(x)**2
plt.title("sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y) 
plt.show() 
```

<details>
<summary>Try it out</summary>

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wIAppbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0ICAKCiMgQ29tcHV0ZSB0aGUgeCBhbmQgeSBjb29yZGluYXRlcyBmb3IgcG9pbnRzIG9uIGN1cnZlIAp4ID0gbnAuYXJhbmdlKC00LCA0LCAwLjEpICMgR2VuZXJhdGUgYXJyYXkgb2YgbnVtYmVycyBiZXR3ZWVuIC00IGFuZCA0IHdpdGggc3RlcCBzaXplIG9mIDAuMSBmb3IgeCBjb29yZGluYXRlcwp5ID0gbnAuc2luKHgpKioyCnBsdC50aXRsZSgic2luZSB3YXZlIGZvcm0iKSAKCiMgUGxvdCB0aGUgcG9pbnRzIHVzaW5nIG1hdHBsb3RsaWIgCnBsdC5wbG90KHgsIHkpIApwbHQuc2hvdygpCg&credit=0" width="100%" height="560" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>

</details>