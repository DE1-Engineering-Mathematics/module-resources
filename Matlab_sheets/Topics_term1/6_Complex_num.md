# Complex Numbers

## Complex number creation
The creation of complex numbers in matlab is straight forward. The letter **i** is used as expected and no multiplication operator is required between i and the coefficient.
```matlab:Code
z = 4 - 3i
```
## Complex number basic operations
The operations are the same as with other number types:
- Addition "+"
- Substraction "-"
- Multiplication "*"
- Division "/"
- Power "^"

In order to obtain the **complex conjugate** there are two different ways: using the **conj()** function or using the " ' " operator.
```matlab:Code
conjz = conj(z)
conjz2 = z'
```

To obtain the **magnitude** of a complex number use the **norm()** function.
```matlab:Code
norm(z)
```

To obtain the argument of a complex number use the **angle()** function.
```matlab:Code
angle(z)
```

The real and imaginary parts of a complex number can be obtained separately using the **real()** and **imag()** functions.
```matlab:Code
real(z)
imag(z)
```
## Plotting

- **plot(X, Y)** generates a 2D plot of X values against Y values. X and Y have to be equal-sized Row/Column matrices. [Full Documentation](https://uk.mathworks.com/help/matlab/ref/plot.html)
```matlab:Code
plot(z,"r*")
```
Image