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

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Given the matrices: $A=\begin{pmatrix}1&1 \newline 2&-1\end{pmatrix}$ and $B=\begin{pmatrix}0&1 \newline -2&3\end{pmatrix}$ <br>
Find the answers to the following operations:

(a) $A+B$
<div class = "answer"> $\Rightarrow{}\quad \boxed{\begin{pmatrix}1&2\\0&2\end{pmatrix}}$ </div>

(b) $A-B$
<div class = "answer">$\Rightarrow{}\quad \boxed{\begin{pmatrix}1&0\\4&-4\end{pmatrix}}$</div>

(c) $AB$
<div class = "answer">$\Rightarrow{}\quad \boxed{ \begin{pmatrix}-2&4\\2&-1\end{pmatrix}}$</div>

(d) $BA$
<div class = "answer">$\Rightarrow{}\quad \boxed{\begin{pmatrix}2&-1\\4&-5\end{pmatrix}}$</div>

(e) $4A+\frac{1}{2}B$
<div class = "answer">$\Rightarrow{}\quad 4\begin{pmatrix}1&1\\2&-1\end{pmatrix}+\frac{1}{2}\begin{pmatrix}0&1\\-2&3\end{pmatrix}$ <br>
$\Rightarrow{}\ \
\begin{pmatrix}4(1)+\frac{1}{2}(0)&4(1)+\frac{1}{2}(0)\\4(2)+\frac{1}{2}(-2)&4(-1)+\frac{1}{2}(3)\end{pmatrix}$ <br>
$\Rightarrow{} \quad \boxed{\begin{pmatrix}4&9/2\\7&-5/2\end{pmatrix}}$</div>

(f) $AB^T$
<div class = "answer">$\Rightarrow{}\quad$
$\begin{pmatrix}1&1\\2&-1\end{pmatrix}\begin{pmatrix}0&1\\-2&3\end{pmatrix}^T$ <br>
$\Rightarrow{} \quad \begin{pmatrix}1&1\\2&-1\end{pmatrix}\begin{pmatrix}0&-2\\1&3\end{pmatrix}$ <br>
$\Rightarrow{} \quad \begin{pmatrix}1(0)+1(1)&1(-2)+1(3)\\2(0)+-1(1)&2(-2)+-1(3)\end{pmatrix}$ <br>
$\Rightarrow{} \quad \boxed{\begin{pmatrix}1&1\\-1&-7\end{pmatrix}}$</div>

(g) $BA^T$
<div class = "answer">$\Rightarrow{}\quad$
$\begin{pmatrix}0&1\\-2&3\end{pmatrix}\begin{pmatrix}1&1\\2&-1\end{pmatrix}^T$ <br>
$\Rightarrow{} \quad \begin{pmatrix}0&1\\-2&3\end{pmatrix}\begin{pmatrix}1&2\\1&-1\end{pmatrix}$ <br>
$\Rightarrow{} \quad \begin{pmatrix}0(1)+1(1)&0(2)+1(-1)\\-2(1)+3(1)&-2(2)+3(-1)\end{pmatrix}$ <br>
$\Rightarrow{} \quad \boxed{\begin{pmatrix}1&-1\\1&-7\end{pmatrix}}$</div>

(h) $B^TA^T$
<div class = "answer">$\Rightarrow{}\quad$
$\begin{pmatrix}0&1\\-2&3\end{pmatrix}^T\begin{pmatrix}1&1\\2&-1\end{pmatrix}^T$ <br>
$\Rightarrow{} \quad \begin{pmatrix}0&-2\\1&3\end{pmatrix}\begin{pmatrix}1&2\\1&-1\end{pmatrix}$ <br>
$\Rightarrow{} \quad \begin{pmatrix}0(1)+-2(1)&0(2)+-2(-1)\\1(1)+3(1)&1(2)+3(-1)\end{pmatrix}$ <br>
$\Rightarrow{} \quad \boxed{\begin{pmatrix}-2&2\\4&-1\end{pmatrix}}$</div>

(i) $det A$
<div class = "answer">$\Rightarrow{}\quad \begin{vmatrix}1&1\\2&-1\end{vmatrix}$
$\quad\Rightarrow{}\quad 1(-1)-2(1) \ \ \Rightarrow{}\ \boxed{ -3}$</div>

(j) $A^{-1}$
<div class = "answer">$\Rightarrow{}\quad$
$\frac{1}{det A}\begin{pmatrix}-1&-1\\-2&1\end{pmatrix}$
$\quad \Rightarrow{}\quad -\frac{1}{-3}\begin{pmatrix}-1&-1\\-2&1\end{pmatrix}$
$\Rightarrow{}\quad \boxed{\begin{pmatrix}\frac{1}{3}&\frac{1}{3}\\\frac{2}{3}&-\frac{1}{3}\end{pmatrix}}$</div>

