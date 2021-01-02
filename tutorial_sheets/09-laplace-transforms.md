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

# Laplace Transforms Tutorial Sheet, Sheet #9

### Learning targets
 * Use the definition of the Laplace transform
 * Use 

### Additional resources
*insert links*

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Using the definition: 
\begin{equation*}
\mathcal{L}\\{f(t)\\}=\int_{0}^{\infty}f(t){e^{-st}}{dt}=F(s),\quad{s>0}
\end{equation*}

(a) $f(t)=e^{at}$
<div class = "answer">
$\Rightarrow{}\quad$
$F(s)=\int_{0}^{\infty}{e^{-st}{e^{at}}}{dt}=\int_{0}^{\infty}{e^{-(s-a)t}{dt}}=\left[-\frac{1}{s-a}e^{-(s-a)t}\right]_0^\infty, \quad{s>a}$
$\Rightarrow{}\quad\boxed{F(s)=\frac{1}{s-a}}$
</div>

(b) $g(t)=9$
<div class = "answer">
$\Rightarrow{}\quad$
$G(s)=\int_{0}^{\infty} \ {9e^{-st}{dt}}={[-\frac{9}{s}{e^{-st}}]_0^\infty}\quad$
$\Rightarrow{}\ \ $ 
$\boxed{G(s)=\frac{9}{s}}$
</div>


(c) $k(t)=4t$
<div class = "answer">
$\Rightarrow{}\quad$
$K(s)=\int_{0}^{\infty} 4t \ e^{-st} dt=4\int_{0}^{\infty} t \ e^{-st} dt$

Using integration by part:
$udv=uv-\int{vdu}$

$u=t, dv=e^{-st}dt$ and $du=dt, v=-\frac{1}{s} e^{-st}$

$\Rightarrow{}\quad$
$4\int_{0}^{\infty} t \ e^{-st}dt=4(-\frac{t}{s} e^{-st} - \int_{0}^{\infty} \frac{-1}{s} e^{-st}dt)=4(\frac{1}{s^2}(-se^{-st}t-e^{-st}))_{0}^{\infty}$

$\Rightarrow{}\quad$
$\boxed{K(s)=\frac{4}{s^2}}$
</div>

(d) $m(t)=e^{2t}$
<div class = "answer">
$\Rightarrow{}\quad$
$G(s)=\int_{0}^{\infty} \ {e^{-st}}{e^{2t}}{dt}={\left[-\frac{1}{s-2}{e^{-(s-2)t}}\right]_0^\infty}\quad$
$\Rightarrow{}\ \boxed{G(s)=\frac{1}{s-2}}$
</div>

### Problem 2.
Using the DE1-MEM Formula sheet, find the Laplace Transforms of the given functions:

(a) $f(t)=6e^{-5t}+e^{3t}-5t^{3}-9$
<div class = "answer">
$\Rightarrow{}\quad$
$F(s)=\mathcal{L}\{{6e^{-5t}+e^{3t}-5t^{3}-9}\}$

$\Rightarrow{}\quad$
$\boxed{F(s)=\frac{6}{s+5}+\frac{1}{s-3}-\frac{30}{s^4}-\frac{9}{s}}$
</div>

(b) $g(t)=4\cos(4t)-9\sin(4t)+2\cos(10t)$
<div class = "answer">
$\Rightarrow{}\quad$
$G(s)=\mathcal{L}\{{4\cos(4t)}\}-\mathcal{L}\{{9\sin(4t)}\}+\mathcal{L}\{{2\cos(10t)}\}$ 

$\Rightarrow{}\quad$
$\boxed{G(s)=\frac{4s}{{s^2}+{16}}-\frac{36}{{s^2}+{16}}+\frac{2s}{{s^2}+{100}}}$
</div>

(c) $k(t)=3\sinh(2t)+4\cosh(3t)$
<div class = "answer">
$\Rightarrow{}\quad$
$K(s)=\mathcal{L}\{{3\sinh(2t)}\}+\mathcal{L}\{{4\cosh(3t)}\}$

$\Rightarrow{}\quad$
$\boxed{K(s)=\frac{6}{{s^2}-{4}}+\frac{4s}{{s^2}-{9}}}$
</div>

(d) $m(t)=e^{3t}+\cos(6t)-e^{3t}\cos(6t)$
<div class = "answer">
$\Rightarrow{}\quad$
$M(s)=\mathcal{L}\{{e^{3t}}\}+\mathcal{L}\{{\cos(6t)}\}-\mathcal{L}\{{e^{3t}\cos(6t)}\}$
    
$\Rightarrow{}\quad$
$\boxed{M(s)=\frac{1}{{s}-{3}}+\frac{s}{{s^2}+{36}}-\frac{s-3}{{(s-3)^2}+{36}}}$
</div>

(e) $o(t)=e^{-2t}{\cos^2}(3t)-3t^2e^{3t}$
<div class = "answer">
$\Rightarrow{}\quad$
${cos^2}(3t)$ can be writen as = $\frac{1+{\cos}(6t)}{2}$
$\Rightarrow{}\quad$
$O(s)=\mathcal{L}\{{e^{-2t}}{(\frac{1}{2}+\frac{1}{2}{\cos}(6t))}-{3t^2e^{3t}}\}=\mathcal{L}\{\frac{1}{2}{e^{-2t}}+{\frac{1}{2}{e^{-2t}}{\cos}(6t)}-{3t^2e^{3t}}\}$
$\Rightarrow{}\quad$
$\boxed{O(s)=\frac{1}{{2s}+{4}}+\frac{s+2}{2(s+2)^{2}+72}-\frac{6}{{(s-3)^3}}}$
</div>


### Problem 3.
Compute the inverse Laplace Transform of the given functions:

(a) $F(s)= \frac{5}{s}-\frac{4}{s-2}+\frac{24}{(s-2)^5}$
<div class = "answer">
$\Rightarrow{}\quad$
$\mathcal{L}^{-1}\{F(s)\}= \ \mathcal{L}^{-1}\{{\frac{5}{s}-\frac{4}{s-2}+\frac{24}{(s-2)^5}}\}$
    
$\Rightarrow{}\quad$
$\boxed{f(s)=5-{4e^{2t}}+e^{2t}{t^4}}$
</div>

(b) $G(s)= \frac{7s-1}{(s+1)(s+2)(s-3)}$
<div class = "answer">
$\Rightarrow{}\quad$
$\mathcal{L}^{-1}\{G(s)\}= \ \mathcal{L}^{-1}\{{\frac{7s-1}{(s+1)(s+2)(s-3)}}\}$
    
$\Rightarrow{}\quad\ \frac{7s-1}{(s+1)(s+2)(s-3)}= \frac{A}{s+1}+\frac{B}{s+2}+\frac{C}{s-3}=\frac{2}{s+1}+\frac{-3}{s+2}+\frac{1}{s-3}$
    
$\Rightarrow{}\quad\ \boxed{g(t)=2e^{-t}-3e^{-2t}+e^{3t}}$
</div>

(c) $K(s)= \frac{4s+5}{(s-2)^2(s+3)}$
<div class = "answer">
$\Rightarrow{}\quad$
$\mathcal{L}^{-1}\{K(s)\}= \ \mathcal{L}^{-1}\{{\frac{4s+5}{(s-2)^2(s+3)}}\}$

$\Rightarrow{}\quad \ \frac{4s+5}{(s-2)^2(s+3)}=-\frac{7}{25(s+3)}+\frac{7}{25(s-2)}+\frac{13}{5(s-2)^2}$

$\Rightarrow{}\quad \ \boxed{k(t)=-\frac{7}{25}{e^{-3t}}+\frac{7}{25}{e^{2t}}+\frac{13}{5}{t}{e^{2t}}}$
</div>


-----------------------------------------------------------------------------------

## Exam Style Questions
### Problem 4.
Solve the following ODE function using Laplace Transform:

(a) $y"+4y'+8y=1\ \ if \ \ y(0)=0,\ \ y'(0)=0$
<div class = "answer">
$\Rightarrow{}\quad$
$\mathcal{L}\{y"(t)+4y'(t)+8y(t)\}=\mathcal{L}\{y"(t)\}+4\mathcal{L}\{y'(t)\}+8\mathcal{L}\{y(t)\}=\mathcal{L}\{1\}$

$\Rightarrow{}\quad \ s^2Y(s)-sy(0)-y'(0)+4(sY(s)-y(0))+8Y(s)=\frac{1}{s}$

$\Rightarrow{}\quad \ (s^2+4s+8)Y(s)-(s+4)y(0)-y'(0)=\frac{1}{s}$

$\Rightarrow{}\quad \ $Substitute $y(0)=0,\ \ y'(0)=0$:

$$(s^2+4s+8)Y(s)-0-0=\frac{1}{s}$$

$\Rightarrow{}\quad \ (s^2+4s+8)Y(s)=\frac{1}{s}$
$\quad\Rightarrow{}\ Y(s)=\frac{1}{s(s^2+4s+8)}$

$\Rightarrow{} \ $ Find the inverse Laplace transform of $Y(s)$:

$\frac{1}{s(s^2+4s+8)}=\frac{A}{s}+\frac{Bs+C}{(s^2+4s+8)}$
$\quad\Rightarrow{}\ 1=A(s^2+4s+8)+(Bs+C)s$

$Y(s)=\frac{1}{8s}-{\frac{s+4}{8(s^2+4s+8)}}$

$Y(s)=\frac{1}{8s}-{\frac{1}{8} \frac{(s+2)}{(s+2)^2+4}-\frac{1}{8} \frac{2}{(s+2)^2+4}}$

$\boxed{y(t)=\frac{1}{8}-{\frac{1}{8}}{e^{-2t}{\cos2t}}-\frac{1}{8}{e^{-2t}{\sin2t}}}$
</div>

### Problem 5.
Solve the following ODE function using Laplace Transform:

(b) $y"+4y'+4y=6e^{-2t}\ \ if \ \ y(0)=-2,\ \ y'(0)=8$
<div class = "answer">
$\Rightarrow{}\quad\mathcal{L}\{y"(t)+4y'(t)+4y(t)\}=\mathcal{L}\{y"(t)\}+4\mathcal{L}\{y'(t)\}+4\mathcal{L}\{y(t)\}=\mathcal{L}\{6e^{-2t}\}$ 

$\Rightarrow{}\quad \ s^2Y(s)-sy(0)-y'(0)+4(sY(s)-y(0))+4Y(s)=\frac{6}{s+2}$

$\Rightarrow{}\quad \ (s^2+4s+4)Y(s)-(s+4)y(0)-y'(0)=\frac{6}{s+2}$

$\Rightarrow{}\quad \ $Substitute $y(0)=-2,\ \ y'(0)=8$:

$$(s^2+4s+4)Y(s)+2(s+4)-8=\frac{6}{s+2}$$

$$(s^2+4s+4)Y(s)=\frac{6}{s+2}-2s$$

$\Rightarrow{}\quad \ (s+2)^2Y(s)=\frac{6}{s+2}-{2s}$
$\quad\Rightarrow{}\ Y(s)=\frac{6}{(s+2)^3}-\frac{2s}{(s+2)^2}$

$\Rightarrow{} \ $ Find the inverse Laplace transform of $Y(s)$:

$Y(s)=\frac{6}{(s+2)^3}-\frac{2(s+2-2)}{(s+2)^2}$

$Y(s)=\frac{6}{(s+2)^3}-\frac{2s+4}{(s+2)^2}+\frac{4}{(s+2)^2}$

$Y(s)=\frac{6}{(s+2)^3}-\frac{2}{(s+2)}+\frac{4}{(s+2)^2}$

$y(t)=3e^{-2t}t^2-2{e^{-2t}}+4e^{-2t}t$
$\quad\Rightarrow{}\quad$ \ans{$y(t)=(3t^2+4t-2){e^{-2t}}$}}
</div>

-----------------------------------

## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">Hide all answers</button>

<br><br>

# Next week, another topic!
![vectors](02-vectors-media/cover.png)