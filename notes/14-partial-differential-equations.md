<!--
Hello Team –
I'm re-writing this section of the notes,
so if you were planning to transcribe this chapter from
the PDF notes, you can skip this one :)
– Freddie
-->

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

<img src="figs/PDEchap.PNG" width="200"/>

# Chapter 14 - Partial Differential Equations
## Recap
In a previous chapter, we looked at
[ODEs – Ordinary Differential Equations](9-ODE).
Here we had a quantity of interest, a model for how the system evolves in time,
and a set of initial conditions.
One of the examples that we considered was the trolley on a spring.
Here the quantity of interest was the position of the trolley $x(t)$,
the model for how it evolves was an ODE like
$\ddot{x}(t) = -\frac{k}{m} x(t)$,
and the initial conditions were $x(0)$ and $\dot{x}(0)$,
the position and velocity of the trolley at $t=0$, when we start the clock.

Solving the ODE meant finding an $x(t)$ that satisfied the ODE
in the general case (of any initial conditions), i.e.
$x(t) = A \cos(\omega t) + B \sin(\omega t)$
with
$\omega = \sqrt{\frac{k}{m}}$;
then matching this general solution to the particular initial conditions we
were given. i.e.
$x(t) = x(0) \cos(\omega t) + \frac{\dot{x}(0)}{\omega}\sin{\omega t}$.

Next, we considered
[Coupled Oscillators](10-coupled-oscillators),
where the game was the same but we had multiple discrete quantities of interest,
and again a model for how the system evolves and set of initial conditions.
E.g. for a set of trolleys connected to each other with springs.

In this setup we upgraded some of our quantities to vectors and matrices, e.g.
$x(t) \rightarrow \mathbf{x}(t)$,
and our ODE became,
$$
\ddot{\mathbf{x}}(t) =
  \begin{bmatrix}
    -\frac{k_1 + j}{m_1} & \frac{j}{m_1} \\
    \frac{j}{m_2} & -\frac{k_2 + j}{m_2}
  \end{bmatrix}
\mathbf{x}
$$
We solved this system by finding the *normal modes* that oscillate
in harmonic motion at a single frequency,
and added the combination of all solutions together for the
genaral solution, before matching to initial conditions.

### Upgrading to PDEs
**Partial Differential Equations**, PDEs, are the next step in this progression
where we go from modelling the time evolution of single quantity,
to a discrete set of quantities, to a continuous set of values – e.g.
the displacement of every point on a guitar string when it is struck,
the temperature at every point in a room when a heat source is nearby,
the stresses on the body of an aircraft during operation.

Solving PDEs allows us to calculate how our systems evolve in time,
but also can give us insight into how to optimise them e.g.
for their response efficiency, or to detect failure modes.

PDEs find applications in many fields of Engineering, and are studied in their
own right as a topic in Appled Mathematics.
In this module we will introduce the topic and give a first set of tools for
approaching them.

We'll be relying heavily on the intuition you have built up for ODEs,
so make sure you are refreshed and comfortable with that topic.

## Introducing PDEs
Returning to our analogy to ODEs and Coupled Oscillators,
Our quantity of interest is usually the value of a quantity both at some point
in time and now at some point in space.
i.e. a multivariate function of space and time – $f(\mathbf{x}, t)$.

The model for our system, how our quantity of interest evolves in time,
is no longer an *Ordinary* Differential Equation,
but a *Partial* Differential Equation,
i.e. a differential equation that contains
[partial derivatives](13-multivariate-calculus).

Some physically motivated PDEs that we'll look at in more detail are the
diffusion equation:
$$
\frac{\partial f(x, t)}{\partial t} =
\alpha \frac{\partial^2 f(x, t)}{\partial x^2}
$$
and the wave equation:
$$
\frac{\partial^2 f(x, t)}{\partial t^2} =
\frac{1}{c^2} \frac{\partial^2 f(x, t)}{\partial x^2}
$$
Notice that in each we have deriviatives in both space and time of our quantity
of interest, $f(x, t)$,
as well as some constants of the system, $\alpha$ and $c$.

A small slight-of-hand to be aware of here is,
previously our quantity of interest was labeled $x$, and we solved for $x(t)$.
In this case, our quantity of interest is $f$
and now $x$ is one of our independent variables along with $t$,
and we solve for $f(x, t)$.
In different applications, we may use different symbols for our dependent and
independent quantities, so it's always worth noting which variables play what
role.

The initial conditions of the system also upgrade,
instead of a single value when $t=0$,
we now typically specify an entire function, $f(x, 0)$.

Solving partial differential equations amounts to asking the question:

*"If I have a system who's behaviour is governed by a particular PDE,*
*and the system starts a known initial state:*
*What is the state of the system at future times?"*