(k)  Comment on any relationships between the results of question (a) to (j)
<div class = "answer">$\Rightarrow{} BA^T=(AB^T)^T$ and $(AB)^T=B^TA^T$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 2
Given the matrices:

$A=\begin{pmatrix}2&0 \newline 3&-1 \newline 1&4\end{pmatrix}$, 
$B=\begin{pmatrix}-1&-3 \newline 5&2 \newline 7&1\end{pmatrix}$ and 
$C=\begin{pmatrix}1&3&5&7 \newline 2&4&6&8\end{pmatrix}$

Find the answers to the following operations, if they exist:

(a) $A+B$
<div class = "answer">$\Rightarrow{}\quad
\boxed{\begin{pmatrix}1&-3\\8&1\\8&5\end{pmatrix}}$</div>

(b) $A-B$
<div class = "answer">$\Rightarrow{}\quad
\boxed{\begin{pmatrix}3&3\\-2&-3\\-6&3\end{pmatrix}}$</div>

(c) $AC$
<div class = "answer">$\Rightarrow{} \ \ $
$\begin{pmatrix}2&0\\3&-1\\1&4\end{pmatrix}\begin{pmatrix}1&3&5&7\\2&4&6&8\end{pmatrix}$ <br>
$\Rightarrow{}\ \ \begin{pmatrix}2(1)+0(2)&2(3)+0(4)&2(5)+0(6)&2(7)+0(8)\\3(1)+-1(2)&3(3)+-1(4)&3(5)+-1(6)&3(7)+-1(8)\\1(1)+4(2)&1(3)+4(4)&1(5)+4(6)&1(7)+4(8)\end{pmatrix}$ <br>
$\Rightarrow{}\ \ \boxed{\begin{pmatrix}2&6&10&14\\1&5&9&13\\9&19&29&39\end{pmatrix}}$</div>

(d) $A+C$
<div class = "answer">Operation is not possible. Two matrices must have an equal number of rows and columns to be added.</div>

(e) $CA$
<div class = "answer">Operation not possible, $C_{2x4}A_{3x2}$</div>

(f) $A^TB$
<div class = "answer">$\Rightarrow{}\ \ \begin{pmatrix}2&0\\3&-1\\1&4\end{pmatrix}^T\begin{pmatrix}-1&-3\\5&2\\7&1\end{pmatrix}\Rightarrow{}\begin{pmatrix}2&3&1\\0&-1&4\\\end{pmatrix}\begin{pmatrix}-1&-3\\5&2\\7&1\end{pmatrix}\\$
$\Rightarrow{}\ \ \begin{pmatrix}2(-1)+3(5)+1(7)&2(-3)+3(2)+1(1)\\0(-1)-1(5)+4(7)&0(-3)-1(2)+4(1)\end{pmatrix}$
$\Rightarrow{}\ \ \boxed{\begin{pmatrix}20&1\\23&2\end{pmatrix}}$</div>

(g) $AB^T$
<div class = "answer">$\Rightarrow{}\ \ \begin{pmatrix}2&0\\3&-1\\1&4\end{pmatrix} \begin{pmatrix}-1&-3\\5&2\\7&1\end{pmatrix}^T\ \Rightarrow{}\begin{pmatrix}2&0\\3&-1\\1&4\end{pmatrix} \begin{pmatrix}-1&5&7\\-3&2&1\end{pmatrix}$ <br>
$\Rightarrow{} \begin{pmatrix}2(-1)+0(-3)&2(5)+0(2)&2(7)+0(1)\\3(-1)-1(-3)&3(5)-1(2)&3(7)-1(1)\\1(-1)+4(-3)&1(5)+4(2)&1(7)+4(1)\end{pmatrix}\ \ \ \ \Rightarrow{}\ \ \boxed{\begin{pmatrix}-2&10&14\\0&13&20\\-13&13&11\end{pmatrix}}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 3.
(a) Find the solution to the following linear equations: 

$$\begin{align} 3x + 2y + z &= 10  \newline 
3x + 5z &= 6  \newline 
2x + 4y - 4z &= 2 \end{align}$$

