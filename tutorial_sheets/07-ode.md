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

# Ordinary Differential Equations Tutorial Sheet, Sheet #7

### Learning targets
* Identify the auxiliary equation for a differential equation
* Understand how the solutions to the auxiliary equation relates to the general solution
* Find the general equation and particular equation for a given differential equation
* Write an expression to describe the dynamics of a spring trolley system

### Additional Resources
* [Khan Academy - ODEs intro](https://youtu.be/6o7b9yyhH7k)

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Find the general solutions of the following differential equations. This is very easy to do with WolframAlpha (or similar), but it's worth understanding how it works.

(a) $\frac{d^2y}{ {dx}^2}-3\frac{dy}{dx}+2y=0$
<div class = "answer">
As the equation is a homogeneous ODE:

$\Rightarrow r^2-3r+2=0,\quad r_{1,2}=1, 2$.

$\Rightarrow{}$ Using $r_{1,2}$:

$ y(x)=C_1e^{1x}+C_2e^{2x} $

$\Rightarrow{}$ Therefore, the general solution is: $\boxed{y(x)=C_1e^x+C_2e^{2x}}$

Using WorframAlpha:

<img src="07-ode-media/answer1a.png">

[Click here for WolframAlpha link](https://www.wolframalpha.com/input/?i=d2y%2Fdx2+-+3+dy%2Fdx+%2B+2y+%3D+0) (you might need to scroll a bit to find the answer)

</div>

<div class = "workingout"><br><br><br></div>

(b) $\frac{d^2y}{ {dx}^2}+2\frac{dy}{dx}+2y=0$
<div class = "answer">

$\Rightarrow{}\quad$
$r^2+2r+2=0, \quad r_{1,2}=-1\pm i$

$\Rightarrow{}\quad\ $Therefore, the general solution is: 
$ y(x)=C_1e^{-x}\cos{x}+C_2e^{-x}\sin{x} $
<br><br>

$\Rightarrow{} $Simplified:

$\boxed{y(x)=e^{-x}(C_1\cos{x}+C_2\sin{x})}$
</div>

<div class = "workingout"><br><br><br></div>

(c) $\frac{d^2y}{ {dx}^2}+4\frac{dy}{dx}+4y=0$
<div class = "answer">
$\Rightarrow r^2+4r+4=0, \quad \rightarrow \quad r_{1,2}=-2$ (for both)
<br><br>
$\Rightarrow{} $Therefore, the general solution is: 
$ y(x)=C_1e^{-2x}+C_2e^{-2x}x $,
<br>
where the final $x$ appears because the root $-2$ is repeated 2x. If that is confusing, have a look at part (d).
<br><br>

$\Rightarrow{} $Simplified:

$\boxed{y(x)=(C_1+C_2x)e^{-2x}}$
</div>

<div class = "workingout"><br><br><br></div>

(d) $\frac{d^3y}{ {dx}^3}+6\frac{d^2y}{ {dx}^2}+12\frac{dy}{dx}+8y=0$
<div class = "answer">
This is a scary third-order ODE, but the way we solve it is exactly the same.
$\Rightarrow r^3+6r^2+12r+8=0, \quad \rightarrow \quad r_{1,2,3}=-2$ (for all three)
<br><br>
$\Rightarrow{} $Therefore, the general solution is: 
$ y(x)=C_1e^{-2x}+C_2e^{-2x}x+C_3e^{-2x}x^2 $,
<br>
where the $x$ & $x^2$ appear because the root $-2$ is repeated 3x.
<br><br>

$\Rightarrow{} $Simplified:

$\boxed{y(x)=(C_1+C_2x+C_3x^2)e^{-2x}}$
</div>

<div class = "workingout"><br><br><br></div>

-----------------------------------------------------------------------------------

### Problem 2.
The differential equation $\ddot{x}+2\dot{x}+4x=0$ describes the free vibration of a mass-spring-damper system, where $x(t)$ represents the displacement from equilibrium of mass $M$.

(a) What values of mass $M$, spring stiffness $k$ and the viscous damping coefficient $c$ does the equation represent?
<div class = "answer">You can read these straight off the equation. For $\ddot{x}+2\dot{x}+4x=0,$ $\boxed{\text{ Mass } M = 1 \text{, damping coefficient } c = 2 \text{ and spring stiffness } k=4.}$</div>

<div class = "workingout"><br><br></div>

(b) Show that the frequency of vibration of the system is $\sqrt{3}$ rad/s and verify that this is equal to $\sqrt{\left(4kM-c^2\right)}/2M$.
<div class = "answer">The auxiliary equation can be written as $mr^2+cr+k=0$. 
At $c = 2, k = 4$ & $m = 1$, this gives $r^2+2r+4=0$.

Solving for homogeneous ODE:

$\Rightarrow{}\ r_{1,2}=\frac{-2 \pm \sqrt{2^2 - 4 * 1 * 4}}{2 * 1}$ (the quadratic formula),

$\Rightarrow{} r_{1,2} =-1\pm \sqrt{3} i$
<br><br>
The frequency of an ODE is the imaginary component of the solution of the auxillary equation, i.e. frequency  $\boxed{\omega = Im(r) = \sqrt{3}.}$ Note that frequency cannot be negative.
<br><br>
$\Rightarrow{} $
Substituting the values of $c,\ k\ \mathrm{and}\ m$ in (this is trivial in WolframAlpha) $\boxed{\sqrt{\left(4kM-c^2\right)}/2M = \sqrt{3}}$
</div>

<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------

## Exam Style Questions
### Problem 3.
This graph shows the speed vs time (purple) and acceleration vs time (red) for a damped harmonic oscillator.

<img src="07-ode-media/question4.png">

(a) State whether this system is under-, over- or critically damped.
<div class="answer">
The waveform is decaying over time, but does oscillate. Therefore, $\boxed{\text{the system is under-damped.}}$ No working is needed.
</div>
<div class = "workingout"><br></div>

(b) Write down the initial velocity and acceleration of the trolley.
<div class="answer">
$\boxed{v=-2m/s, a=2m/s}$. These can be read off the graph.
</div>
<div class = "workingout"><br></div>

(c) Find the integer frequency of oscillation of the system, in rad/s.
<div class="answer">
From the graph, it seems that the time period of oscillation $T ≈ 2.1$s.

Damped natural frequency $\omega = \frac{2\pi}{T} ≈ \frac{2\pi}{2.1}$

$\omega ≈ 2.992$, so we can say that $\boxed{\omega = 3\text{rad/s}}$
</div>
<div class = "workingout"><br><br><br><br><br></div>

### Problem 4.

A trolley of mass, $m=$ 5kg, is attached to a wall by a spring of stiffness $k=$ $10Nm^{-1}$ and rolls along the floor with a drag coefficient $c=3$.

At $x=0$ the spring is in its neutral position (neither extended nor compressed) and the positive $x$ direction is considered to be pointing away from the wall. Air resistance can be neglected.

(a) Draw a diagram of this system.
<div class = "answer">
<img src="07-ode-media/answer3a.png"><br>
$m=$ 5kg,  $k=$ 10Nm$^{-1}$,  $c=3$ & $x(0) = 0$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(b) Write an expression relating the location of the trolley to its acceleration.
<div class = "answer">
Using the above values for $m$, $k$ & $c$:
$m\ddot{x}+c\dot{x}+kx=0 \quad\rightarrow\quad \boxed{5\ddot{x}+3\dot{x}+10x=0}$
</div>

<div class = "workingout"><br><br></div>

(c) State whether this system is underdamped, critically damped or overdamped.
<div class = "answer">$b^2-4ac$ $,\quad 3^2-(4\times 5 \times 10) = 9 - 200 = -191$
$\Rightarrow \boxed{\text{Under-damped}}$
</div>
<div class = "workingout"><br><br><br></div>

(d) Using this information, sketch a graph of displacement $x$ vs time $t$ for the trolley.

<div class = "answer">
This is something that WolframAlpha is really good at. From your knowledge of what 'under-damped' means, you should have a rough idea of what you're expecting - this will help because you'll know whether Wolfram has given you a sensible answer or not.
Just type the equation and initial conditions into the search:

```5x''+3x'+10x=0, x(0)=0```.
One of its many outputs will be a ready-made graph:
<img src="07-ode-media/answer3d.png"><br>


[Click here for WolframAlpha link](https://www.wolframalpha.com/input/?i=5x%27%27%2B3x%27%2B10x%3D0%2C+x%280%29%3D0)

</div>

<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------------------------

## Extension Question
### Problem 5.

A cargo barge of mass $1000$ tonnes ($=1\times10^6\text{kg}$) is anchored to the seabed by a chain that we can assume to behave elastically. The chain has length $L=10m$ and a cross-sectional area $A$ of $0.0002m^2$. The Young's Modulus $E$ of steel is $210\text{GPa}$, and spring constant $K=\frac{E\times{A}}{L}$.

(a) Find the spring constant $K$.
<div class="answer">
$K=\frac{E\times{A}}{L}=\frac{210\times10^9\times{0.0002}}{10}\boxed{=4.2\times10^6}$
</div>
<div class = "workingout"><br><br><br><br></div>

The anchored barge is hit by a wave, causing it to oscillate on its chain. The water around the barge has a damping effect on the barge, with a damping coefficient $c=2\times10^6$. The below graph shows the barge's speed vs time (green) and acceleration vs time (red). The y-intercept of the green line is $-2$ and the red line is $\frac{4}{3}$.
<img src="07-ode-media/question5.png">

(b) State and explain whether this system is under-, over-, or critically damped.
<div class="answer">
$\boxed{\text{Underdamped. The system makes several oscillations before coming to rest.}}$
</div>
<div class = "workingout"><br><br></div>

(c) Construct an ODE to describe the motion of the barge.
<div class="answer">
Using $M$, $C$ & $K$:

$\boxed{1\times10^6\ddot{x}+2\times10^6\dot{x}+4.2\times10^6x=0}$
</div>
<div class = "workingout"><br><br><br><br></div>

(d) Find the height of the wave that displaced the barge to start the oscillation (i.e. find $x(0)$).
<div class="answer">
Using the above equation and the initial conditions from the graph,

$10^6\ddot{x}+2\times10^6\dot{x}+4.2\times10^6x=0,\quad\ddot{x}(0)=\frac{4}{3},\quad\dot{x}(0)=-2$

We can solve this as we would any other ODE. We have 2 initial conditions, so we can build an equation for $x(t)$, and then solve for $t=0$. 

We can do this very easily in WolframAlpha

$\Rightarrow$ Tell Wolfram what you know, separating the initial conditions with commas. \
```(1e6)x''+(2e6)x'+(4.2e6)x=0, x''(0)=(4/3), x'(0)=-2```

$\Rightarrow$ Wolfram will [solve the ODE](https://www.wolframalpha.com/input/?i=%281e6%29x%27%27%2B%282e6%29x%27%2B%284.2e6%29x%3D0%2C+x%27%27%280%29%3D%284%2F3%29%2C+x%27%280%29%3D-2) for you.
<img src="07-ode-media/answer5c.png"> \
This isn't a particularly nice way of writing the equation - but that doesnt matter.

We now have a Wolfram solution to this ODE. All we have to do now is plug $t=0$ into the equation:

$\Rightarrow$ Plug the equation back into Wolfram.\
You can do this by clicking on it. Then add ```, t=0``` to the end of the query and press enter. This tells Wolfram that you want the value of the equation at $t=0$.

$\Rightarrow \boxed{x(0)=0.635m}$ \
$\Rightarrow$ This means that the barge was lifted by a 63.5cm high wave.

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><br><br><br><br></div>


-----------------------------------------------------------------------------------

### WolframAlpha
You can generate a limitless suppply of these second order homogeneous ODE questions and answers using WolframAlpha including the various graphs. For example, try typing in: 
``` 3x”(t)+3x’(t)+4x(t)=0 where x(0)=3, x’(0)=0 ```,

[Click here for WolframAlpha link](https://www.wolframalpha.com/input/?i=3x%27%27(t)%2B3x%27(t)%2B4x(t)%3D0+where+x(0)%3D3,+x%27(0)%3D0)

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

# Next week, Coupled Harmonic Oscillators!