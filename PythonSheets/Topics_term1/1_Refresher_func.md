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

<iframe src="https://trinket.io/embed/python3/6e711fb447?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

</details>