<div class = "answer">$\Rightarrow{} \begin{pmatrix}3 & 2 & 1\\3 & 0 & 5\\2&4&-4\end{pmatrix} \begin{pmatrix}x\\y\\z\end{pmatrix} = 
\begin{pmatrix}10\\6\\2\end{pmatrix}$ <br>
$\Rightarrow\begin{pmatrix}x\\y\\z\end{pmatrix} = 
\begin{pmatrix}3&2&1\\3&0&5\\2&4&-4\end{pmatrix}^{-1} \ 
\begin{pmatrix}10\\6\\2\end{pmatrix}$ <br>
$\Rightarrow\begin{pmatrix}x\\y\\z\end{pmatrix} = 
\begin{pmatrix}5&-3&-2.5\\-5.5&3.5&3\\-3&2&1.5\end{pmatrix} \ 
\begin{pmatrix}10\\6\\2\end{pmatrix}$ <br>
$\Rightarrow{} \quad\boxed{ x = 27 \\ y = -28 \\ z = -15}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 4.
Evaluate the following determinants:

(a) $\begin{vmatrix}20&6 \newline 1&2\end{vmatrix}$
<div class = "answer">$\Rightarrow{}$
$20(2)-6(1) \ \Rightarrow{}\ \boxed{34}$</div>

(b) $\begin{vmatrix}1&2&6 \newline 1&3&9 \newline 1&4&12\end{vmatrix}$
<div class = "answer">$\Rightarrow{}\ \ 1\begin{vmatrix}3&9\\4&12\end{vmatrix}-2\begin{vmatrix}1&9\\1&12\end{vmatrix}+6\begin{vmatrix}1&3\\1&4\end{vmatrix}$ <br>
$\Rightarrow{}\ \ 1[3(13)-9(4)]-2[1(12)-9(1)]+6[1(4)-3(1)] \ \ \Rightarrow{}\ \ \boxed{0}$</div>

(c) $\begin{vmatrix}1&1&1 \newline  \lambda & \mu & \nu \newline  \lambda^3 & \mu^3 & \nu^3\end{vmatrix}$
<div class = "answer">
$\Rightarrow{}\ \ 1\begin{vmatrix}\mu & \nu \\ \mu^3 & \nu^3 \end{vmatrix}-1\begin{vmatrix}\lambda & \nu \\ \lambda^3 & \nu^3 \end{vmatrix}+1\begin{vmatrix}\lambda & \mu \\ \lambda^3 & \mu^3 \end{vmatrix}$ <br>
$\Rightarrow{}\ \ (\mu\nu^3-\nu\mu^3) - (\lambda\nu^3-\nu\lambda^3) + (\lambda\mu^3-\mu\lambda^3)$
$\Rightarrow{}\ \ \boxed{\nu^3(\mu-\lambda)+\mu^3(\lambda-\nu)+\lambda^3(\nu-\mu)}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 5.
Determine the elements of the matrix $M$, so that $AMB=C$, where

