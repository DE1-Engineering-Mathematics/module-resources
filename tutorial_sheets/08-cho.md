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

# Coupled Harmonic Oscillators Tutorial Sheet, Week 8

### Learning targets
* Write down the equations of motion for a system
* Rewrite equations of motion in matrix form
* Find eigenvalues to solve for mode shapes

<!-- ### Reading
* [section](link#page=x) -->

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
For each one of the following systems, write down the equation of motion of the masses involved, considering undriven and undamped motion. Then, express these equations in matrix form with separate vectors containing only displacements and accelerations. Finally, determine the characteristic frequencies and the corresponding mode shapes.

(a) Consider the masses $m_1=2m$ and $m_2=m$ and the spring constants $k_1=k_2=k$ The locations of the two masses are described by the variables $x_1$ and $x_2$, which are both zero when the system is in static equilibrium.

<img src = "08-cho-media\figure3.PNG" width="20%" style = "margin: 10px auto 20px; display: block;">

<div class = "answer">
$\Rightarrow$ Although the system is vertical, gravity can be ignored as $x_1$ and $x_2$ are defined as zero when the system is in static equilibrium, which accounts for this effect.

$\Rightarrow$ The equation of motion of the masses are:
$$2m\ddot{x}_1+2kx_1-kx_2= 0
\\\ 
m\ddot{x}_2-kx_1+kx_2= 0$$

$\Rightarrow$ Writing the system in matrix form:

$$
\boxed{\begin{bmatrix}
-\frac{k}{m} & \frac{k}{2m}\\\ 
\frac{k}{m}   & -\frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
x_1\\\ 
x_2
\end{bmatrix} =
\begin{bmatrix}
\ddot{x}_1\\\ 
\ddot{x}_2
\end{bmatrix}}
$$

$\Rightarrow$ Trial solution for $x_1$ and $x_2$:
$$ 
x_1=A_{1}\cos(\omega t),\quad \ddot{x}\_1 = - A\_{1}\omega^{2}\cos (\omega t)
\\\ 
x_2=A_{2}\cos(\omega t),\quad \ddot{x}\_2=-A\_{2}\omega^{2}\cos (\omega t)
$$

$\Rightarrow$ Therefore:
$$
\begin{bmatrix}
-\frac{k}{m} & \frac{k}{2m}\\\ 
\frac{k}{m}   & -\frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
A_1\\\ 
A_2
\end{bmatrix} =-\omega ^{2}
\begin{bmatrix}
{A}_1\\\ 
{A}_2
\end{bmatrix}
$$

$\Rightarrow \det(A−\lambda I) = 0$:
$$
\begin{vmatrix}
-\frac{k}{m} -\lambda & \frac{k}{2m}\\\ 
\frac{k}{m}   & -\frac{k}{m}-\lambda 
\end{vmatrix}
= 0
$$

$\Rightarrow \lambda_1 = -\frac{k}{m}+\frac{1}{\sqrt{2}}\frac{k}{m},\ \lambda_2 =-\frac{k}{m}-\frac{1}{\sqrt{2}}\frac{k}{m},\quad \omega_1^{2} = \frac{k}{m}-\frac{1}{\sqrt{2}}\frac{k}{m},\ \omega_2^{2} = \frac{k}{m}+\frac{1}{\sqrt{2}}\frac{k}{m}$}

$\Rightarrow \boxed{\omega_1 = \sqrt{\frac{k}{m}-\frac{1}{\sqrt{2}}\frac{k}{m}}}, \boxed{\ \omega_2 =\sqrt{\frac{k}{m}+\frac{1}{\sqrt{2}}\frac{k}{m}}}$

$\Rightarrow$ Mode shape for $\omega_1 = \sqrt{\frac{k}{m}-\frac{1}{\sqrt{2}}\frac{k}{m}}$ :

$$
\boxed{
\begin{bmatrix}
-\frac{1}{\sqrt{2}}\frac{k}{m} & \frac{k}{2m}\\\ 
\frac{k}{m} & -\frac{1}{\sqrt{2}}\frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
A_1\\\ 
A_2
\end{bmatrix} =
\begin{bmatrix}
0\\\ 
0
\end{bmatrix}}
$$

