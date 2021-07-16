# Eigenproblems

## Eigen Operations

- **det(A)** computes the determinant of a square matrix, sometimes when the matrix is singular the result of this function might not be 0 but some number of a very small magnitude e.g(3.5x10^-17) due to the finite numerical nature of matlab. [Full Documentation](https://uk.mathworks.com/help/matlab/ref/det.html)
    ``` matlab:Code
    A = [2 3 4; 1 2 5; 0 2 4];
    det(A)
    ```

- **eig(A)** is able to compute the eigenvalues and eigenvectors of _n x n_ matrix. The function outputs two separate matrices, the first one contains a matrix with the eigenvectors in the following format: (for a 2x2) [x1 x2; y1 y2] and the second matrix contains the eigenvalues [lambda1 0; 0 lambda 2]. [Full Documentation](https://uk.mathworks.com/help/matlab/ref/eig.html)

    ```matlab:Code
    A = [1 0; 0 -3]
    [v d] = eig(A)
    ```


## Plotting
**IMPORTANT** plotv requires the [Deep learning toolbox](https://uk.mathworks.com/products/deep-learning.html) to work. Make sure it is installed before trying to use it.
- **plotv(M)** generates 2 Dimensional plot of vectors from the origin, the input argument M is a matrix that contains the x components of the vectors in the first row and the second row contains the y components of the vectors: M = [x1 x2; y1 y2]. [Full Documentation](https://uk.mathworks.com/help/deeplearning/ref/plotv.html)
    ```matlab:Code
    M = [2 3 5; 1 2 3];
    plotv(M)
    ``` 

<p align="center">
<img src = "images/plotv.png" width="50%" >
</p>


###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco