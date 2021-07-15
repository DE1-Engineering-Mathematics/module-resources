# Refresher and Functions

[<= Back to the Cheatsheet](../wolfram_cheatsheet.md)

**IMPORTANT** You will need to have a [WolframAlphs Pro account](https://www.imperial.ac.uk/admin-services/ict/self-service/computers-printing/devices-and-software/get-software/get-software-for-students/wolfram-alpha-pro/) to use Wolfram effectively.

## Basic Algebra
WolframAlpha is a really powerful tool for algebra. Most of the learning you do won't be through these sheets (because there is too much to teach), but through playing around with it and seeing what happens.

You really can ask it anything. For example, try asking ```How many calories in a cubic parsec of cheese```. You'll notice it even gives you a list of cheeses to choose from - and then it gives you a whole load of other information that you might find interesting.

That might not be very _useful_, but it does show the power of Wolfram. You can speak to it in English, and it will reply with maths. More topically, try asking Wolfram to [split a fraction into partial fractions](https://www.wolframalpha.com/input/?i=%285x-4%29%2F%28x%5E2-x-2%29+partial+fraction). It really is as simple as writing ```(your-fraction) partial fraction``` into the search bar.

If you want it to solve a quadratic, you don't even need to ask the question: just type any equation, e.g. ```x^2 + 17x + 12 = 3``` and it'll work out what you want. It will even graph the equation (useful for curve sketching).

<img href="Wolfram_sheets/wolfram_pics/quadratic.png">

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