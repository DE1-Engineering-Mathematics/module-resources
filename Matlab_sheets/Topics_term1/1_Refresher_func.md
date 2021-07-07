# Refresher and Functions
**IMPORTANT** Some of these functions require the [Symbolic Math Toolbox](https://uk.mathworks.com/products/symbolic.html) to work. Make sure it is installed before trying to use them.
## Refresher
- **partfrac(expr,var)** expresses expr as partial fractions, relative to var
- diff
- int and Integral

## Functions
### Plotting
- **plot(X, Y)** generates a 2D plot of X values against Y values. X and Y have to be equal-sized Row/Column matrices. [More](https://uk.mathworks.com/help/matlab/ref/plot.html)
```matlab:Code
X = [1, 2, 3, 4, 5];
Y = [1, 4, 9, 16, 25];
plot(X,Y)
```
Image
- **fplot(f(x),Range)** similar to plot() but instead it takes a symbolic function and a range as [xmin xmax] to plot the function through. If the Range argument is omited the range is [-5 to 5]. [More](https://uk.mathworks.com/help/matlab/ref/fplot.html) 
```matlab:Code
f = @(x) sin(x)^-3;
fplot(f)
```
Image
- **fsurf(f(x,y),xyinterval)** generates a 3D plot of a symbolic function of 2 variables, the second argument is a matrix that contains the following values [xmin xmax ymin ymax]. By default it's interval is [-5 to 5] for both x and y. [More](https://uk.mathworks.com/help/matlab/ref/fsurf.html)
```matlab:Code
f = @(x,y) cos(x)*y^3;
fsurf(f)
```
Image


### Finding coefficients
- **limit(f(x), x, value)** computes the limit of a function when the variable x of a **symbolic function** (which is different from the normal functions) tends to the **value**. [More](https://uk.mathworks.com/help/symbolic/limits.html) 
```matlab:Code
sym(x);
f = 3*x^-2 + 5;
limit(f,x,Inf)
```
- **solve(eqn1,eqn2,var1,var2)** solves a or a system of **symbolic equations**. The equations can be inputed in a matrix or separetly and so can the variables that you desire to solve for. [More](https://uk.mathworks.com/help/symbolic/solve.html)

```matlab:Code
syms x
eq1 = 4*x^2 + 8 == -4;
solve(eq1,x)
```

```matlab:Code
syms x y;
eq1 = x + y - 5 == 0;
eq2 = x^2 - y == 3;
[xsol ysol] = solve(eq1,eq2,x,y)  
```
