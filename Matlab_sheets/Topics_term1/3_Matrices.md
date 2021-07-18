# Matrices
**IMPORTANT** Some of these functions require the [Symbolic Math Toolbox](https://uk.mathworks.com/products/symbolic.html) to work. Make sure it is installed before trying to use them.

## Matrix Operations
- **det(A)** computes the determinant of a square matrix, sometimes when the matrix is singular the result of this function might not be 0 but some number of a very small magnitude e.g(3.5x10^-17) due to the finite numerical nature of matlab. [Full Documentation](https://uk.mathworks.com/help/matlab/ref/det.html)
    ``` matlab:Code
    A = [2 3 4; 1 2 5; 0 2 4];
    det(A)
    ```

- **inv(A)** computes the inverse of a square matrix, unless it is a singular matrix of course. This function is prone to the same error as the det() function, make sure to always check and understand your answer! [Full Documentation](https://uk.mathworks.com/help/matlab/ref/inv.html)
    ```matlab:Code
    inv(A)
    ```

- **adjoint(A)** computes the adjoint of a square matrix A. [Full Documentation](https://uk.mathworks.com/help/symbolic/adjoint.html)
    ```matlab:Code
    adjoint(A)
    ```

- **issymmetric(A,type)** is a boolean function that will **1** or **0** if the matrix A meets the type of symmetry. By default the type is **non-skew** but it can be specified as **skew**. [Full Documentation](https://uk.mathworks.com/help/matlab/ref/issymmetric.html)
    ```matlab:Code
    A = [0 -1; 1 0];
    issymmetric(A,"skew")
    ```

###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco 
