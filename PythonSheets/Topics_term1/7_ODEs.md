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

# ODEs

Python comes to great use when solving ODEs.

## Solving ODEs

ODEs can be solved using the amazing sympy module and the `dsolve` function.

Here is how this can be done, step by step to solve the ODE $\frac{d^2y}{ {dx}^2}-3\frac{dy}{dx}+2y=0$:

1. Import sympy

  ```python
  from sympy import *
  ```

2. Create symbols

  We need to tell sympy that the letter `x` represents a symbol whilst `y` will be used to define the function.

  ```python
  x = Symbol('x')
  y = Function('y')
  ```

3. Calculate derivatives

  In sympy we can use the `Derivative(y(x), x, i)` function to calculate the ith derivative of the function `y(x)` with respect to `x`.

  ```python
  y_ = Derivative(y(x), x)
  y__ = Derivative(y(x), x, 2)
  ```

4. Solve the ODEs

  We can now solve the ODE using `dsolve(eq, func)` which will solve the equation `eq` for the function `func`.

  ```python3
  sol = dsolve(y__ - 3*y_ + 2*y(x), y(x))
  ```

5. Show the result

  You can show a pretty formatted result using this command

  ```python
  pprint(sol)
  ```

## Solving ODEs with initial conditions

We can also solve apply initial conditions to the `dsolve` function using the `ics` parameter.

For instance, to solve the ODE $3y”(x)+3y’(x)+4y(x)=0$ where $y(0)=3$ and $y’(0)=0$, we would apply the following `ics`: `{y(0): 3, y(x).diff(x).subs(x, 0): 0}`.

- `y(0): 3` defines the y(0)=3 condition

- `y(x).diff(x).subs(x, 0): 0}` defines the `y’(0)=0` condition. We first calculate the derivative of y(x) using `diff(x)`, then we substitute `x` for the actual value which is `0`.

Here is the full code:

```python
from sympy import *

x = Symbol('x')
y = Function('y')

y_ = Derivative(y(x), x)
y__ = Derivative(y(x), x, 2)

sol = dsolve(3*y__ + 3*y_ + 4*y(x), y(x), ics={y(0): 3, y(x).diff(x).subs(x, 0): 0})

pprint(sol) # pprint formats the solution in a more readable format
```