$A=\begin{pmatrix}2&1&1 \newline 1&1&0 \newline 0&0&1\end{pmatrix}$, $B=\begin{pmatrix}3&1 \newline 1&1\end{pmatrix}$ and $C=\begin{pmatrix}1&1 \newline 2&2 \newline 1&1\end{pmatrix}$
<div class = "answer">
$\Rightarrow{}\quad M=A^{-1}CB^{-1}$ <br>
$\Rightarrow{}\quad det(a)=1$ and $det(b)=2$ <br>
$\Rightarrow{}\quad B^{-1}=\frac{1}{det(c)}adj(d) \quad\Rightarrow{}\quad B^{-1}=\frac{1}{2}\begin{pmatrix}1&-1\\-1&3\end{pmatrix} \quad\Rightarrow{}\quad B^{-1}=\begin{pmatrix}1/2&-1/2\\-1/2&3/2\end{pmatrix}$
$\Rightarrow{}\quad A^{-1}=\frac{1}{det(e)}adj(f)=\frac{1}{det(g)}C_A^T$, where $C_A$ is the cofactor matrix of A <br><br>
$\Rightarrow{}\quad C_A=\begin{pmatrix}
\begin{vmatrix}1&0\\0&1\end{vmatrix} & -\begin{vmatrix}1&0\\0&1\end{vmatrix} & \begin{vmatrix}1&1\\0&0\end{vmatrix} \\ 
-\begin{vmatrix}1&1\\0&1\end{vmatrix} & \begin{vmatrix}2&1\\0&1\end{vmatrix} & -\begin{vmatrix}2&1 \\0&0\end{vmatrix} \\
\begin{vmatrix}1&1\\1&0\end{vmatrix} & -\begin{vmatrix}2&1\\1&0\end{vmatrix} & \begin{vmatrix}2&1\\1&1\end{vmatrix}
\end{pmatrix}$ <br><br>
$\Rightarrow{}\quad C_A=\begin{pmatrix}1&-1&0\\-1&2&0\\-1&1&1\end{pmatrix}$ <br><br>
$\Rightarrow{}\quad C_A^T=\begin{pmatrix}1&-1&-1\\-1&2&1\\0&0&1\end{pmatrix}$
$\Rightarrow{}\quad A^{-1}=\begin{pmatrix}1&-1&-1\\-1&2&1\\0&0&1\end{pmatrix}$ <br><br>
$\Rightarrow{} \quad M=\begin{pmatrix}1&-1&-1\\-1&2&1\\0&0&1\end{pmatrix} \begin{pmatrix}1&1\\2&2\\1&1\end{pmatrix}\begin{pmatrix}1/2&-1/2\\-1/2&3/2\end{pmatrix} \quad\Rightarrow{} \quad \boxed{M=\begin{pmatrix}0&-2\\0&4\\0&1\end{pmatrix}}$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 6.
(a) Given $A=\begin{pmatrix}1&2&3 \newline 1&3&5 \newline 1&5&12\end{pmatrix}$ find $\|A\|$, the adjoint of $A$ and $A^{-1}$. Verify that $AA^{-1}=I$, where $I$ is the corresponding unit matrix.
<div class = "answer">$\Rightarrow{}\quad det(A) = 1\begin{vmatrix}3&5\\5&12\end{vmatrix} - 2\begin{vmatrix}1&5\\1&12\end{vmatrix} + 3\begin{vmatrix}1&3\\1&5\end{vmatrix} \quad\Rightarrow{}\quad \boxed{det(A)=3}$ <br>
$\Rightarrow{}\quad adj(A) = C^T$, where C is the cofactor matrix of A. <br>
$\Rightarrow{}\quad C=\begin{pmatrix}
\begin{vmatrix}3&5\\5&12\end{vmatrix} & -\begin{vmatrix}1&5\\1&12\end{vmatrix} & \begin{vmatrix}1&3\\1&5\end{vmatrix}\\ 
-\begin{vmatrix}2&3\\5&12\end{vmatrix} & \begin{vmatrix}1&3\\1&12\end{vmatrix} & -\begin{vmatrix}1&2\\1&5\end{vmatrix}\\ 
\begin{vmatrix}2&3\\3&5\end{vmatrix} & -\begin{vmatrix}1&3\\1&5\end{vmatrix} & \begin{vmatrix}1&2\\1&3\end{vmatrix}
\end{pmatrix} \quad\Rightarrow{}\quad C=\begin{pmatrix}11&-7&2\\-9&9&-3\\1&-2&1\end{pmatrix}$ <br>
$\Rightarrow{}\quad \boxed{ adj(A) = C^T = \begin{pmatrix}11&-9&1\\-7&9&-2\\2&-3&1\end{pmatrix}}$ <br>
$\Rightarrow{}\quad A^{-1} = \frac{1}{det(A)}adj(A) = \frac{1}{3} \begin{pmatrix}11&-9&1\\-7&9&-2\\2&-3&1\end{pmatrix}$ <br>
$\Rightarrow{}\quad \boxed{AA^{-1} = \begin{pmatrix}1&2&3\\1&3&5\\1&5&12\end{pmatrix} \begin{pmatrix}11/3 & -9/3 & 1/3 \\-7/3 & 9/3 & -2/3\\ 2/3 & -3/3 & 1/3 \end{pmatrix} = \begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}}$ <br></div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 7.
Solve the following sets of equations, if possible, using matrix methods. Otherwise, determine any relationships between the unknowns.

(a) $\begin{align}
x + y + z &=  7  \newline 
2x -y + 2z &=  8  \newline 
3x + 2y -z &=  11 \end{align}$
<div class = "answer">
$\Rightarrow{}\quad Ax = b \quad\Rightarrow{}\quad \begin{pmatrix}1&1&1\\2&-1&2\\3&2&-1\end{pmatrix} \begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}7\\8\\11\end{pmatrix}$ <br>
$\Rightarrow{}\quad A^{-1}Ax = A^{-1}b \quad\Rightarrow{}\quad Ix = A^{-1}b \quad\Rightarrow{}\quad x = A^{-1}b$ <br>
$\Rightarrow{}\quad A^{-1} = \frac{1}{detA}adj(A) \quad\Rightarrow{}\quad A^{-1} = \frac{1}{12} \begin{pmatrix}-3&3&3\\8&-4&0\\7&1&-3\end{pmatrix}$ <br>

