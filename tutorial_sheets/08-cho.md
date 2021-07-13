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

# Coupled Harmonic Oscillators Tutorial Sheet, Sheet #8

### Learning targets
* Write down the equations of motion for a system
* Rewrite equations of motion in matrix form
* Find eigenvalues to solve for mode shapes

### Additional Resources
* [AFP - Interactive coupled oscillators](https://fourier.space/assets/coupled.oscillator/index.html)
* [Introduction to Eigenfrequency Analysis](https://uk.comsol.com/multiphysics/eigenfrequency-analysis)

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.

<img src = "08-cho-media\figure3.PNG" width="20%" style = "margin: 10px auto 20px; display: block;">

(a) Write down the equations of motion of the masses $m_1=2m$ and $m_2=m$, considering the spring constants $k_1=k_2=k$ and locations of the two masses $x_1$ and $x_2$, which are both zero when the system is in static equilibrium.

<div class = "answer">
$\Rightarrow$ Even though the system is vertical, we can ignore the effects of gravity. This is because the equilibrium position of the above system already takes the effects of gravity into account (i.e. the masses only hang the way they do because gravity is already acting on them).

$\Rightarrow$ The equations of motion of the masses are:
$$2m\ddot{x}_1+2kx_1-kx_2= 0
\\\ 
m\ddot{x}_2-kx_1+kx_2= 0$$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(b) Express these equations in matrix form with separate vectors containing only displacements and accelerations and determine the characteristic frequencies and the corresponding mode shapes.

<div class = "answer">
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
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

------------------------------------------------------

## Exam Style Questions
### Problem 2.

The question above was fairly straightforward (not because it's easy, but because it only has 2 masses). Here, we will be dealing with four masses - please don't try to do this by hand. It'll be much easier to use MATLAB.
This is a clone of the 2020 exam question.

A one-dimensional system of 4 coupled harmonic oscillators of mass $m=6kg$ are connected in series by springs of stiffness $k=18N/m$ and to a wall at one end of the system but left unconstrained at the other end. 

(a) Write down an expression for the acceleration of the first oscillator in the form $\ddot{x}_1=Ax_1+Bx_2$.

<div class="answer">

$\Rightarrow$ The general form for the acceleration of the $n$th mass is:

$m_n\ddot{x}_n=-k_n(x_n-x_{(n-1)})-k_{(n+1)}(x_n-x_{(n+1)})$

$\Rightarrow$ We are interested in the first mass, so $n=1$. This also means that any $(n-1)$ terms are replaced with 0. We have:

$m_1\ddot{x}_1=-k_1(x_1-0)-k_{2}(x_1-x_{2})$

$m_1\ddot{x}_1=-k_1x_1-k_2x_1+k_2x_2$

$\ddot{x}_1=\frac{-2k}{m}x_1+\frac{k}{m}x_2$

$\ddot{x}_1=\frac{-2\times18}{6}x_1+\frac{18}{6}x_2$

$\boxed{\ddot{x}_1=-6x_1+3x_2}$, so $A=-6$ & $B=3$
</div>
<div class = "workingout"><br><br><br><br></div>

(b) Write down the matrix relating the positions to the accelerations of the four masses.
<div class="answer">
$\Rightarrow$ The first line of the matrix will come from the above formula:

$\begin{pmatrix}
-6 & 3 & 0 & 0\\
? & ? & ? & ?\\
? & ? & ? & ?\\
? & ? & ? & ?
\end{pmatrix}$

The next line can be found by constructing the equation for $\ddot{x}_2$, and so on - remembering either to construct the equations from first principals each time, or to apply the above general equation correctly: if spring or mass $n+1$ or $n-1$ does not exist, use 0 as its value.

$\boxed{
\begin{pmatrix}
-6 & 3 & 0 & 0\\
3 & -6 & 3 & 0\\
0 & 3 & -6 & 3\\
0 & 0 & 3 & -3
\end{pmatrix}x=\ddot{x}}$

</div>
<div class = "workingout"><br><br><br><br></div>

(c) How many natural frequencies does this system have?
<div class="answer">

This is a 4-mass system, so we would expect it to have four natural frequencies.

We can verify this very easily using MATLAB of Wolfram: the number of eigenvalues = the number of natural frequencies.

In MATLAB, type ```eigs[/matrix/]```, or in Wolfram just type something like ```eigenvalues /matrix/```.

MATLAB:
<img src = "08-cho-media\answer2c.PNG" width="80%" style = "margin: 10px auto 20px; display: block;">

(MATLAB tends to be easier and quicker for matrix operations than Wolfram, but both will work.)
</div>
<div class = "workingout"><br><br><br><br><br></div>

(d) Find the period of oscillation of the vibrational mode at which all the oscillators are out of phase with their immediate neighbours, to 1 significant figure. 
<div class="answer">
Again using MATLAB, we can find the eigenvectors & eigenvalues of the system:

```[vectors, values] = eigs(Matrix)```

<img src = "08-cho-media\answer2d1.PNG" width="50%" style = "margin: 10px auto 20px; display: block;">

We can see from the ```vectors``` that the eigen mode which satisfies the question is the 1st one, as each mass has a different sign to its neighbours.

From our knowledge of eigen analysis, we know that $\lambda=-\omega^2$, so to find $\omega$ from our eigenvalue, we have to take $\omega=\sqrt{-value}$.

<img src = "08-cho-media\answer2d2.PNG" width="50%" style = "margin: 10px auto 20px; display: block;">
In the above code, we take the first eigenvalue, which we have identified as the one we need, and use it to calculate the corresponding $\omega$.

$\Rightarrow \omega=3.2552$

We now need to convert this into a time period.

$\omega=\frac{2\pi}{t} \therefore t=\frac{2\pi}{\omega}=1.9302s$

$\Rightarrow \boxed{t=2s (1s.f.)}$
</div>
<div class = "workingout"><br><br><br><br><br></div>

(e) If a 5th similar spring were added to this system, connecting the final oscillator to another wall, what would you expect this to do to the resonant frequencies of the system? 
<div class="answer">
To answer this, we work out the last line of the stiffness matrix using this extra spring:

$\begin{pmatrix}
-6 & 3 & 0 & 0\\
3 & -6 & 3 & 0\\
0 & 3 & -6 & 3\\
0 & 0 & 3 & -6
\end{pmatrix}$

Then we repeat the MATLAB eigen analysis.
<img src = "08-cho-media\answer2e.PNG" width="20%" style = "margin: 10px auto 20px; display: block;">

We can see that the new eigenvalues are slightly larger than the old ones

$\Rightarrow \boxed{\text{The resonant frequencies all increase}}$
</div>
<div class = "workingout"><br><br><br><br><br></div>

### Problem 3.

A 16-coach train is rolling down a hill.

The coaches can be modelled as coupled harmonic oscillators, each with mass $m=6.5\times10^3kg$ and connected by springs with spring constant $k=300Nm$. Every 15 seconds, the train passes an electricity pylon next to the track. The aeodynamic effect of these pylons begin to cause the coaches of the train to oscillate. If this oscillation frequency matches any of the natural frequencies of the train, it will begin to resonate at higher and higher amplitudes and eventuallly break apart.

By calcuating the time periods of the natural frequencies of the system to the nearest second, decide if this wil be a problem.

Note: This will be a problem if the time period between pylons ($=15s$) = the time period of any of the natural frequencies.

<div class="answer">
The wording of this question makes it seem very complex, but all it is asking you to do is decide whether any of the natural time periods ($=\frac{1}{\text{natural frequency}}$) is 15 seconds, to the nearest integer.

To solve this, we will:
- Find the eigenvalues of the system
- Convert these to omega values
- Convert these to the natural time periods
- Check to see if any of the above = 15s.

We can construct a stiffness matrix for the train, as in previous questions. Note that there are no couplings at either end (the train is free to move).

$\begin{pmatrix}
-\frac{3}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
\frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65} & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac{3}{65} & -\frac{6}{65} & \frac{3}{65}\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 &\frac{3}{65} & -\frac{3}{65}\\
\end{pmatrix}$

The matrix is also huge, and therefore evil to type into MATLAB.
<img src = "08-cho-media\answer51.PNG" width="90%" style = "margin: 10px auto 20px; display: block;">

Then the omega values:
<img src = "08-cho-media\answer52.PNG" width="30%" style = "margin: 10px auto 20px; display: block;">

To find the natural lime periods, we use the fact that $\omega=\frac{2\pi}{t}$, so $t=\frac{2\pi}{\omega}$.
We have to use a ```.``` in the MATLAB code here, because we want it to perform the operation on each of the elements of the array, and not on the array as a whole.
<img src = "08-cho-media\answer53.PNG" width="30%" style = "margin: 10px auto 20px; display: block;">

This is frustrating, because it is displaying the array in standard form, in order to be able to display the last one. We need to know the integer values, not in standard form. In order to correct this, we need to use ```format shortG```:
<img src = "08-cho-media\answer54.PNG" width="30%" style = "margin: 10px auto 20px; display: block;">

We can now see that the first 3 of these times round to 15 seconds, to the nearest second. This means that the pylons are driving the oscillation of the train at it's natural frequency.

$\Rightarrow \boxed{\text{There will be a problem. The effect of the pylons will be to cause the train to resonate.}}$

*Incidentally, it was exactly this sort of resonance problem that caused the Tacoma Narrows bridge collapse ([video](https://www.youtube.com/watch?v=j-zczJXSxnw)).
</div>

<div class = "workingout"><br><br><br><br><br><br><br><br><br><br></div>

------------------------------------------------------
 ## Extension Question
 ### Problem 4.

The below is a stiffness matrix for a series of 3 masses connected to each other and a wall at each end by 4 springs.

$\begin{pmatrix}
-3 & 2 & 0\\
1 & -4 & 3\\
0 & 2 & -6
\end{pmatrix}$

(a) Calculate what each of the masses $m_1\rightarrow{}m_3$ and spring constants $k_2\rightarrow{}k_4$ must be, in terms of $k_1$

<div class="answer">
First, we have to construct an algebraic stiffness matrix for the system:

$\begin{pmatrix}
-\frac{k_1+k_2}{m_1} & \frac{k_2}{m_1} & 0\\
\frac{k_2}{m_2} & -\frac{k_2+k_3}{m_2} & \frac{k_3}{m_2}\\
0 & \frac{k_3}{m_3} & -\frac{k_3+k_4}{m_3}
\end{pmatrix}$

Then, we can equate this to the original stiffness matrix:

$\begin{pmatrix}
-\frac{k_1+k_2}{m_1} & \frac{k_2}{m_1} & 0\\
\frac{k_2}{m_2} & -\frac{k_2+k_3}{m_2} & \frac{k_3}{m_2}\\
0 & \frac{k_3}{m_3} & -\frac{k_3+k_4}{m_3}
\end{pmatrix}=\begin{pmatrix}
-3 & 2 & 0\\
1 & -4 & 3\\
0 & 2 & -6
\end{pmatrix}$

So, therefore:

$
\frac{k_1+k_2}{m_1}=3, \quad \frac{k_2}{m_1}=2\\
\frac{k_2}{m_2}=1, \quad \frac{k_2+k_3}{m_2}=4, \quad \frac{k_3}{m_2}=3\\
\frac{k_3}{m_3}=2, \quad \frac{k_3+k_4}{m_3}=6
$

Plugging these equations into Wolfram ([link](https://www.wolframalpha.com/input/?i=3%3D%28k_1%2Bk_2%29%2Fm_1%2C+2%3Dk_2%2Fm_1%2C+1%3Dk_2%2Fm_2%2C+4%3D%28k_2%2Bk_3%29%2Fm_2%2C+3%3Dk_3%2Fm_2%2C+2%3Dk_3%2Fm_3%2C+6%3D%28k_3%2Bk_4%29%2Fm_3)) gives us that:

$\Rightarrow \boxed{k_2=2k_1, k_3=6k_1, k_4=12k_1, m_1=k_1, m_2=2k_1, m_3=3k_1 \text{ where } k_1\not=0}$

Note that Wolfram can be a bit picky about simultaneous equations and that the above link may sometimes not work. Try typing it in yourself: ```(k_1 + k_2) / m_1 = 3, k_2 / m_1 = 2, etc...```
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(b) What integer-value of $k_1$ will yield the smallest natural frequency of the system?

<div class="answer">
This is an understanding-based trick question. The value of $k_1$ does not affect the stiffness matrix, so its eigenvalues (and thus the natural frequencies) are unaffected.
</div>

<div class = "workingout"><br><br></div>

(c) We connect mass $m_3$ to a wall using spring $k_4$, and ignore all other components of the original setup. Assuming a damping constant of $c=24$, and that this new oscillator is critically damped, use your knowledge of ODEs to find the value of $k_1$ and thus the values of all the springs and masses.

<div class="answer">
Once you have deciphered the words, this question is essentially revision of last week's topic.

For a critically damped oscillator, we know that the determinant is 0, i.e. $\sqrt{c^2-4\times{}m_3\times{}k_4}=0$.

$\therefore \sqrt{24^2-4\times3k_1\times12k_1}=0$

$\therefore 24^2=4\times3k_1\times12k_1$

$\therefore 576=144k_1^2$

$\therefore k_1^2=4$

$\Rightarrow \boxed{k_1=2Nm}$

From this, you can work out that $k_2=4$, $k_3=12$, $k_4=24$ and $m_1=2$, $m_2=4$, $m_3=6$.

</div>

<div class = "workingout"><br><br><br><br><br><br><br></div>

------------------------------------------------------

<br><br>

## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>
<br><br>
### For Printing
<button type="button" onclick="prepareForPrint('block')">Add whitespace</button>
<button type="button" onclick="prepareForPrint('none')">Remove whitespace</button>

<br><br>

# Next week, a test! :)