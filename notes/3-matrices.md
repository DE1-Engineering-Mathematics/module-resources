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

## [Return to Contents](notes-contents)

<img src="figs/MatrixChap.svg" width="200"/>

# Chapter 3 - Matrices
### What is a Matrix?

$$\begin{pmatrix*}
1 & 3 & 0 \\
-2 & 8 & 2 \\
4 & 0 & -1 \\
\frac{1}{2} & 0 & 117
\end{pmatrix*}$$

<br>

A *matrix* is a rectangular array of *elements*. These elements could be anything, but they are usually numbers when we discuss them as engineers. The core idea of matrices is *ordering*, by which we mean that the *location* of each element in our matrix tells us something about it. Compare a shopping list, which is an unordered vector where the location of each item on it doesn't really matter; to a digital image, which is a matrix of numbers representing colours, where clearly the location matters a lot!


The above matrix is a 4$\times$3 matrix, ie it has four rows and three columns, so 12 elements in total.


We use matrices in mathematics and engineering because often we need to deal with several variables at once - eg coordinate vectors, as we saw in the previous chapter are a type of matrix which only has either a single column or a single row. In the following chapter on 'linear transformations' we'll see a particular interpretation of the structure of a matrix relating to operations that transform vectors, but in this chapter we're simply going to lay out the language and start building up a toolbox. 


It turns out that many operations that are needed to be performed on coordinates of points are **linear operations** and so can be organised in terms of rectangular arrays of numbers (matrices). Then we find that matrices themselves can, under certain conditions, be added, subtracted and multiplied so that there arises a whole new set of algebraic rules for their manipulation
<br><br>
In general, a matrix '$\textit{A}$' with dimensions of ($n \times m$) looks like:
<br><br>

$$A =
\begin{pmatrix}
	a_{11} & a_{12} & a_{13} & \dots & a_{1,m-1} & a_{1,m} \\
	a_{21} & a_{22} & a_{23} & \dots & a_{2,m-1} & a_{2,m} \\
	a_{31} & a_{32} & a_{33} & \dots & a_{3,m-1} & a_{3,m} \\
	\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
	a_{n-1,1} & a_{n-1,2} & a_{n-1,3} & \dots & a_{n-1,m-1} & a_{n-1,m} \\
	a_{n,1} & a_{n,2} & a_{n,3} & \dots & a_{n,m-1} & a_{n,m}
\end{pmatrix}$$

<br><br>
It is convention to denote entries within a matrix $a_{ij}$, where $\textit{i}$ denotes the row and $\textit{j}$ denotes the column, also a capital letter is typically used to define the matrix itself.
<br><br>
The following sections describe methods for calculating various matrix operations; **however**, since the advent of modern computing, **no one does this by hand any more** ... So you might wonder why we're going over it! The answer is partly so that you know what's going on in the machine and partly to make you appreciate how incredible computing power is!<br><br>

## <a id="matrix-operations"></a>3.1 Matrix Operations
### 3.1.1 Addition
It is possible to add two matrices together, but *only if they have the same dimensions*. We simply add the corresponding entries to form a new matrix of the same size:<br><br>

$$\begin{pmatrix}
	1 & 3 & 0 \\
	-2 & 8 & 2 \\
	4 & 0 & -1 \\
	\frac{1}{2} & 0 & 117
\end{pmatrix}
+
\begin{pmatrix}
	4 & 0 & 1 \\
	0 & -8 & -3 \\
	5 & 1 & -2 \\
	\frac{1}{2} & 1 & -50
\end{pmatrix}
=
\begin{pmatrix}
	5 & 3 & 1 \\
	-2 & 0 & -1 \\
	9 & 1 & -3 \\
	1 & 1 & 67
\end{pmatrix}$$

<br><br>
If two matrices do not have the same dimensions they cannot be added, or we say the sum is 'not defined'.<br><br>

### 3.1.2 Multiplication or "Rows times cols"


### 3.1.3 Scalar Multiplication

## <a id="rules"></a>3.2 Rules of Addition and Multiplication

## <a id="transpose"></a>3.3 Transpose

## <a id="square-matrices"></a>3.4 Square Matrices
### 3.4.1 Identity Matrix
### 3.4.2 Determinants

## <a id="inverses"></a>3.5 Inverses
### 3.5.1 Inverse of a (2x2) Matrix
### 3.5.2 Inverse of (3x3) matrices (or higher)

## <a id="linear-systems"></a>3.6 Linear Systems
### 3.6.1 Larger Systems

## <a id="labels"></a>3.7 Labels

## Conclusions