$\Rightarrow \frac{1}{\sqrt{2}}A_1=\frac{1}{2}A_2$, masses move in phase with each other in the same direction.}

Mode shape for $\omega_2 =\sqrt{\frac{k}{m}+\frac{1}{\sqrt{2}}\frac{k}{m}}$ :
$$
\boxed{
\begin{bmatrix}
\frac{1}{\sqrt{2}}\frac{k}{m} & \frac{k}{2m}\\\ 
\frac{k}{m} & \frac{1}{\sqrt{2}}\frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
A_1\\\ 
A_2
\end{bmatrix} =
\begin{bmatrix}
0\\\ 
0
\end{bmatrix}}
$$

$\frac{1}{\sqrt{2}}A_1=-\frac{1}{2}A_2$, masses move in opposite directions.
</div>

------------------------------------------------------

(b) Consider the masses $m_1=m_2=m$, lengths $L_1=L_2=L$, spring constant $k$ and that gravity produces oscillatory motions, given by $-mg\sin(\theta)$, if the pendulums are offset from their equilibrium positions.
<img src = "08-cho-media\figure2.PNG" width="40%" style = "margin: 10px auto 20px; display: block;">
<div class = "answer">
$\Rightarrow$ The equation of motion of the masses are:
$$
m_1\ddot{x}_1+mg\sin(\theta_1)+(x_{1}-x_2)k= 0
\\\ 
m_2\ddot{x}_2+mg\sin(\theta_2)+(x_{2}-x_1)k= 0
$$

$\Rightarrow$ Expressing the $\sin(\theta)$ in terms of $x$ and $L$:
$$
-\big(\frac{g}{L}+\frac{k}{m})x_1+\frac{k}{m}x_2=\ddot{x}_1
\\\
-\big(\frac{g}{L}+\frac{k}{m})x_2+\frac{k}{m}x_1=\ddot{x}_2
$$

$\Rightarrow$ Writing the system in matrix form:
$$
\boxed{
\begin{bmatrix}
-(\frac{g}{L}+\frac{k}{m}) & \frac{k}{m}\\\ 
\frac{k}{m}   & -(\frac{g}{L}+\frac{k}{m})
\end{bmatrix}
\begin{bmatrix}
x_1\\\ 
x_2
\end{bmatrix}
=-\omega ^{2}
\begin{bmatrix}
\ddot{x}_1\\\ 
\ddot{x}_2
\end{bmatrix}}
$$

$\Rightarrow$ Therefore:
$$
\begin{bmatrix}
-(\frac{g}{L}+\frac{k}{m}) & \frac{k}{m}\\\ 
\frac{k}{m}   & -(\frac{g}{L}+\frac{k}{m})
\end{bmatrix}
\begin{bmatrix}
A_1\\\ 
A_2
\end{bmatrix}
=-\omega ^{2}
\begin{bmatrix}
{A}_1\\\ 
\ddot{}{A}_2
\end{bmatrix}
$$

$\Rightarrow \det(A-\lambda I) = 0$:
$$
\begin{vmatrix}
-(\frac{g}{L}+\frac{k}{m}) -\lambda& \frac{k}{m}\\\ 
\frac{k}{m}   & -(\frac{g}{L}+\frac{k}{m})-\lambda\\\ 
\end{vmatrix}
= 0
$$

$\Rightarrow \lambda_1 = -\frac{g}{L}-2\frac{k}{m},\ \lambda_2 = -\frac{g}{L},\quad \omega_1^{2} = \frac{g}{L}+2\frac{k}{m},\ \omega_2^{2} = \frac{g}{L}$

$$\boxed{\omega_1 = \sqrt{\frac{g}{L}+2\frac{k}{m}},\ \omega_2 =\sqrt{\frac{g}{l}}}$$

$\Rightarrow$ Mode shape for $ \omega_1 = \sqrt{\frac{g}{L}+2\frac{k}{m}}$:
$$
\boxed{
\begin{bmatrix}
\frac{k}{m} & \frac{k}{m}\\\ 
\frac{k}{m} & \frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
A_1\\\ 
A_2
\end{bmatrix}=
\begin{bmatrix}
0\\\ 
0
\end{bmatrix}}
$$

$A_1=-A_2$, masses move in opposite directions with equal but opposite displacements.}

$\Rightarrow$ Mode shape for $\omega_2 =\sqrt{\frac{g}{L}}$:
$$
\boxed{
\begin{bmatrix}
-\frac{k}{m} & \frac{k}{m}\\\ 
\frac{k}{m} & -\frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
A_1\\\ 
A_2
\end{bmatrix}=
\begin{bmatrix}
0\\\ 
0
\end{bmatrix}}
$$

$\Rightarrow A_1=A_2$, masses move in phase with each other, in the same direction.

</div>

------------------------------------------------------

## Exam Style Questions
### Problem 3.
Consider the masses $m_1=m_2=m$ and the spring constants $k_1=k_2=k_3=k$
<img src = "08-cho-media\figure1.PNG" width="80%" style = "margin: 10px auto 20px; display: block;">

<div class = "answer">
$\Rightarrow$ The equation of motion of the masses are (mass times acceleration of each mass is equal to the resulting force acting on each mass):
$$
m_1\ddot{x}_1+(k_1+k_2)x_1-k_2x_2= 0
\\\  
m_{2}\ddot{x}_2+(k_3+k_2)x_2-k_2x_1= 0
$$

$\Rightarrow$ Writing the system in matrix form:
$$
\boxed{
\begin{bmatrix}
-2\frac{k}{m} & \frac{k}{m}\\\ 
\frac{k}{m}   & -2\frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
x_1\\\ 
x_2
\end{bmatrix} =
\begin{bmatrix}
\ddot{x}_1\\\ 
\ddot{x}_2
\end{bmatrix}}
$$

$\Rightarrow$ Trial solution for $x_1$ and $x_2$:
$$
x_1=A_{1}\cos(\omega t),\quad \ddot{x}\_1=-A\_{1}\omega^{2}\cos (\omega t) \\\ 
x_2=A_{2}\cos(\omega t),\quad \ddot{x}\_2=-A\_{2}\omega^{2}\cos (\omega t)
$$

$\Rightarrow$ Therefore:
$$
\begin{bmatrix}
-2\frac{k}{m} & \frac{k}{m}\\\ 
\frac{k}{m}   & -2\frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
A_1\\\ 
A_2
\end{bmatrix}
=-\omega ^{2}
\begin{bmatrix}
{A}_1\\\ 
{A}_2
\end{bmatrix}
$$

$\Rightarrow \det(A-\lambda I) = 0$:
$$
\begin{vmatrix}
-2\frac{k}{m} -\lambda & \frac{k}{m}\\\ 
\frac{k}{m}   & -2\frac{k}{m}-\lambda 
\end{vmatrix}
= 0
$$

$\Rightarrow\lambda_1 = -3\frac{k}{m},\ \lambda_2 = -\frac{k}{m},\quad \omega_1^{2} = 3\frac{k}{m},\ \omega_2^{2} = \frac{k}{m}$

$\Rightarrow \boxed{\omega_1 = \sqrt{3\frac{k}{m}},\ \omega_2 =\sqrt{\frac{k}{m}}}$

$\Rightarrow$ Mode shape for $\omega_1 = \sqrt{3\frac{k}{m}}\quad$(sub $\lambda_1$ into det$(A-\lambda I) = 0$):
$$
\boxed{
\begin{bmatrix}
\frac{k}{m} & \frac{k}{m}\\\ 
\frac{k}{m} & \frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
A_1\\\ 
A_2
\end{bmatrix} =
\begin{bmatrix}
0\\\ 
0
\end{bmatrix}}
$$

$\Rightarrow$ $A_1=-A_2$, masses move in opposite directions with equal but opposite displacements.

Mode shape for $\omega_2 =\sqrt{\frac{k}{m}}\quad$(sub $\lambda_2$ into det$(A-\lambda I)=0$):
$$
\boxed{
\begin{bmatrix}
-\frac{k}{m} & \frac{k}{m}\\\ 
\frac{k}{m} & -\frac{k}{m}
\end{bmatrix}
\begin{bmatrix}
A_1\\\ 
A_2
\end{bmatrix} =
\begin{bmatrix}
0\\\ 
0
\end{bmatrix}}
$$

$A_1=A_2$, masses move in phase with each other, in the same direction.
</div>

------------------------------------------------------

<br><br>

## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>

<br><br>

# Next week, a test! :)