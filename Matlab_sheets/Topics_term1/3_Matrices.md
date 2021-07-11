# Matrices

- **det(A)** computes the determinant of a square matrix, sometimes when the matrix is singular the result of this function might not be 0 but some number of a very small magnitude e.g(3.5x10^-17) due to the finite numerical nature of matlab.
``` matlab:Code
A = [2 3 4; 1 2 5; 0 2 4];
det(A)
```

- **inv(A)** computes the inverse of a square matrix, unless it is a singular matrix of course. This function is prone to the same error as the det() function, make sure to always check and understand your answer!
```matlab:Code
inv(A)
```

- **adjoint(A)** computes the adjoint of a square matrix A.
```matlab:Code
adjoint(A)
```

- **issymmetric(A,)**

###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco