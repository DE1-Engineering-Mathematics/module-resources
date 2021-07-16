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

# Complex Numbers Tutorial Sheet, Sheet #6


### Learning targets
* Convert complex numbers from their Cartesian form to their Polar or exponential form
* Divide, multiply, add and subtract Complex numbers
* Manipulate complex numbers to find real and imaginary parts; find the absolute value and conjugate
* Plot complex numbers and an Argand diagram
* Understand and use de Moivres theorem

### Additional Resources
* [Welch Labs - Imaginary Numbers are Real](https://youtu.be/T647CGsuOVU)

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Express the flowing complex numbers in their polar form, $r(\cos\theta+\mathrm{i}\sin\theta)$ and exponential form, $re^{i\theta }$.

(a) $z=3+4\mathrm{i}$
<div class = "answer">

Find the $r$ (the magnitude of $z$): <br>
$r=\| z \|=\sqrt{3^2+4^2}=\sqrt{25}=5$ <br>

Find the argument $arg(z)$ (angle $\theta$): <br>

$\theta= \text{arg}(z) =\tan^{-1}(\frac{\text{imaginary part}}{\text{real part}})= \tan^{-1}(\frac{4}{3}) = 53.13^\circ$ <br>

<strong>Polar Form</strong><br>

$z=a+b\mathrm{i}=r(\cos\theta+\mathrm{i}\sin\theta)$ <br>

$\Rightarrow \boxed{\text{Therefore } z=5(\cos 53.13^\circ+\mathrm{i}\sin 53.13^\circ)}$ <br>

<strong>Exponential Form</strong><br>

$z = re^{i\theta }$ <br>

$\Rightarrow \boxed{\text{Therefore } 5e^{53.13^\circ i}}$

</div>

(b) $z=-3-\mathrm{i}$
<div class = "answer"> 
$r=|z|=\sqrt{(-3)^2+(-1)^2}=\sqrt{10}=3.16$ <br>

Plot $z$ on an Argand diagram: 

<img src = "06-complex-numbers-media\figure1.png" width="50%"> <br>

$\alpha=\tan^{-1}(\frac{-1}{-3})=\tan^{-1}(\frac{1}{3})=18.43^\circ$
        
As a result, $arg(z) = \theta = 18.43^\circ + 180^\circ = 198.43^\circ$ <br>

<strong>Polar Form</strong><br>

$z=a+b\mathrm{i}=r(\cos\theta+\mathrm{i}\sin\theta)$ <br>

$\Rightarrow \boxed{\text{Therefore } z= 3.16(\cos198.43^\circ+\mathrm{i}\sin198.43^\circ)}$ 

Alternative answer: $z= 3.16(\cos(-161.57^\circ)+\mathrm{i}\sin(-161.57^\circ))$ <br>

<strong>Exponential Form</strong><br>

$z = re^{i\theta }$ <br>

$\Rightarrow \boxed{\text{Therefore } 3.16e^{198.43^\circ i}}$

</div>


(c) $z=-\mathrm{i}$
<div class = "answer">
$r=|z|=\sqrt{(0)^2+(-1)^2}=\sqrt{1}=1$ <br>
        
Find the argument $arg(z)$ (angle $\theta$):

$\theta=\mathrm{arg}(z)=\tan^{-1}(\frac{-1}{0})+180^\circ=\tan^{-1}(\infty)+180^\circ=90^\circ+180^\circ=270^\circ $ <br>

<strong>Polar Form</strong><br>

$z=a+b\mathrm{i}=r(\cos\theta+\mathrm{i}\sin\theta)$ <br>

$\Rightarrow \boxed{\text{Therefore }z=1(\cos270^\circ+\mathrm{i}\sin270^\circ)}$ 

Alternative answer: $z=1(\cos-90^\circ+\mathrm{i}\sin-90^\circ)$ <br>

<strong>Exponential Form</strong><br>

$z = re^{i\theta }$ <br>

$\Rightarrow \boxed{\text{Therefore } e^{270^\circ i}}$
</div>

(d) $z=3-4\mathrm{i}$
<div class = "answer">
$r=|z|=\sqrt{(3)^2+(4)^2}=\sqrt{25}=5$ <br>

Plot $z$ on an Argand diagram: <br>

<img src = "06-complex-numbers-media\figure1d.png" width="50%"> <br>

$\alpha = \tan^{-1}(\frac{4}{3})=53.13$ <br>
$\theta=\mathrm{arg}(z)=360^\circ-53.13^\circ=306.87^\circ$ <br>

<strong>Polar Form</strong><br>

$z=a+b\mathrm{i}=r(\cos\theta+\mathrm{i}\sin\theta)$ <br>

$\Rightarrow \boxed{\text{Therefore } z= 5(\cos306.87^\circ+\mathrm{i}\sin306.87^\circ)}$

Alternative answer: $z=5(\cos-53.13^\circ+\mathrm{i}\sin-53.13^\circ)$ <br>

<strong>Exponential Form</strong><br>

$z = re^{i\theta }$ <br>

$\Rightarrow \boxed{\text{Therefore } 5e^{306.87^\circ i}}$

</div>

<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 2.
Consider the complex numbers $z_1=2+4\mathrm{i}$ and $z_2=4-7\mathrm{i}$.

(a)  Find $z_1+z_2$
<div class = "answer">
Collect real and complex terms: <br>
$ z_1+z_2=(2+4\mathrm{i})+(4-7\mathrm{i})=(2+4)+(4-7)\mathrm{i}=\boxed{6-3\mathrm{i}}$</div>

(b) Find $z_1-z_2$
<div class = "answer">$z_1-z_2=(2+4\mathrm{i})-(4-7\mathrm{i})=(2-4)+(4+7)\mathrm{i}=\boxed{-2+11\mathrm{i}}$</div>

(c) Find $z_1z_2$
<div class = "answer">
Expand the brackets: <br>
$z_1z_2=(2+4\mathrm{i})(4-7\mathrm{i})=2\times4-2\times7\mathrm{i}+4\times4\mathrm{i}-4\times7\mathrm{i^2}$ <br>

Collect real and complex terms: 
$8-14\mathrm{i}+16\mathrm{i}+28= \boxed{36+2\mathrm{i}}$
</div>

(d) Find $\frac{z_1}{z_2}$
<div class = "answer">
$ \frac{z_1}{z_2}=\frac{2+4\mathrm{i}}{4-7\mathrm{i}}=\frac{2+4\mathrm{i}}{4-7\mathrm{i}}\cdot\frac{4+7\mathrm{i}}{4+7\mathrm{i}}=\frac{8+16\mathrm{i}+14\mathrm{i}-28}{16+49}=\frac{-20+30\mathrm{i}}{65}=\boxed{-\frac{4}{13}+\frac{6}{13}\mathrm{i}}$ <br>
        
Note: <br>
Simplify a complex fraction $\frac{a+b\mathrm{i}}{c+d\mathrm{i}}$ by rationalizing the denominator - multiplying the fraction with the complex conjugate of the denominator over itself (effectively multiplying by $1$), i.e.,
$\frac{a+b\mathrm{i}}{c+d\mathrm{i}}\cdot\frac{c-d\mathrm{i}}{c-d\mathrm{i}}$
</div>

<div class = "workingout"><br><br><br><br><br><br><br><br></div>

---------------------------------------------------------------------------------

### Problem 3.

(a)  Find the real and imaginary part of $z = \frac{\mathrm{i}-4}{2\mathrm{i}-3}$
<div class = "answer">Simplify and collect real and complex terms: <br>
$z=\frac{\mathrm{i}-4}{2\mathrm{i}-3}=\frac{\mathrm{i}-4}{2\mathrm{i}-3}\cdot\frac{2\mathrm{i}+3}{2\mathrm{i}+3}=\frac{-12-2+3\mathrm{i}-8\mathrm{i}}{-4-9}=\frac{14}{13}+\frac{5}{13}\mathrm{i}$. <br>

Therefore, $\boxed{\mathrm{Re}(z)=\frac{14}{13}}$ and $\boxed{\mathrm{Im}(z)=\frac{5}{13}}$
</div>

(b) Find the absolute value and the conjugate of $z = (1+\mathrm{i})^6$
<div class = "answer">
Express $z$ in polar form:
$z=(1+\mathrm{i})^6=\sqrt{2}(\cos\frac{\pi}{4}+\mathrm{i}\sin\frac{\pi}{4})^6$ <br>

Using De Moivre's Theorem: 
$\sqrt{2}(\cos\frac{\pi}{4}+\mathrm{i}\sin\frac{\pi}{4})^6=8(\cos\frac{3\pi}{2}+\mathrm{i}\sin\frac{3\pi}{2})=-8i$ <br>

Hence, $\boxed{|z|=8 \text{ and } \overline{z}=8\mathrm{i}}$
</div>

(c) Find the absolute value and the conjugate of $w = \mathrm{i}^{17}$
<div class = "answer">
Considering $\mathrm{i}^{4} = 1$ 

$w = \mathrm{i}^{17}=\mathrm{i}\cdot\mathrm{i}^{16}=\mathrm{i}\cdot\mathrm{(i^{4})}^{4}=\mathrm{i}\cdot(1)^4=\mathrm{i}.$ 

Hence, $\boxed{\| w \|=1 \text{ and } \overline{w}=-\mathrm{i}}$
</div>

(d) Simplify the complex number $\frac{1+\mathrm{i}}{1-\mathrm{i}}-(1+2\mathrm{i})(2+2\mathrm{i})+\frac{3-\mathrm{i}}{1+\mathrm{i}}$
<div class = "answer">
Evaluate each part: <br>
$\frac{1+\mathrm{i}}{1-\mathrm{i}}=\frac{1+\mathrm{i}}{1-\mathrm{i}}\cdot\frac{1+\mathrm{i}}{1+\mathrm{i}} = \frac{1-i^{2}+2\mathrm{i}}{2}=\mathrm{i}$ 

$-(1+2\mathrm{i})(2+2\mathrm{i})=2-6\mathrm{i}$

$\frac{3-\mathrm{i}}{1+\mathrm{i}}=\frac{3-\mathrm{i}}{1+\mathrm{i}}\cdot\frac{1-\mathrm{i}}{1-\mathrm{i}}=\frac{3+\mathrm{i}^2-3\mathrm{i}-\mathrm{i}}{1-\mathrm{i}^2}=1-2\mathrm{i}$ <br>

Therefore: <br>
$\frac{1+\mathrm{i}}{1-\mathrm{i}}-(1+2\mathrm{i})(2+2\mathrm{i})+\frac{3-\mathrm{i}}{1+\mathrm{i}}=\mathrm{i}+2-6\mathrm{i}+1-2\mathrm{i}=\boxed{3-7\mathrm{i}}$
</div>

(e) Simplify the complex number $2\mathrm{i}(\mathrm{i}-1)+(\sqrt{3}-\mathrm{i})^3+(1+\mathrm{i})(1-\mathrm{i})$
<div class = "answer">
Expand the brackets and evaluate: 
$2\mathrm{i}(\mathrm{i}-1)+(\sqrt{3}-\mathrm{i})^3+(1+\mathrm{i})(1-\mathrm{i})\\=2\mathrm{i}^2-2\mathrm{i}+3\sqrt{3}-3\mathrm{i}(\sqrt{3})^{2}+3\mathrm{i}^{2}\sqrt{3}+(-\mathrm{i})^{3}+1-\mathrm{i}^{2}$
$=-2-2\mathrm{i}+3\sqrt{3}-3\sqrt{3}-8\mathrm{i}+2=\boxed{-10\mathrm{i}}$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 4.
Plot the flowing complex numbers on an Argand diagram: 

(a) $z=3+2\mathrm{i}$
<div class = "answer">
<img src = "06-complex-numbers-media\figure2.PNG" width = "50%">
</div>

(b) $z=4-5\mathrm{i}$
<div class = "answer">
<img src = "06-complex-numbers-media\figure3.PNG" width = "50%">
</div>

(c) $z=-2-\mathrm{i}$
<div class = "answer">
<img src = "06-complex-numbers-media\figure4.PNG" width = "50%">
</div>

(d)  $\| z \|=3$
<div class = "answer">
$\Rightarrow$ On an Argand diagram, plot the locus defined by $\| z \|=3$.

$z=x+\mathrm{i}y$ <br>
$|z|=|x+\mathrm{i}y|=3$

$\sqrt{x^2+y^2}=3$

$\Rightarrow$ Therefore: $x^2+y^2=9$
The solution ($x^2+y^2=9$) consists of all the points lying on the circle of radius 3 with center (0,0). <br>

<img src = "06-complex-numbers-media\figure5.PNG" width = "50%">
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 5.
Write the following complex number in polar and exponential forms

$z=\frac{1}{2}-\frac{\sqrt{3}}{2}\mathrm{i}$

<div class = "answer">

$\| z \|=\sqrt{(\frac{1}{2})^2+(\frac{\sqrt{3}}{2})^2}=\sqrt{\frac{1}{4}+\frac{3}{4}}=1$. 

Plot $z$ on an Argand diagram <br>
<img src = "06-complex-numbers-media\figure6.PNG" width = "50%"> <br>
$\theta=\tan^{-1}(\sqrt{3})=\frac{\pi}{3}$ 

Therefore $\mathrm{arg}(z)=-\frac{\pi}{3}$ or alternatively: $\mathrm{arg}(z)=\frac{5\pi}{3}$ <br>

Complex number $z$ in polar form: <br>
$z=\cos\frac{-\pi}{3}+\mathrm{i}\sin\frac{-\pi}{3}=\boxed{\cos\frac{\pi}{3}-\mathrm{i}\sin\frac{\pi}{3}}$
or: $\cos\frac{5\pi}{3}+\mathrm{i}\sin\frac{5\pi}{3}$

In exponential form:
$\boxed{e^{-\frac{\pi}{3}\mathrm{i}}}$ or: $e^{\frac{5\pi}{3}\mathrm{i}}$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 6.
Application of de Moivre’s theorem.

(a) Find $(\cos\theta+\mathrm{i}\sin\theta)^{-10}$ in the form $(\cos(A\theta)-\mathrm{i}\sin(B\theta))$
<div class = "answer">
Using de Moivre’s theorem:
$(\cos\theta+\mathrm{i}\sin\theta)^{-10}=(\cos(-10\theta)+\mathrm{i}\sin(-10\theta))=\boxed{(\cos(10\theta)-\mathrm{i}\sin(10\theta))}$
</div>

(b) Simplify the flowing expression: $\frac{\cos2\theta+\mathrm{i}\sin2\theta}{\cos3\theta+\mathrm{i}\sin3\theta}$
<div class = "answer">Using de Moivre’s theorem:

$\frac{\cos2\theta+\mathrm{i}\sin2\theta}{\cos3\theta+\mathrm{i}\sin3\theta}$ <br>
$=\frac{(\cos\theta+\mathrm{i}\sin\theta)^2}{(\cos\theta+\mathrm{i}\sin\theta)^3}$ .
$\frac{(\cos\theta+\mathrm{i}\sin\theta)^2}{(\cos\theta+\mathrm{i}\sin\theta)^3}$ <br>
$=\frac{(\cos\theta+\mathrm{i}\sin\theta)^2}{(\cos\theta+\mathrm{i}\sin\theta)^2(\cos\theta+\mathrm{i}\sin\theta)}$ <br>
$=\frac{1}{\cos\theta+\mathrm{i}\sin\theta}(\frac{\cos\theta-\mathrm{i}\sin\theta}{\cos\theta-\mathrm{i}\sin\theta})$ <br>
$=\boxed{\cos\theta-\mathrm{i}\sin\theta}$
</div>

(c) Prove that $\cos3\theta = \cos^3\theta-3\cos\theta\sin^2\theta$
<div class = "answer">
Consider the complex number $\cos3\theta+\mathrm{i}\sin3\theta$

By de Moivre’s theorem:

$\cos3\theta+\mathrm{i}\sin3\theta =(\cos\theta+\mathrm{i}\sin\theta)^3 $ <br>
$=\cos^3\theta+3\cos^2\theta(\mathrm{i}\sin\theta)+3\cos\theta(\mathrm{i}\sin\theta)^2+(\mathrm{i}\sin\theta)^3$ . $\cos^3\theta+3\mathrm{i}\cos^2\theta\sin\theta-3\cos\theta\sin^2\theta-\mathrm{i}\sin^3\theta $ <br>
$=\cos^3\theta-3\cos\theta\sin^2\theta+\mathrm{i}(3\cos^2\theta\sin\theta-\sin^3\theta) $ <br>

Comparing real parts of each side of the equation above, you obtain:
$$\boxed{\cos3\theta = \cos^3\theta-3\cos\theta\sin^2\theta}$$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

## Exam Style Questions
### Problem 7.

(a) Write down the modulus and argument of the complex number $4-4\mathrm{i}$. 

<div class = "answer">

$\|4-4\mathrm{i}\|=\sqrt{(4^2+(-4)^2)}=\boxed{4\sqrt{2}}$

Plotting $z^5$ on an Argand diagram:

<img src = "06-complex-numbers-media\figure7.PNG" width = "50%"> <br>

From the Argand diagram above:
$\mathrm{arg}(4-4\mathrm{i})=arctan(\frac{-4}{4})$ <br>
$\Rightarrow\boxed{-\frac{\pi}{4}}$ alternatively, $\boxed{\frac{7\pi}{4}}$

</div>

(b) Solve the equation $z^5 = 4-4\mathrm{i}$, expressing your answers in the exponential form.

<div class = "answer">

<strong>Method 1</strong> <br>
Rewrite the argument for the complex number, $4-4\mathrm{i}$, in its exponential form: $4\sqrt{2}e^{i\frac{7\pi}{4}}$ <br>

According to De Moivre's theorem: <br>

$z^n$ = $(re^{i\theta})^n$ = $r^n e^{in\theta}$ <br>

As the value is $z^5$, n = 5. <br>

$\sqrt[5]{4\sqrt{2}}$ = $\sqrt{2}$ <br>

$\frac{7\pi}{4}$ / 5 = $\frac{7\pi}{20}$ <br>

There will be 5 solutions before the angle 'repeats'. <br>

Adding/subtracting $\frac{2\pi}{5}$ from $\frac{7\pi}{20}$ = ${\frac{-17\pi}{20}, \frac{-9\pi}{20}, \frac{-\pi}{20}, \frac{7\pi}{20}, \frac{15\pi}{20}}$ <br>

Putting it together, solutions in the exponential are: 
$\boxed{z_1=\sqrt{2}e^{\frac{-17\pi}{20}i}}$, $\boxed{z_2=\sqrt{2}e^{\frac{-9\pi}{20}i}}$, $\boxed{z_3=\sqrt{2}e^{\frac{-\pi}{20}i}}$, $\boxed{z_4=\sqrt{2}e^{\frac{7\pi}{20}i}}$, and $\boxed{z_5=\sqrt{2}e^{\frac{3\pi}{4}i}}$ <br><br>

<strong>Method 2</strong> <br>

Rewrite the argument for the complex number, $4-4\mathrm{i}$, in its general form: $2n\pi-\frac{\pi}{4}$, where n is an integer.
Note: For any integer n, $\cos(2n\pi-\frac{\pi}{4})=\cos(-\frac{\pi}{4})$. Likewise for $\sin(-\frac{\pi}{4})$.
<br>

Now, $z^5=\cos(2\pi-\frac{\pi}{4})+\mathrm{i}\sin(2\pi-\frac{\pi}{4})$
<br>
Model the solutions, $z_n$, to $z^5=4-4\mathrm{i}$ as complex numbers in polar form, i.e.:
$z_n=r(\cos\theta+\mathrm{i}\sin\theta)$
<br>

If $z_n=r(\cos\theta+\mathrm{i}\sin\theta)$, then by de Moivres theorem: $z^{5}=r^{5}(\cos5\theta+\mathrm{i}\sin5\theta)$
$=4\sqrt{2}(\cos\frac{\pi}{4}-\mathrm{i}\sin\frac{\pi}{4})$
<br>

Compare magnitudes:
$r^5=4\sqrt{2}, r=\sqrt{2}$
<br>

Compare arguments:
$5\theta=2n\pi-\frac{\pi}{4}, \theta=(8n-1)\frac{\pi}{20}$
<br>

For appropriate values of n, so that $\theta$ lies between $-\pi$ and $\pi$:

$$n=-2\quad\Rightarrow\quad\theta=\frac{-17\pi}{20}$$
$$n=-1\quad\Rightarrow\quad\theta=\frac{-9\pi}{20}$$
$$n=0\quad\Rightarrow\quad\theta=\frac{-\pi}{20}$$
$$n=1\quad\Rightarrow\quad\theta=\frac{7\pi}{20}$$
$$n=2\quad\Rightarrow\quad\theta=\frac{15\pi}{20} \text{ or } \frac{3\pi}{4}$$

Therefore solutions in exponential are: 
$\boxed{z_1=\sqrt{2}e^{\frac{-17\pi}{20}i}}$, $\boxed{z_2=\sqrt{2}e^{\frac{-9\pi}{20}i}}$, $\boxed{z_3=\sqrt{2}e^{\frac{-\pi}{20}i}}$, $\boxed{z_4=\sqrt{2}e^{\frac{7\pi}{20}i}}$, and $\boxed{z_5=\sqrt{2}e^{\frac{3\pi}{4}i}}$

</div>

(c) State the solution, to part (b), with the smallest positive argument and find the real part of it (in polar form).
<div class = "answer">
Solution with the smallest positive argument: $\sqrt{2}e^{\frac{7\pi}{20}i}$ <br>

$\boxed{Re({\sqrt{2}e^{\frac{7\pi}{20}i})} =\sqrt{2}\cos\left(\frac{7\pi}{20}\right)}$
</div>

<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 8.
Find the value of $x$ and $y$ in the equation $(x+iy)(3+4i) =  3-4i$ given that $x \in \mathbb{R}$ and $y\in \mathbb{R}$. 

<div class = "answer">
$x+iy = \frac{3-4i}{3+4i}$ <br>
=$\frac{(3-4i)(3-4i)}{(3+4i)(3-4i)}$<br>
=$\frac{9-12i-12i-16i^2}{9-12i-12i+16i^2}$<br>
=$\frac{-7-24i}{25}$<br>

Therefore $\boxed{x = \frac{-7}{25}}$ and $\boxed{y = \frac{-24}{25}}$ 
</div>

<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 9.
It is given that $z = \frac{1+8i}{1-2i}$. Show that $arctan(8) + arctan(2) + arctan(\frac{2}{3}) = \pi$.

<div class = "answer">

Express $z$ in the form $x+iy$ where $x$ and $y$ are real numbers.

$x+iy = \frac{1+8i}{1-2i}$ <br>
=$\frac{(1+8i)(1+2i)}{(1-2i)(1+2i)}$ <br>
=$\frac{1+2i+8i-16}{1+4}$ <br>
=$\frac{-15+10i}{5}$ <br>
=$-3+2i$ <br>

$arg(\frac{1+8i}{1-2i})$ = $arg(-3+2i)$ <br>
$arg(1+8i)-arg(1-2i)$ = $arg(-3+2i)$ <br>
$arctan(\frac{8}{1}) - arctan(\frac{-2}{1}) = \pi - arctan(\frac{2}{3})$ <br>
$arctan(8) + arctan(2) = \pi - arctan(\frac{2}{3})$ <br>
$arctan(8) + arctan(2) + arctan(\frac{2}{3}) = \pi $  <br>



</div>

<div class = "workingout"><br><br><br><br><br><br><br><br></div>


## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">Hide all answers</button>
<br><br>
### For Printing
<button type="button" onclick="prepareForPrint('block')">Add whitespace</button>
<button type="button" onclick="prepareForPrint('none')">Remove whitespace</button>

<br><br>

# Next week, ODEs!