$\Rightarrow{}\quad \begin{pmatrix}x  \newline  y  \newline  z\end{pmatrix} = \frac{1}{12} \begin{pmatrix}-3&3&3  \newline  8&-4&0  \newline  7&1&-3\end{pmatrix} \begin{pmatrix}7  \newline  8  \newline  11\end{pmatrix} \quad\Rightarrow{}\quad \begin{pmatrix}x  \newline  y  \newline  z\end{pmatrix} = \begin{pmatrix} 3  \newline  2  \newline  2\end{pmatrix}$ <br>

$\Rightarrow{}\quad \boxed{x=3, \quad y=2, \quad z=2}$
</div>

(b) $\begin{align}
x + 3y + z &= 0  \newline 
5x + y + 3z &= 0  \newline 
4x - 2y + 2z &= 0 \end{align}$
<div class = "answer">$\Rightarrow{}\quad Ax = b \quad\Rightarrow{}\quad \begin{pmatrix}1&3&1\\5&1&3\\4&-2&2\end{pmatrix} \begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}0\\0\\0\end{pmatrix}$ <br>

$\Rightarrow{}\quad detA = 0 \quad\Rightarrow{}\quad$ singular (not invertible) <br>

$\Rightarrow{}\quad \boxed{x/y=4, \quad y/z=1/7}$</div>

(c) $\begin{align}
x + 3y + 4z &= 0  \newline 
x + y + 3z &= 0  \newline 
2x + 5y + z &= 0 \end{align}$
<div class = "answer">$\Rightarrow{}\quad Ax = b \quad\Rightarrow{}\quad \begin{pmatrix}1&3&4 \\ 1&1&3 \\ 2&5&1\end{pmatrix} \begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}0 \\ 0 \\ 0\end{pmatrix}$ <br>

$\Rightarrow{}\quad detA = 13 \quad\Rightarrow{}\quad$ nonsingular (invertible) <br>

$\Rightarrow{}\quad A^{-1}$ can be obtained, but whatever the elements of it $\Rightarrow{}\quad \boxed{x=y=z=0}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><P style="page-break-before: always"></div>

-----------------------------------------------------------------------------------

## Challenging Questions
### Problem 8.
Determine whether the following matrices are symmetric, skew-symmetric, triangular, diagonal or singular:

(a) $\begin{pmatrix}1&2  \newline  2&3\end{pmatrix}$
<div class = "answer">SS

A symmetric matrix is a square matrix that is equal to its transpose; that is, it satisfies the condition $A=A^T$. <br>

A skew-symmetric matrix is a square matrix whose transpose equals its negative; that is, it satisfies the condition $A^T=-A$. <br>

A triangular matrix is a square matrix that is either lower triangular or upper triangular. In a lower triangular matrix, all the entries above the main diagonal are zero. In a upper triangular matrix, all the entries below the main diagonal are zero. <br>

A diagonal matrix is a square matrix that is both upper and lower triangular; that is all entries outside the main diagonal are zero. <br>

A singular matrix is a square matrix that is not invertible. A square matrix is singular if and only if its determinant is 0. <br>

$\quad\Rightarrow{}\quad$
$\begin{pmatrix}1&2  \newline  2&3\end{pmatrix}^T=\begin{pmatrix}1&2 \newline 2&3\end{pmatrix} \quad\Rightarrow{}\ \ \begin{vmatrix}1&2 \newline 2&3\end{vmatrix} = 1(3)-2(2) = 1 \quad\Rightarrow{}\ \ \boxed{\text{symmetric}}$</div>

(b) $\begin{pmatrix}2&1 \newline -1&4\end{pmatrix}$
<div class = "answer">$\quad\Rightarrow{}\quad$
$\begin{pmatrix}2&1\\-1&4\end{pmatrix}^T=\begin{pmatrix}2&-1\\1&4\end{pmatrix} \quad\Rightarrow{}\ \ \begin{vmatrix}2&1\\-1&4\end{vmatrix} = 2(4)-1(-1) = 9 \quad\Rightarrow{}\ \ \boxed{\text{none}}$</div>

(c) $\begin{pmatrix}0&a \newline a&0\end{pmatrix}$
<div class = "answer">
$\quad\Rightarrow{}\quad$
$\begin{pmatrix}0&a\\a&0\end{pmatrix}^T=\begin{pmatrix}0&a\\a&0\end{pmatrix} \quad\Rightarrow{}\ \ \begin{vmatrix}0&a\\a&0\end{vmatrix} = 0(0)-a(a) = -a^2 \quad\Rightarrow{}\ \ \boxed{\text{symmetric}}$</div>

