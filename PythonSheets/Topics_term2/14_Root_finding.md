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

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=ZGVmIGYoeCk6CiAgICByZXR1cm4geCoqMi0zKngrMQoKZGVmIHNlY2FudCh4MCx4MSxlLE4pOgogICAgc3RlcCA9IDEKICAgIGNvbmRpdGlvbiA9IFRydWUKICAgIHdoaWxlIGNvbmRpdGlvbjoKICAgICAgICBpZiBmKHgwKSA9PSBmKHgxKToKICAgICAgICAgICAgcHJpbnQoJ0RpdmlkZSBieSB6ZXJvIGVycm9yIScpCiAgICAgICAgICAgIGJyZWFrCiAgICAgICAgCiAgICAgICAgeDIgPSB4MCAtICh4MS14MCkqZih4MCkvKCBmKHgxKSAtIGYoeDApICkgCiAgICAgICAgeDAgPSB4MQogICAgICAgIHgxID0geDIKICAgICAgICBzdGVwID0gc3RlcCArIDEKICAgICAgICAKICAgICAgICBpZiBzdGVwID4gTjoKICAgICAgICAgICAgcHJpbnQoJ05vdCBDb252ZXJnZW50IScpCiAgICAgICAgICAgIGJyZWFrCiAgICAgICAgCiAgICAgICAgY29uZGl0aW9uID0gYWJzKGYoeDIpKSA-IGUKICAgIHByaW50KCdSb290IGlzOiAnLCB4MikKCngwID0gLTIgIyBHdWVzcyAxCngxID0gMyAjIEd1ZXNzIDIKZSA9IDAuMDAwMSAjIFByZWNpc2lvbgpOID0gMTAwMCAjIE1heCBudW1iZXIgb2YgdHJpYWxzCgpzZWNhbnQoeDAseDEsZSxOKQo&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>

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

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=ZnJvbSBzY2lweSBpbXBvcnQgb3B0aW1pemUKCmRlZiBmKHgpOgogIHJldHVybiAoeCoqMyAtIDEpIAogIApyb290ID0gb3B0aW1pemUubmV3dG9uKGYsIDEuNSkKcHJpbnQocm9vdCkK&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>

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

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=ZGVmIHNhbWVzaWduKGEsIGIpOgogICAgcmV0dXJuIGEgKiBiID4gMAoKZGVmIGJpc2VjdChmdW5jLCBsb3csIGhpZ2gpOgogICAgYXNzZXJ0IG5vdCBzYW1lc2lnbihmdW5jKGxvdyksIGZ1bmMoaGlnaCkpCgogICAgZm9yIGkgaW4gcmFuZ2UoNTQpOgogICAgICAgIG1pZHBvaW50ID0gKGxvdyArIGhpZ2gpIC8gMi4wCiAgICAgICAgaWYgc2FtZXNpZ24oZnVuYyhsb3cpLCBmdW5jKG1pZHBvaW50KSk6CiAgICAgICAgICAgIGxvdyA9IG1pZHBvaW50CiAgICAgICAgZWxzZToKICAgICAgICAgICAgaGlnaCA9IG1pZHBvaW50CgogICAgcmV0dXJuIG1pZHBvaW50CgpkZWYgZih4KToKICAgIHJldHVybiB4KiozIC0gNip4KioyICsgMTEqeCAtIDYKCnggPSBiaXNlY3QoZiwgMi41LCA0KQpwcmludCh4LCBmKHgpKQo&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>

</details>

