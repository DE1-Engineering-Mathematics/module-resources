# Sequences

## Sequences Operations

- **limit(f(x), x, value)** computes the limit of a function when the variable x of a **symbolic function** (which is different from the normal functions) tends to the **value**. [Full Documentation](https://uk.mathworks.com/help/symbolic/limits.html) 
```matlab:Code
syms x;
f = 3*x^-2 + 5;
limit(f,x,Inf)
```
- **symsum(f,k,a,b)** computes the summation of function f with respect to variable k from the values of _k = a_ to _k = b_. [More documentation needed]()
```matlab:Code
syms k;
f = (k+3)^2;
symsum(f,k,1,8)
```
###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco