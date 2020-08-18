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

# Tutorial Sheet Title, Week 3

### Learning targets
* Perform operations on matrices (add, subtract, multiply)
* Find the transpose, adjudicate, determinant of 2x2 and 3x3 matrices
* use matrices to find the solutions to linear equations
* Identify unit, symmetric, skew-symmetric, triangular, diagonal, singular and orthogonal matrices

### Reading
* [section](link#page=x)

### Lectures
* One (monday)
* Two (tuesday)

### Additional resources
*insert links*

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Given the matrices: $A=\begin{pmatrix}1&1\\\\2&-1\end{pmatrix}$ and $B=\begin{pmatrix}0&1\\\\-2&3\end{pmatrix}$ <br>
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

-----------------------------------------------------------------------------------

## Problem 2
Given the matrices:

$A=\begin{pmatrix}2&0\\\\3&-1\\\\1&4\end{pmatrix}$, 
$B=\begin{pmatrix}-1&-3\\\\5&2\\\\7&1\end{pmatrix}$ and 
$C=\begin{pmatrix}1&3&5&7\\\\2&4&6&8\end{pmatrix}$

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
<div class = "answer">$\begin{pmatrix}2&0\\3&-1\\1&4\end{pmatrix} \begin{pmatrix}-1&-3\\5&2\\7&1\end{pmatrix}^T\ \Rightarrow{}\begin{pmatrix}2&0\\3&-1\\1&4\end{pmatrix} \begin{pmatrix}-1&5&7\\-3&2&1\end{pmatrix}$ <br>
$\Rightarrow{} \begin{pmatrix}2(-1)+0(-3)&2(5)+0(2)&2(7)+0(1)\\3(-1)-1(-3)&3(5)-1(2)&3(7)-1(1)\\1(-1)+4(-3)&1(5)+4(2)&1(7)+4(1)\end{pmatrix}\ \ \ \ \Rightarrow{}\ \ \boxed{\begin{pmatrix}-2&10&14\\0&13&20\\-13&13&11\end{pmatrix}}$</div>

-----------------------------------------------------------------------------------

### Problem 3.
(a) Find the solution to the following linear equations: 
$$3x + 2y + z = 10$$
$$3x + 5z = 6$$
$$2x + 4y - 4z = 2$$

<div class = "answer">$\Rightarrow{} \begin{pmatrix}3&2&1\\3&0&-5\\2&4&-4\end{pmatrix} \begin{pmatrix}x\\y\\z\end{pmatrix} = 
\begin{pmatrix}10\\6\\2\end{pmatrix}$ <br>
$\Rightarrow\begin{pmatrix}x\\y\\z\end{pmatrix} = 
\begin{pmatrix}3&2&1\\3&0&-5\\2&4&-4\end{pmatrix} \ 
\begin{pmatrix}10\\6\\2\end{pmatrix}$ <br>
$\Rightarrow{} \quad\boxed{ x = 27 \\ y = -28 \\ z = -15}$</div>

### Problem 4.
Evaluate the following determinants:

(a) $\begin{vmatrix}20&6\\\\1&2\end{vmatrix}$
<div class = "answer">$\Rightarrow{}$
$20(2)-6(1) \ \Rightarrow{}\ \boxed{34}$</div>

(b) $\begin{vmatrix}1&2&6\\\\1&3&9\\\\1&4&12\end{vmatrix}$
<div class = "answer">$\Rightarrow{}\ \ 1\begin{vmatrix}3&9\\4&12\end{vmatrix}-2\begin{vmatrix}1&9\\1&12\end{vmatrix}+6\begin{vmatrix}1&3\\1&4\end{vmatrix}$ <br>
$\Rightarrow{}\ \ 1[3(13)-9(4)]-2[1(12)-9(1)]+6[1(4)-3(1)] \ \ \Rightarrow{}\ \ \boxed{0}$</div>

(c) $\begin{vmatrix}1&1&1\\ \lambda & \mu & \nu\\ \lambda^3 & \mu^3 & \nu^3\end{vmatrix}$
<div class = "answer">
$\Rightarrow{}\ \ 1\begin{vmatrix}\mu & \nu \\ \mu^3 & \nu^3 \end{vmatrix}-1\begin{vmatrix}\lambda & \nu \\ \lambda^3 & \nu^3 \end{vmatrix}+1\begin{vmatrix}\lambda & \mu \\ \lambda^3 & \mu^3 \end{vmatrix}$ <br>
$\Rightarrow{}\ \ (\mu\nu^3-\nu\mu^3) - (\lambda\nu^3-\nu\lambda^3) + (\lambda\mu^3-\mu\lambda^3)$
$\Rightarrow{}\ \ \boxed{\nu^3(\mu-\lambda)+\mu^3(\lambda-\nu)+\lambda^3(\nu-\mu)}$</div>

### Problem 5.
Determine the elements of the matrix $M$, so that $AMB=C$, where

$A=\begin{pmatrix}2&1&1\\\\1&1&0\\\\0&0&1\end{pmatrix}$, $B=\begin{pmatrix}3&1\\\\1&1\end{pmatrix}$ and $C=\begin{pmatrix}1&1\\\\2&2\\\\1&1\end{pmatrix}$
<div class = "answer">
$\Rightarrow{}\quad M=A^{-1}CB^{-1}$ <br>
$\Rightarrow{}\quad det(a)=1$ and $det(b)=2$ <br>
$\Rightarrow{}\quad B^{-1}=\frac{1}{det(c)}adj(d) \quad\Rightarrow{}\quad B^{-1}=\frac{1}{2}\begin{pmatrix}1&-1\\-1&3\end{pmatrix} \quad\Rightarrow{}\quad B^{-1}=\begin{pmatrix}1/2&-1/2\\-1/2&3/2\end{pmatrix}$
$\Rightarrow{}\quad A^{-1}=\frac{1}{det(e)}adj(f)=\frac{1}{det(g)}C_A^T$, where $C_A$ is the cofactor matrix of A
$\Rightarrow{}\quad C_A=\begin{pmatrix}
\begin{vmatrix}1&0\\0&1\end{vmatrix} & -\begin{vmatrix}1&0\\0&1\end{vmatrix} & \begin{vmatrix}1&1\\0&0\end{vmatrix}\\ 
-\begin{vmatrix}1&1\\0&1\end{vmatrix} & \begin{vmatrix}2&1\\0&1\end{vmatrix} & -\begin{vmatrix}2&1 \\0&0\end{vmatrix} <br>
\begin{vmatrix}1&1\\1&0\end{vmatrix} & -\begin{vmatrix}2&1\\1&0\end{vmatrix} & \begin{vmatrix}2&1\\1&1\end{vmatrix}
\end{pmatrix} \quad\Rightarrow{}\quad C_A=\begin{pmatrix}1&-1&0\\-1&2&0\\-1&1&1\end{pmatrix}$
$\Rightarrow{}\quad C_A^T=\begin{pmatrix}1&-1&-1\\-1&2&1\\0&0&1\end{pmatrix}$\\
$\Rightarrow{}\quad A^{-1}=\begin{pmatrix}1&-1&-1\\-1&2&1\\0&0&1\end{pmatrix}$ <br>
$\Rightarrow{} \quad M=\begin{pmatrix}1&-1&-1\\-1&2&1\\0&0&1\end{pmatrix} \begin{pmatrix}1&1\\2&2\\1&1\end{pmatrix}\begin{pmatrix}1/2&-1/2\\-1/2&3/2\end{pmatrix} \quad\Rightarrow{} \quad \boxed{M=\begin{pmatrix}0&-2\\0&4\\0&1\end{pmatrix}}$
</div>

### Problem 6.
(a) Given $A=\begin{pmatrix}1&2&3\\\\1&3&5\\\\1&5&12\end{pmatrix}$ find $\|A\|$, the adjoint of $A$ and $A^{-1}$. Verify that $AA^{-1}=I$, where $I$ is the corresponding unit matrix.
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

-----------------------------------

## Exam Style Questions
### Problem n.

-----------------------------------

## Challenging Questions
### Problem n.

## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>

<br><br>

# Next week, another topic!
![vectors](02-vectors-media/cover.png)