(d) $\begin{pmatrix}a&0 \newline 0&a\end{pmatrix}$
<div class = "answer">$\quad\Rightarrow{}\quad$
$\begin{pmatrix}a&0\\0&a\end{pmatrix}^T=\begin{pmatrix}a&0\\0&a\end{pmatrix} \quad\Rightarrow{}\ \ \begin{vmatrix}a&0\\0&a\end{vmatrix} = a(a)-0(0) = a^2$
$\quad\Rightarrow{}\ \ \boxed{\text{symmetric and diagonal (and triangular)}}$</div>

(e) $\begin{pmatrix}1&1 \newline 1&1\end{pmatrix}$
<div class = "answer">$\quad\Rightarrow{}\quad$
$\begin{pmatrix}1&1\\1&1\end{pmatrix}^T=\begin{pmatrix}1&1\\1&1\end{pmatrix} \quad\Rightarrow{}\ \ \begin{vmatrix}1&1\\1&1\end{vmatrix} = 1(1)-1(1) = 0$
$\quad\Rightarrow{}\ \ \boxed{\text{symmetric and singular}}$</div>

(f) $\begin{pmatrix}0&-1 \newline 1&0\end{pmatrix}$
<div class = "answer">$\quad\Rightarrow{}\quad$
$\begin{pmatrix}0&-1\\1&0\end{pmatrix}^T=\begin{pmatrix}0&1\\-1&0\end{pmatrix} \quad\Rightarrow{}\ \ \begin{vmatrix}0&-1\\1&0\end{vmatrix} = 0(0)--1(1) = 1$
$\quad\Rightarrow{}\ \ \boxed{\text{skew-symmetric}}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><P style="page-break-before: always"></div>

-----------------------------------------------------------------------------------

### Problem 9.
Determine whether the following matrices are singular or orthogonal:

(a) $\begin{pmatrix}1&0.5&0 \newline 0.5&0.75&0.5 \newline 0&0.5&0.5\end{pmatrix}$
<div class = "answer">A orthogonal matrix is a square matrix whose columns and rows are orthogonal unit vectors; that is, it satisfies the condition $Q^TQ=QQ^T=I$.

A singular matrix is a square matrix that is not invertible. A square matrix is singular if and only if its determinant is 0.

$\quad\Rightarrow{}\quad \begin{vmatrix}1&0.5&0 \newline 0.5&0.75&0.5 \newline 0&0.5&0.5\end{vmatrix} = 1\begin{vmatrix}0.75&0.5 \newline 0.5&0.5\end{vmatrix} -0.5\begin{vmatrix}0.5&0.5 \newline 0&0.5\end{vmatrix} +0\begin{vmatrix}0.5&0.75 \newline 0&0.5\end{vmatrix}= 0$
$\quad\Rightarrow{}\quad \boxed{\text{singular}}$ <br>

$\quad\Rightarrow{}\quad \begin{pmatrix}1&0.5&0 \newline 0.5&0.75&0.5 \newline 0&0.5&0.5\end{pmatrix}^T = \begin{pmatrix}1&0.5&0 \newline 0.5&0.75&0.5 \newline 0&0.5&0.5\end{pmatrix}$

$\quad\Rightarrow{}\quad \begin{pmatrix}1&0.5&0 \newline 0.5&0.75&0.5 \newline 0&0.5&0.5\end{pmatrix}\begin{pmatrix}1&0.5&0 \newline 0.5&0.75&0.5 \newline 0&0.5&0.5\end{pmatrix} \neq I \quad\Rightarrow{}\quad \boxed{\text{non orthogonal}} $</div>

(b) $\begin{pmatrix}0.6&-0.8&0 \newline 0.8&0.6&0 \newline 0&0&1\end{pmatrix}$
<div class = "answer">$\quad\Rightarrow{}\quad \begin{vmatrix}0.6&-0.8&0\\0.8&0.6&0\\0&0&1\end{vmatrix} = 0.6\begin{vmatrix}0.6&0\\0&1\end{vmatrix} -0.8\begin{vmatrix}0.8&0\\0&1\end{vmatrix} +0\begin{vmatrix}0.8&0.6\\0&0\end{vmatrix} = 1$ <br>
$\quad\Rightarrow{}\quad \boxed{\text{non singular }}$ <br>

