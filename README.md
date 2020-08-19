# module-resources
Module resources for the Dyson School of Design Engineering's 1st year undergraduate mathematics course.

<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { inlineMath: [ ['$','$'], ["\\(","\\)"] ], processEscapes: true } }); </script> <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"> </script> <script type="text/javascript" src="tutorialSheetScripts.js"> </script>

# Coursework

## __Problem__
The year is 1930’s New York City and you are applying to help build the Empire State building. However, to be selected you need to write a report to the big boss to show your worth as an engineer, for this he set you a challenge. \
The challenge is to show the final position of a grain inside a cylindrical wooden beam. \
You are told that this beam is being fixed on a wall and during its installation, it is hammered into a small cylindrical gap in the wall and then twisted in to secure it. \
You are only told:

* The radius of the beam is (0.6 0 0.8)dm with the centre (0 0 0).
* The length of the beam is (-1.2 0 1.6)m.
* The position of the grain is assumed to be positioned at (-0.72 0.01 0.96)m.
* The force of the hammer is (120 0 -120)N.
* The twisting force applied at the edge of the beam (0 1 0)N.
* The cost of lumber is £16.49 per square meter.
* The distance from Earth to the moon is 356,000km.

## __Report__
Your aim is not only to find the final position but to detail your reasoning in your report  through graph sketching, vectors, matrices and state any assumptions made such as tolerances and probability.

## __Resources__
Equations you might need to know: \
Stress equation ($\sigma$ is stress, $F$ is force and $A$ is area)\
$\sigma = \frac{F}{A} $ \
Young's Modulus equatoin ($E$ is Young's modulus, $\sigma$ is stess and $\epsilon$ is strain) \
$E = \frac{\sigma}{\epsilon} $ \
Strain equation ($\epsilon$ is strain, $L$ is original length and $L_0$) \
$\epsilon = \frac{L - L_0}{L} $ \
Torque equation ($T$ is torque, $r$ is radius, $F$ is force and $\theta$ is angle of rotation) \
$ T = \vec{r} \times \vec{F} = rFsin(\theta)$

### __Hints__
<div class = "answer"> There's no need to know the distance from Earth to the Moon or the price of lumber.
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> Start finding the area of a the surface. 
(Area of a circle equation is 
$A = r\pi^2$)
There is two ways of solving this, either doing a dot product of two vectors or finding the magnitude of r. 
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> Heads up, there will be a lot of googling. Start with making an assumption of lumber's Young Modulus.
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> Keep the length's as vectors. Once you find the change of length of the beam, apply this difference to grain position, or don't...
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> For the second part in regards to the twist, you will only need the torsion equation. 
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> Once you find the angle, find a second vector on the circle which snaps to the edge and has an angle $\theta$ to the radius vector.
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> $cos(\theta) = \frac{\vec{u}.\vec{v}}{|u||v|}$
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> A second way to write the radius vector would be (0, 0.1, 0).
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> Perfect time to sketch out the circle and possible equations.
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> Now that you found the new point at the end of the beam due to torsion. Why not sketch out position of the grain and the new point.
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> Feel free to make assumptions here, there are multiple ways of tackling this.
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
<div class = "answer"> Heads up, did you realise that at the very beginning, it's possible to do make a matrix which would shift all the points and vectors to a simple x,y,z coordinate?
</div>
<button type="button" onclick="displayAnswers('block')">Show hint </button>
<button type="button" onclick="displayAnswers('none')">Hide hint </button>
<br>
