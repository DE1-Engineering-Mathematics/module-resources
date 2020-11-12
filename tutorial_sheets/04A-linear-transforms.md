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

# Linear Transforms Tutorial Sheet, Sheet #4A

### Learning Targets
* Understand and produce a graphical representation of a transformation matrix
* Find the transformation matrix for given representations of linear transformations
* Find the null space
* Understand how the relationship between the determinant of a matrix as area scale factor for a linear transformation

### Additional Resources
* [3Blue1Brown - Linear Algebra Playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
* [AFP - Interactive linear transforms](https://fourier.space/assets/matrices/index.html)
* [Let's remove Quaternions from every 3D Engine: Intro to Rotors from Geometric Algebra](https://youtu.be/syyK6hTWT7U)

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
From the following linear transformations, $T:\mathbb{R} \rightarrow \mathbb{R}$ where $T(a) = b$, express $b$ as a function of $a$.

(a)


![1a](04A-linear-transforms-media/1a.png)

<div class = "answer">$T(a)=3a$</div>

(b)

![1b](04A-linear-transforms-media/1b.png)
<div class = "answer">$T(a)=-a/2$</div>

(c)

![1c](04A-linear-transforms-media/1c.png)
<div class = "answer">$T(a)=3a/2$</div>

(d)

![1d](04A-linear-transforms-media/1d.png)
<div class = "answer">$T(a)=-2a$</div>

-----------------------------------------------------------------------------------

### Problem 2.
The following graphs show pairs of vectors where the vector $\vec{a}$ is linearly transformed to $\vec{b}$ by a matrix, $T:\mathbb{R}^2 \rightarrow \mathbb{R}^2$. Considering that these transformations are all pure scalings, find the transformation matrix ($A$) in each case.

(a)

![2a](04A-linear-transforms-media/2a.png)
<div class = "answer">$\Rightarrow{}\quad T\bigg(\begin{pmatrix}a_1\\a_2\end{pmatrix}\bigg)=\begin{pmatrix}1&0\\0&-3\end{pmatrix} \begin{pmatrix}a_1\\a_2\end{pmatrix}$</div>

(b)

![2b](04A-linear-transforms-media/2b.png)
<div class = "answer">$\Rightarrow{}\quad T\bigg(\begin{pmatrix}a_1\\a_2\end{pmatrix}\bigg)=\begin{pmatrix}-1&0\\0&1\end{pmatrix} \begin{pmatrix}a_1\\a_2\end{pmatrix}$</div>

(c)

![2c](04A-linear-transforms-media/2c.png)
<div class = "answer">$\Rightarrow{}\quad T\bigg(\begin{pmatrix}a_1\\a_2\end{pmatrix}\bigg)=\begin{pmatrix}-2&0\\0&-3/2\end{pmatrix} \begin{pmatrix}a_1\\a_2\end{pmatrix}$</div>


(d)

![2d](04A-linear-transforms-media/2d.png)
<div class = "answer">$\Rightarrow{}\quad T\bigg(\begin{pmatrix}a_1\\a_2\end{pmatrix}\bigg)=\begin{pmatrix}-2&0\\0&-4\end{pmatrix} \begin{pmatrix}a_1\\a_2\end{pmatrix}$</div>

-----------------------------------------------------------------------------------

### Problem 3.
The following graphs show pairs of vectors where the vector $\vec{a}$ is linearly transformed to $\vec{b}$ by a matrix, $T:\mathbb{R}^2 \rightarrow \mathbb{R}^2$. Considering that these transformations are all pure rotations (anti-clockwise from $\hat{i}$ should be assumed for rotations unless otherwise stated, just like for polar coordinates), find the angle $\theta$ and matrix $A$ in each case. $\bigg($NB. $R(\theta)=\begin{pmatrix}\cos{\theta}&-\sin{\theta}\\\sin{\theta}&\cos{\theta}\end{pmatrix}\bigg)$


(a)

![3a](04A-linear-transforms-media/3a.png)
<div class = "answer">$\Rightarrow{}\quad T\bigg(\begin{pmatrix}a_1\\a_2\end{pmatrix}\bigg)=\begin{pmatrix}-1&0\\0&-1\end{pmatrix} \begin{pmatrix}a_1\\a_2\end{pmatrix}$ <br>
$\Rightarrow{}\quad \cos^{-1}(-1)=180^{\circ}$</div>

(b)

![3a](04A-linear-transforms-media/3b.png)
<div class = "answer">$\Rightarrow{}\quad T\bigg(\begin{pmatrix}a_1\\a_2\end{pmatrix}\bigg)=\begin{pmatrix}0&-1\\1&0\end{pmatrix} \begin{pmatrix}a_1\\a_2\end{pmatrix}$ <br>
$\Rightarrow{}\quad \sin^{-1}(1)=90^{\circ}$</div>

### Problem 4.
From applying a linear transformation, $T:\mathbb{R}^2 \rightarrow \mathbb{R}^2$ where $T(\vec{a}) = \vec{b}$. Find the vector $\vec{b}$ resulting when a <u>clockwise</u> rotation described by $R(\theta)=\begin{pmatrix}\cos{\theta}&\sin{\theta} \\\ -\sin{\theta}&\cos{\theta}\end{pmatrix}$ is applied to $\vec{a}$. Sketch the vectors $\vec{a}$ and $\vec{b}$ on a Cartesian axes

(a) $\vec{a}=\begin{pmatrix}2\\\2\end{pmatrix}$ and $\theta=60^{\circ}$
<div class = "answer">$R(60^{\circ})=\begin{pmatrix}0.5&0.866\\-0.866&0.5\end{pmatrix}$ <br>
$\Rightarrow{}\quad \begin{pmatrix}0.5&0.866\\-0.866&0.5\end{pmatrix} \begin{pmatrix}2\\2\end{pmatrix} = \boxed{ \begin{pmatrix}2.732\\-0.732\end{pmatrix}}$ <br>
$\Rightarrow{}\quad$ <br>
<img src = "04A-linear-transforms-media/4a.png"> 
</div>

(b) $a=\begin{pmatrix}2 \newline 3\end{pmatrix}$ and $\theta=45^{\circ}$
<div class = "answer">$R(45^{\circ})=\begin{pmatrix}0.7071&0.7071\\-0.7071&0.7071\end{pmatrix}$ <br>
$\Rightarrow{}\quad \begin{pmatrix}0.7071&0.7071\\-0.7071&0.7071\end{pmatrix} \begin{pmatrix}2\\3\end{pmatrix} = \boxed{ \begin{pmatrix}3.536\\0.7071\end{pmatrix}}$ <br>
$\Rightarrow{}\quad$ <br>
<img src = "04A-linear-transforms-media/4b.png"> </div>

-----------------------------------------------------------------------------------

### Problem 5.
From the linear transformations represented in the following figures, obtain the transformation matrix and the change in size (\ie product of change in each dimension, such as area or volume). (NB. The red vector shown is the result of transforming the blue vector.


(a)

<img src = "04A-linear-transforms-media/5a.png">
<div class = "answer">$A = \begin{pmatrix}2&0\\0&1\end{pmatrix}$ and $\det(A) = 2$</div>

(b)

<img src = "04A-linear-transforms-media/5b.png">
<div class = "answer">$A = \begin{pmatrix}1&2\\0&1\end{pmatrix}$ and $\det(A) = 1$</div>

(c)

<img src = "04A-linear-transforms-media/5c.png">
<div class = "answer">$A = \begin{pmatrix}2&0\\0&2\end{pmatrix}$ and $\det(A) = 4$</div>

(d)

<img src = "04A-linear-transforms-media/5d.png">
<div class = "answer">$A = \begin{pmatrix}2&-1\\0&2\end{pmatrix}$ and $\det(A) = 4$</div>

(e)

<img src = "04A-linear-transforms-media/5e.png">
<div class = "answer">$A = \begin{pmatrix}0.5&0\\-0.5&0.5\end{pmatrix}$ and $\det(A) = 0.25$</div>

(f)

<img src = "04A-linear-transforms-media/5f.png">
<div class = "answer">$A = \begin{pmatrix}0&-2\\2&0\end{pmatrix}$ and $\det(A) = 4$</div>

(g)

<img src = "04A-linear-transforms-media/5g.png">
<div class = "answer">$A = \begin{pmatrix}0&2\\-2&0\end{pmatrix}$ and $\det(A) = 4$</div>

(h)

<img src = "04A-linear-transforms-media/5h.png">
<div class = "answer">$A = \begin{pmatrix}2&0\\0&-2\end{pmatrix}$ and $\det(A) = -4$</div>

(i)

<img src = "04A-linear-transforms-media/5i.png">

NB. Difficult to see exactly in 3D, but each of the scalings are integers.

<div class = "answer">$A = \begin{pmatrix}2&0&0\\0&1&0\\0&0&3\end{pmatrix}$ and $\det(A) = 6$</div>

-----------------------------------------------------------------------------------

### Problem 6.
For the following linear systems of equations find the null space and the corresponding solution of $x$ and $y$. Sketch the solutions as lines in a Cartesian axes

(a) $\begin{pmatrix}1&1 \\\ 2&1\end{pmatrix} \begin{pmatrix}x \\\ y\end{pmatrix} = \begin{pmatrix}2 \\\ 3\end{pmatrix}$

<div class = "answer">$\Rightarrow{}\quad$
$A^{-1} = \frac{1}{-1} \begin{pmatrix}1&-1\\-2&1\end{pmatrix} = \begin{pmatrix}-1&1\\2&-1\end{pmatrix}$ <br>
$\Rightarrow{}\quad \begin{pmatrix}x\\y\end{pmatrix} = A^{-1}b = \begin{pmatrix}-1&1\\2&-1\end{pmatrix} \begin{pmatrix}2\\3\end{pmatrix} \quad\Rightarrow{}\quad \boxed{\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}1\\1\end{pmatrix}}$ <br>

<img src = "04A-linear-transforms-media/6aA.png">
</div>

(b) $\begin{pmatrix}2&4\\\ 1&3\end{pmatrix} \begin{pmatrix}x\\\ y\end{pmatrix} = \begin{pmatrix}6\\\ 12\end{pmatrix}$

<div class = "answer">$\Rightarrow{}\quad$
$A^{-1} = \frac{1}{2} \begin{pmatrix}3&-4\\-1&2\end{pmatrix} = \begin{pmatrix}3/2&-2\\-1/2&1\end{pmatrix}$ <br>
$\Rightarrow{}\quad \begin{pmatrix}x\\y\end{pmatrix} = A^{-1}b = \begin{pmatrix}3/2&-2\\-1/2&1\end{pmatrix} \begin{pmatrix}6\\12\end{pmatrix}$
$\Rightarrow{}\quad\boxed{\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}-15\\9\end{pmatrix}}$ <br>

<img src = "04A-linear-transforms-media/6bA.png">
</div>

-----------------------------------

## Challenging Questions
### Problem 7.
The following figure shows a square in $\mathbb{R}^2$, marked with a circle and cross on its perimeter.
<img src = "04A-linear-transforms-media/7a.png">

(a) On a single plot, sketch the result of applying the following transformation, A, to the square (including the new locations of the circle and cross) 
$$A = \begin{bmatrix} 2 \ 0 \\\ 1 \ 1.5\end{bmatrix}$$

<div class = "answer"><img src = "04A-linear-transforms-media/7aA.png"></div>

(b) Assuming the area of the initial square is 4, what is the area of this region after the transformation?
<div class = "answer">$\det(A) = 3$, therefore area$ = 3 \cdot 4 = \boxed{12}$</div>

<br><br>

## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>

<br><br>

# Next week, Power Series and Sequences!