$\quad\Rightarrow{}\quad \begin{pmatrix}0.6&-0.8&0 \newline 0.8&0.6&0 \newline 0&0&1\end{pmatrix}^T = \begin{pmatrix}0.6&0.8&0 \newline -0.8&0.6&0 \newline 0&0&1\end{pmatrix}$ <br>
$\quad\Rightarrow{}\quad \begin{pmatrix}0.6&-0.8&0 \newline 0.8&0.6&0 \newline 0&0&1\end{pmatrix} \begin{pmatrix}0.6&0.8&0 \newline -0.8&0.6&0 \newline 0&0&1\end{pmatrix} = \begin{pmatrix}1&0&0 \newline 0&1&0 \newline 0&0&1\end{pmatrix} \quad\Rightarrow{}\quad \boxed{\text{orthogonal}}$</div>

(c) $\begin{pmatrix}0&2^{-\frac{1}{2}}&2^{-\frac{1}{2}} \newline 2^{-\frac{1}{2}}&-0.5&0.5 \newline 2^{-\frac{1}{2}}&0.5&-0.5\end{pmatrix}$
<div class = "answer">$\quad\Rightarrow{}\quad \begin{vmatrix}0&2^{-\frac{1}{2}}&2^{-\frac{1}{2}}\\2^{-\frac{1}{2}}&-0.5&0.5\\2^{-\frac{1}{2}}&0.5&-0.5\end{vmatrix} = 0\begin{vmatrix}-0.5&0.5\\0.5&-0.5\end{vmatrix} -2^{-\frac{1}{2}}\begin{vmatrix}2^{-\frac{1}{2}}&0.5\\2^{-\frac{1}{2}}&-0.5\end{vmatrix} +2^{-\frac{1}{2}}\begin{vmatrix}2^{-\frac{1}{2}}&-0.5\\2^{-\frac{1}{2}}&0.5\end{vmatrix}$ <br>
$\quad\Rightarrow{}\quad \begin{vmatrix}0&2^{-\frac{1}{2}}&2^{-\frac{1}{2}}\\2^{-\frac{1}{2}}&-0.5&0.5\\2^{-\frac{1}{2}}&0.5&-0.5\end{vmatrix} = 1 \quad\Rightarrow{}\quad \boxed{\text{no singular}}$ <br>
$\quad\Rightarrow{}\quad \begin{pmatrix}0&2^{-\frac{1}{2}}&2^{-\frac{1}{2}}\\2^{-\frac{1}{2}}&-0.5&0.5\\2^{-\frac{1}{2}}&0.5&-0.5\end{pmatrix}^T = \begin{pmatrix}0&2^{-\frac{1}{2}}&2^{-\frac{1}{2}}\\2^{-\frac{1}{2}}&-0.5&0.5\\2^{-\frac{1}{2}}&0.5&-0.5\end{pmatrix}$ <br>
$\quad\Rightarrow{}\quad \begin{pmatrix}0&2^{-\frac{1}{2}}&2^{-\frac{1}{2}}\\2^{-\frac{1}{2}}&-0.5&0.5\\2^{-\frac{1}{2}}&0.5&-0.5\end{pmatrix} \begin{pmatrix}0&2^{-\frac{1}{2}}&2^{-\frac{1}{2}}\\2^{-\frac{1}{2}}&-0.5&0.5\\2^{-\frac{1}{2}}&0.5&-0.5\end{pmatrix} = \begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}\\ \quad\Rightarrow{}\quad \boxed{\text{orthogonal}}$</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><P style="page-break-before: always"></div>

-----------------------------------------------------------------------------------

## Exam Style Questions
### Problem 10.
[10 marks] Given the following matrices: 
$A =  \begin{bmatrix} 
    1 \ 2 \ 0  \newline  3 \ 1 \ 0  \newline  5 \ 0 \ 1
    \end{bmatrix}$ 
$B = \begin{bmatrix}
    3 \ 3 \ 3  \newline  3 \ 3 \ 3
    \end{bmatrix} $
$C = \begin{bmatrix} \ 
    2 \ 1 \ 9 
    \end{bmatrix}.$

(a) Find the determinant of $A$
<div class = "answer">$detA= 1(1)-2(3)+0 = \boxed{-5}$ [1 mark]</div>

(b) Find the inverse of matrix $A$ multiplied by the determinant of $A$
<div class = "answer">
$A^{-1}|A| = \boxed{\begin{bmatrix}
1 & -2 & 0 \\ -3 & 1 & 0 \\ -5 & 10 & -5
\end{bmatrix}}$ [3 marks]</div>

(c) Find the inverse of the transpose of matrix $A$
<div class = "answer">
$(A^{T})^-1 = (A^{-1})^T = \boxed{\frac{1}{-5} \begin{bmatrix}
1 & -3 & -5 \\ -2 & 1 & 10 \\ 0 & 0 & -5
\end{bmatrix}}$ [2 marks]</div>

