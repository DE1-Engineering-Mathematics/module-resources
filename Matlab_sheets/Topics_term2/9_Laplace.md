# Laplace Transform

**IMPORTANT** Some of these functions require the [Symbolic Math Toolbox](https://uk.mathworks.com/products/symbolic.html) to work. Make sure it is installed before trying to use them.

- **laplace(f,var,transvar)** computes the laplace transform of a symbolic expression **f** with respect to a variable **var**. The transform is a symbolic expression in terms of **transvar**. [Full Documentation](https://uk.mathworks.com/help/symbolic/sym.laplace.html)
    ```matlab:Code
    syms t s
    f = exp(-5*t) + t*sin(2*t);
    laplace(f,t,s)
    ```
- **ilaplace(f,var,transvar)** computes the **inverse** laplace transform of a symbolic expression **f** with respect to the variable **var**. The inverse transform is a symbolic expression in terms of **transvar**. [Full Documentation](https://uk.mathworks.com/help/symbolic/sym.ilaplace.html)
    ```matlab:Code
    syms s t
    f = 1/(s + 5) + (4*s)/(s^2 + 4)^2;
    ilaplace(f,s,t)
    ```


###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco
