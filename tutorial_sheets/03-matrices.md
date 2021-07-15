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
<script type="text/javascript" src="tutorialSheetScripts.js"> </script>
<link rel="stylesheet" type="text/css" media="all" href="styles.css">

![vectors](03-matrices/cover.png)

# Matrices, Sheet #3

### Learning Targets
* Perform operations on matrices (add, subtract, multiply)
* Find the transpose, adjudicate, determinant of 2x2 and 3x3 matrices
* use matrices to find the solutions to linear equations
* Identify unit, symmetric, skew-symmetric, triangular, diagonal, singular and orthogonal matrices

### Additional Resources
* [3Blue1Brown - Linear Algebra Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
* [MathWorks - Matrices and Arrays](https://www.mathworks.com/help/matlab/learn_matlab/matrices-and-arrays.html)

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Given the matrices: $A=\begin{pmatrix}1&1 \newline 2&-1\end{pmatrix}$ and $B=\begin{pmatrix}0&1 \newline -2&3\end{pmatrix}$ <br>
Find the answers to the following operations:

(a) $A+B$
<div markdown="1"> 
Solving with the Matlab terminal:

```matlab:Code
a = [1 1 ; 2 -1]
b = [0 1 ; -2 3]

a + b
```

$\Rightarrow{}\quad \boxed{\begin{pmatrix}1&2\\0&2\end{pmatrix}}$
</div>