(d) Find $BA$
<div class = "answer">
$BA = \boxed{\begin{bmatrix}
27 & 9 & 3 \\ 27 & 9 & 3
\end{bmatrix}}$</div>

(e) What are the dimensions of $D$ in the following operation? $D = ((BA)^T B - A)C^T$
<div class = "answer">$[(2x3)(3x3)^T(2x3)-(3x3)](3x1)=\boxed{(3x1)}$ [2 marks]</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><P style="page-break-before: always"></div>

-----------------------------------------------------------------------------------
### Problem 11.
The matrix $\textbf{M}$ is given by:
$$\textbf{M} =
\begin{bmatrix}
k & 2 & 1 \newline
3 & 0 & 4 \newline 
1 & -2 & 1 \newline 
\end{bmatrix}, \quad k \neq 1 $$

(a) Show that the determinant of $\textbf{M} = 8\textit{k}-4$.
<div class = "answer">$Det(\textbf{M}) = k(0+8)-2(3-4)+1(-6)= \boxed{8\textit{k}-4}$</div>

(b) Find $\textbf{M}^{-1}$ in terms of k.
<div class = "answer">
Matrix of minors:
$$
    \begin{bmatrix}
    8 & -1 & -6\\
    4 & k-1 & -(2k+2)\\
    8 & 4k-3 & -6\\
    \end{bmatrix}
$$
Matrix of cofactors and transpose:
$$
    \begin{bmatrix}
    8 & -4 & 8\\
    1 & k-1 & 3-4k\\
    -6 & 2k+2 & -6\\
    \end{bmatrix}
$$
Multiply by $\frac{1}{det(\textbf{M})}$:
$$
\boxed{\frac{1}{8\textit{k}-4}
    \begin{bmatrix}
    8 & -4 & 8\\
    1 & k-1 & 3-4k\\
    -6 & 2k+2 & -6\\
    \end{bmatrix}}
$$
</div>

The straight line $l_{1}$ is mapped onto the straight line $l_{2}$ by the transformation represented by the matrix:
$$
N =
\begin{bmatrix}
1 & 2 & 1 \newline 
3 & 0 & 4 \newline 
1 & -2 & 1 \newline 
\end{bmatrix}
$$
The equation of $l_{2}$ is $(\textbf{r}-\textbf{a})\times\textbf{b}=0$, where $\textbf{a} = 6\textbf{i}+5\textbf{j}+2\textbf{k}$ and $\textbf{b} = 6\textbf{i}+5\textbf{j}+4\textbf{k}$

(c) Find a vector equation for the line $l_{1}$.
<div class = "answer">
Let $(x,y,z)$ be on $l_{1}$.

Equation $l_{2}$ can be written as:

$$r = \begin{pmatrix}
6+6\mu \newline 
5+5\mu \newline 
2+4\mu \newline 
\end{pmatrix}$$


Use $\textbf{N}^{-1}$ to map $l_{2}$ back to $l_{1}$ (matrix N is just matrix M with $k=1$):



$$\begin{pmatrix}
x \newline 
y \newline 
z \newline 
\end{pmatrix} =
\textbf{N}^{-1}
\begin{pmatrix}
6+6\mu \newline 
5+5\mu \newline 
2+4\mu \newline 
\end{pmatrix}$$

$$\begin{pmatrix}
x \newline 
y \newline 
z \newline 
\end{pmatrix} =
\begin{pmatrix}
(12-5+4)+(12-5+8)\mu \newline 
(1.5-0.5)+(1.5-1)\mu \newline 
(-9+5-3)+(-9+5-6)\mu \newline 
\end{pmatrix} =
\textbf{N}^{-1}
\begin{pmatrix}
11+15\mu \newline 
1+0.5\mu \newline 
-7-10\mu \newline 
\end{pmatrix}$$

Therefore the equation of $l_{1}$ is $\boxed{(\textbf{r}-\textbf{a})\times \textbf{b}}$ or $\boxed{\textbf{r}=\textbf{a}+\mu\textbf{b}}$ where $\boxed{\textbf{a}=11i+j-k}$ and $\boxed{\textbf{b}=15i+0.5j+2k}$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><P style="page-break-before: always"></div>


## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>
<br><br>
### For Printing
<button type="button" onclick="prepareForPrint('block')">Add whitespace</button>
<button type="button" onclick="prepareForPrint('none')">Remove whitespace</button>

<br><br>

# Next week, another Linear Transforms and Eigenproblems!