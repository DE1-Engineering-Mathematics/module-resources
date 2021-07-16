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

# Partial Differential Equations Tutorial Sheet, # 12

### Learning Targets
 * Evaluate and manipulate Partial Differentials
 * Understand how partial differentials work on vector fields
 * Use separation of variables solution to solve a PDE

### Additional resources
* [PDE intro video](https://youtu.be/PTvvoVLzVCE)

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Which of the following are solutions to Laplace's equation,
$\nabla^2 f(\mathbf{x}) = 0$?
For those that are not, can you come up with a differential equation involving the Laplacian, $\nabla^2$, that $f(\mathbf{x})$ is a solution of?

(a) $e^{-y} \sin x $
<div class = "answer">
Yes, $\nabla^2 f(\mathbf{x}) = 0$ <br>


$\Rightarrow{}\quad$ The Laplacian operator is defined as: <br>

$\Rightarrow{}\nabla^2= \frac{\partial^2 } {\partial x^2}+  \frac{\partial^2} {\partial y^2} + \frac{\partial^2} {\partial z^2}$<br>

$\Rightarrow{}\nabla^2 f(\mathbf{x}) =  \frac{\partial^2 }{\partial x^2}{e^{-y} \sin x} +  \frac{\partial^2}{\partial y^2}{e^{-y} \sin x}$<br>

$\Rightarrow{} =  \frac{\partial }{\partial x}{e^{-y} \cos x} -  \frac{\partial}{\partial y}{e^{-y} \sin x}$<br>

$\Rightarrow{} = {e^{-y} \sin x - e^{-y} \sin x} = 0$<br>

NB This is an example for this kind problem in case you get confused by these short answers :) <br>
</div>

(b) $\sin\left(\frac{x+y}{2}\right)\sin\left(\frac{x-y}{2}\right)$
<div class = "answer">
No, but $\nabla^2 f(\mathbf{x}) + f = 0$
</div>

(c) $f(x + i y)$
<div class = "answer">
Yes, $\nabla^2 f(x + i y) = 0$, this becomes a useful result in complex analysis.
</div>

(d) $4 \arctan(y/x) + \log(x^2 +y^2)$
<div class = "answer">
Yes, $\nabla^2 f(\mathbf{x}) = 0$
</div>

(e) $\frac{x+y}{z}$
<div class = "answer">
No, but $\nabla^2 f(\mathbf{x}) = 2 f / z^2$ would work.
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 2.
Show that the function $u\left(x,y\right)=\ln⁡(1+xy^2)$ satisfies the partial differential equation:

$$
2 \frac{\partial{} ^2u}{ \partial{} x^2} + 
y^3 \frac{ \partial{} ^2u }{ \partial{} y \partial{} x }
= 0
$$

<div class = "answer">
$$
\frac{\partial{}u}{\partial{}x}=\frac{y^2}{1+xy^2}\ ;\ \ \
\frac{ {\partial{}}^2u}{ {\partial{}x}^2}=-\frac{y^2}{ {\left(1+{xy}^2\right)}^2}.y^2=\frac{-y^4}{ {\left(1+{xy}^2\right)}^2}
$$
<br>

$$
\frac{ {\partial{}}^2u}{\partial{}y\partial{}x}=\frac{\partial{}}{\partial{}y}\left(\frac{\partial{}u}{\partial{}x}\right)=\frac{2y\left(1+xy^2\right)-y^2(2xy)}{ {(1+xy^2)}^2}=\frac{2y+2xy^3-2xy^3}{ { {(1+xy}^2)}^2}=\frac{2y}{ { {(1+xy}^2)}^2}
$$
<br>

$$
2\frac{ {\partial{}}^2u}{\partial{}x^2}+y^3\frac{ {\partial{}}^2u}{\partial{}y\partial{}x}=-\frac{2y^4}{ { {(1+xy}^2)}^2}+\frac{ {2y}^4}{ { {(1+xy}^2)}^2}=0
$$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------------------------------------------------------

<br>

# Exam Style Question
### Problem 3.
Vibrations on a guitar string can be modelled by the wave equation,
$\frac{\partial ^{2}u}{\partial t^{2}}-\frac{\tau\partial ^{2}u}{\rho \partial x^{2}}=0$
<br>where $u(x,t)$  is the displacement of the string from its equilibrium position, 𝜏 is its tension, and 𝜌 is the linear density of the string.
<br><br>
(a) Use separation of variables to produce linear ODEs for the separated parts.
State any relationship between constants you define.
<br><br>
<div class = "answer">
$\Rightarrow{}$ Using $𝑢(𝑥,𝑡)=𝑋(𝑥)𝑇(𝑡)$, the PDE becomes<br><br>
$X\left ( x \right )T{}''\left ( t \right )-\frac{\tau }{\rho }X{}''\left ( x \right )T\left ( t \right )=0$
<br><br>
$\Rightarrow{}$ And therefore   $\frac{T{}''\left ( t \right )}{T\left ( t \right )}-\frac{\tau }{\rho }\frac{X{}''\left ( x \right )}{X\left ( x \right )}=0$
<br><br>$\Rightarrow{}$Extract ODEs,
$\frac{T{}''\left ( t \right )}{T\left ( t \right )}=-\omega ^{2},\frac{X{}''\left ( x \right )}{X\left ( x \right )}=-k^{2}$
<br><br>
$\Rightarrow{}$Then,$\boxed{T{}''\left ( t \right )=-\omega ^{2}T\left ( t \right ),X{}''\left ( x \right )=-k^{2}X\left ( x \right )}$, with $\boxed{\omega ^{2}=\frac{\tau }{\rho }k^{2}}$
<br><br>
</div>
(b) Solve the ODEs in terms of sinusoidal solutions.
<br><br>
<div class = "answer">
$\boxed{𝑇(𝑡)=cos𝜔𝑡,sin𝜔𝑡}$ and
<br><br>
$\boxed{𝑋(𝑥)=cos𝑘𝑥,sin𝑘𝑥}$
<br><br>
Accept complex exponentials, accept equivalent correct forms, accept sum with coefficients, A cos + B sin etc.
<br><br>
</div>
(c)The string has a length 𝐿, and is fixed at both ends, such that $𝑢(𝑥 = 0, 𝑡) = 𝑢(𝑥 = 𝐿, 𝑡) = 0$. How does this constrain your solutions? Write a general solution of the PDE, $ 𝑢(𝑥, 𝑡)$, that is subject to these constraints.
<br><br>
<div class = "answer">
Fixed at $𝑥=0$ constrains to $sin𝑘𝑥$ spatial solutions only.
<br><br>
Fixed at $𝑥=𝐿$ constrains to $k=\frac{n\pi }{L}$.
<br><br>
$\boxed{u\left ( x,t \right )=\left ( A\cos\omega t+B\sin\omega t \right )sin\frac{n\pi x}{L}}$
<br><br>
</div>
(d)Write an expression for the fundamental (lowest) frequency allowed by the string.
<br><br>
<div class = "answer">
Using $\omega ^{2}=\frac{\tau }{\rho }k^{2}$ and $k=\frac{n\pi }{L}$, then $\omega =\sqrt{\frac{\tau }{\rho }}\frac{n\pi }{L}$
<br><br>
Fundamental frequency, set $𝑛=1$.
<br><br>
$\boxed{\omega =\sqrt{\frac{\tau }{\rho }}\frac{\pi }{L}}$
<br><br>
</div>
(e)If a guitar has a neck length of 0.65 m, and a string has linear density 5 g/m, what tension does the string need to be to sound an A note at a frequency $𝜔 = 2𝜋 × 110$ Hz?
<br><br>
<div class = "answer">Rearrange for 𝜏.
<br><br>
$\Rightarrow{}\tau =\frac{L^{2}\omega ^{2}}{\pi ^{2}}\rho $
<br><br>
Insert given values, $\Rightarrow{}\tau =\frac{\left ( 0.65m \right )^{2}\left ( 2\pi \times 110Hz \right )^{2}}{\pi ^{2}}0.005\frac{kg}{m}$
<br><br>
$\boxed{\tau =102N}$
<br><br>
</div>


## Challenging Questions
### Problem 4.

Prove for the 1D diffusion equation,
$\frac{ \partial f(x,t)}{ \partial t} = \alpha \frac{ \partial^2 f(x,t)}{\partial x^2}$,
that the total area under the curve $f(x,t)$ does not change over time.
(You may assume that $\frac{ \partial f(x,t)}{ \partial x} \rightarrow 0$ for $x \rightarrow \pm\infty$).

<div class = "answer">
The area under the curve is calculated by integrating $f(x,t)$ over all x.
Integrating both sides of the PDE,


$$
\int_{-\infty}^{\infty} \mathrm{d}x \; \frac{ \partial {f(x,t)}}{ \partial t} = \int_{-\infty}^{\infty} \mathrm{d}x \; \alpha \frac{\partial f(x,t)}{\partial x}
$$

$\Rightarrow{}$ We can swap the order of differentiation and integration on the LHS and directly integrate the expression on the RHS,

$$
\frac{\partial}{\partial t} \int_{-\infty}^{\infty} \mathrm{d}x \; f(x,t) =
\alpha \left.\frac{ \partial f(x,t)}{ \partial x}\right| _ {x\rightarrow \infty} - \left.\alpha \frac{ \partial f(x,t)}{ \partial x}\right|_{x\rightarrow -\infty}
$$

$\Rightarrow{}$ The x derivatives go to zero at infinity

$$
\boxed{ \frac{\partial}{ \partial t} \int_{-\infty}^{\infty} \mathrm{d}x \; f(x,t) = 0 }
$$

$\Rightarrow{}$ Therefore the area under the concentration curve does not change in time.

The area will be proportional to the numbers of ions or molecules etc. the total number of these will stay the same as they diffuse within the space.
The area taken over a region of the space will be proportional to the number of particles in that region.
</div>


<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------

### Problem 5.

Solve the 3D wave equation by separation of variables to show,
$u(\mathbf{x}, t) = \exp(i\mathbf{k}\cdot\mathbf{x} - i \omega t)$,
is a solution. With $\mathbf{k} = (k_x, k_y, k_z)^T$
What is the resulting relationship between $\mathbf{k}$ and $\omega$?
$$
\frac{n^2}{c^2}\frac{\partial^2 u(\mathbf{x}, t)}{\partial t^2} - \nabla^2 u(\mathbf{x}, t) = 0
$$

<div class = "answer">
<b>NB:</b>   Coordinate vector $\mathbf{x} = (x,y,z)$ and, $u(\mathbf{x}) = (u(x),v(x),w(x))^T$ is a vector field.  <br><br>
    
$\Rightarrow{}$ Start with a separation of variables solution, let $u(\mathbf{x}, t) = X(x)Y(y)Z(z)T(t)$.
then,

\begin{align*}\frac{n^2}{c^2}{T''(t)}{X(x)Y(y)Z(z)} -X''(x)Y(y)Z(z)T(t) - Y''(y)X(x)Z(z)T(t)) - Z''(z)X(x)Y(y)T(t) = 0 \end{align*}
\begin{align*}
\frac{n^2}{c^2}\frac{T''(t)}{T(t)} - \frac{X''(x)}{X(x)} - \frac{Y''(y)}{Y(y)} - \frac{Z''(z)}{Z(z)} = 0
\end{align*}

$\Rightarrow{}$ There is some freedom of choice as to how you define the constants here.
In order to match to the test solution, $u(\mathbf{x}, t) = \exp(i\mathbf{k}\cdot\mathbf{x} - i \omega t)$,
the most straightforward choice is,

\begin{align*}
\frac{T''(t)}{T(t)} = -\omega^2 \quad
\frac{X''(x)}{X(x)} = -k_x^2 \quad
\frac{Y''(y)}{Y(y)} = -k_y^2 \quad
\frac{Z''(z)}{Z(z)} = -k_z^2 \space .
\end{align*}

$\Rightarrow{}$  But here we'll solve as if we assumed arbitrary constants instead,

\begin{align*}
\frac{T''(t)}{T(t)} = a \quad
\frac{X''(x)}{X(x)} = b \quad
\frac{Y''(y)}{Y(y)} = c \quad
\frac{Z''(z)}{Z(z)} = d \space .
\end{align*}

$\Rightarrow{}$ With $\frac{n^2}{c^2} a - b - c - d = 0$.
Solving the ODEs, we get,

\begin{align*}
T(t) &= A_+ e^{+ \sqrt{a} t} + A_- e^{- \sqrt{a} t}
\newline
X(x) &= B_+ e^{+ \sqrt{b} x} + B_- e^{- \sqrt{b} t}
\end{align*}

$\Rightarrow{}$ And equivalently for $Y(y)$ and $Z(z)$.
To match with our test solution,

$u(\mathbf{x}, t) = \exp(i\mathbf{k}\cdot\mathbf{x} - i \omega t)$, We'll keep the negative exponential from the $T(t)$ function,
and the positive exponentials from the spatial functions.
This allow us to build the solution,

$u(\mathbf{x}, t) \propto \exp(\sqrt{b} x + \sqrt{c} y + \sqrt{d} z - \sqrt{a} t)$,
Matching coefficients requires,}

$$
\sqrt{a} = i \omega \quad
\sqrt{b} = i k_x \quad
\sqrt{c} = i k_y \quad
\sqrt{d} = i k_z \quad .
$$

$\Rightarrow{}$ Which gives,
$u(\mathbf{x}, t) \propto \exp(i k_x x + i k_y y + i k_z z - i \omega t)$,
or $\exp(i\mathbf{k}\cdot\mathbf{x} - i \omega t)$.
and a dispersion relations,}

$$
\boxed{ \frac{n^2}{c^2} \omega^2 = k_x^2 + k_y^2 + k_z^2 }
$$

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>


-----------------------------------------------------------------------------------

### Problem 6.
Show that a Gaussian function,
$f(x,t) = \frac{1}{\sigma(t)\sqrt{2\pi}} \exp\left( -\frac{x^2}{2\sigma(t)^2} \right)$
, solves the 1D diffusion equation, on the condition that
$\sigma(t) = \sqrt{\sigma(0)^2 + 2 \alpha t}$.


<div class = "answer">
This is a show-that question, so you need only show it satisfies the equation, rather than proving it outright (which is done in the course notes). This is an ideal opportunity for the chain rule, rather than directly inserting the form of $\sigma(t)$. First calculate the derivatives of the diffusion equation:


\begin{align*}
\frac{\partial f(x,t)}{\partial t} &=
\frac{1}{\sqrt{2\pi}}\left[
-\frac{1}{\sigma(t)^2} + \frac{x^2}{\sigma(t)^4}
\right]\sigma'(t)\exp\left(-\frac{x^2}{2
\sigma(t)^2}\right)
\newline
\frac{\partial f(x,t)}{\partial x} &=
\frac{1}{\sqrt{2\pi}}\left[
-\frac{x}{\sigma(t)^3}
\right]\exp\left(-\frac{x^2}{2
\sigma(t)^2}\right)
\newline
\frac{\partial^2 f(x,t)}{\partial x^2} &=
\frac{1}{\sqrt{2\pi}}\left[
-\frac{1}{\sigma(t)^3}
+\frac{x^2}{\sigma(t)^5}
\right]\exp\left(-\frac{x^2}{2
\sigma(t)^2}\right)
\;,
\end{align*}

$\Rightarrow{}$ and then,

\begin{align*}
\sigma'(t) &= \frac{\alpha}{\sigma(0)^2 + 2 \alpha t} = \frac{\alpha}{\sigma(t)}
\;,
\end{align*}

$\Rightarrow{}$ Inserting into the diffusion equation,


\begin{align*}
\frac{f(x,t)}{t} &= \alpha \frac{ \partial^2 f(x,t)}{\partial x^2}
\newline
\frac{1}{\sqrt{2\pi}}\left[
-\frac{1}{\sigma(t)^2} + \frac{x^2}{\sigma(t)^4}
\right]\sigma'(t)\exp\left(-\frac{x^2}{2
\sigma(t)^2}\right)
&=
\alpha \frac{1}{\sqrt{2\pi}}\left[
-\frac{1}{\sigma(t)^3}
+\frac{x^2}{\sigma(t)^5}
\right]\exp\left(-\frac{x^2}{2
\sigma(t)^2}\right)
\end{align*}

$\Rightarrow{}$ Divide common terms,
\begin{align*}
\left[
-\frac{1}{\sigma(t)^2} + \frac{x^2}{\sigma(t)^4}
\right]\sigma'(t)
&=
\alpha \left[
-\frac{1}{\sigma(t)^3}
+\frac{x^2}{\sigma(t)^5}
\right]
\end{align*}

$\Rightarrow{}$ Substitute for $\sigma'(t)$,
\begin{align*}
\left[
-\frac{1}{\sigma(t)^2} + \frac{x^2}{\sigma(t)^4}
\right]
\frac{\alpha}{\sigma(t)}
&=
\alpha \left[
-\frac{1}{\sigma(t)^3}
+\frac{x^2}{\sigma(t)^5}
\right]
\end{align*}

$\Rightarrow{}$ LHS is equal RHS, so this is proven.
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

------------------------------

### Problem 7.

For an initial concentration,
$f(x,0) = \frac{1}{\sigma_0}\exp\left( -\frac{(x-x_0)^2}{2 \sigma_0^2} \right)$,
governed by the diffusion equation, calculate the concentration at
$x=0\,\mu\mathrm{m}$ and $t=10\,\mathrm{s}$, for $x_0 = 5\,\mu\mathrm{m}$,
$\sigma_0 = 1\,\mu\mathrm{m}$, and $\alpha = 2\,\mu\mathrm{m}^2\mathrm{s}^{-1}$.
(Use the solution given in Q6 to help)

<div class = "answer">
$\Rightarrow{}$ First set up a solution to the diffusion equation such that it matches the initial condition. i.e.

$$
f(x,t) = \frac{1}{\sqrt{\sigma_0^2 + 2 \alpha t}}
\exp\left(-\frac{(x-x0)^2}{2
{\sigma_0^2 + 4 \alpha t}}\right) \;.
$$

$\Rightarrow{}$ Then substitute in all constant and variable values,

$$
f(x=0,t=10\,\mathrm{s}) = \frac{1}{\sqrt{(1\,\mu\mathrm{m})^2 + 2\times2\,\mu\mathrm{m}^2\mathrm{s}^{-1} \, 10\,\mathrm{s}}}
\exp\left(-\frac{(0-5\,\mu\mathrm{m})^2}{2\times
{(1\,\mu\mathrm{m})^2 + 4 \times 2\,\mu\mathrm{m}^2\mathrm{s}^{-1} \, 10\,\mathrm{s}}}\right) \;
$$


$\Rightarrow{}$ Which reduces to,
$$
\boxed{ f(x=0,t=10\,\mathrm{s}) = \frac{1}{\sqrt{41\,\mu\mathrm{m}^2}}
\exp\left(-\frac{25\,\mu\mathrm{m}^2}{82\,\mu\mathrm{m}^2}\right)
\approx 0.12 \mu\mathrm{m}^{-1} }
$$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>


<br><br>


## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">Hide all answers</button>
<br><br>
### For Printing
<button type="button" onclick="prepareForPrint('block')">Add whitespace</button>
<button type="button" onclick="prepareForPrint('none')">Remove whitespace</button>

<br><br>

# Next week, Finite Methods!
