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

# Root finding

In this section you will find 3 short code snippets to find roots with different methods. Try to understand how the code works and adapt it to solve your own problems.

## Secant method

This code will find the roots of $f(x)=x^2-3x+1=0$ with the secant method.

```python
def f(x):
    return x**2-3*x+1

def secant(x0,x1,e,N):
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = abs(f(x2)) > e
    print('Root is: ', x2)

x0 = -2 # Guess 1
x1 = 3 # Guess 2
e = 0.0001 # Precision
N = 1000 # Max number of trials

secant(x0,x1,e,N)
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/35fa51573f?outputOnly=true&runOption=run&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

</details>


## Newton-Raphson method

This code snippet will find the root of $f(x)=x^3-1$ with an initial guess of 1.5.

```python
from scipy import optimize

def f(x):
  return (x**3 - 1) 
  
root = optimize.newton(f, 1.5)
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/c75bba4d9d?outputOnly=true&runOption=run&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

</details>


## Bisection method

The following code will find the positive root of $f(x)=x^3-6x^2+11x-6=0$ using the bisection method from the interval [2.5, 4].

```python
def samesign(a, b):
    return a * b > 0

def bisect(func, low, high):
    assert not samesign(func(low), func(high))

    for i in range(54):
        midpoint = (low + high) / 2.0
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint

    return midpoint

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

x = bisect(f, 2.5, 4)
print(x, f(x))
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/2f05b6a541?outputOnly=true&runOption=run&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

</details>

