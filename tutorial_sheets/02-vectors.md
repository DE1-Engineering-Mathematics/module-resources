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

# Vectors, Week 2

### Learning targets
* Add and subtract vectors
* Find modulus of a vector
* Find the unit vector
* Calculate the scalar product
* Use $\cos{\theta} = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}$
* Use the cross product
* Find the cartesian and vector equations for a plane

### Reading
* [section](link#page=x)

### Lectures
* One (monday)
* Two (tuesday)

### Additional resources

### Additional resources
*insert links*

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Consider the three vectors $\vec{a}=$ (2,1,0), $\vec{b}=$ (-1,2,3), and $\vec{c}=$ (1,2,1). Calculate the following:

(a) $\vec{a}+\vec{b}=$

<div class = "answer">$\Rightarrow \quad \boxed{\vec{a}+\vec{b}=(1,3,3)}$</div>

(b) $2\vec{a}-\vec{b}=$

<div class = "answer">$2\vec{a}-\vec{b}=(2\times2+1,2\times1-2,2\times0-3) = \boxed{ (5,0,-3)}$</div>

(c) $\vec{a}\circ\vec{b}\circ \vec{c}=$

<div class = "answer">$\vec{a}\circ\vec{b}\circ \vec{c}=(\vec{a}\circ\vec{b})\circ\vec{c}=(-2,2,0)(1,2,1)=\boxed{(-2,4,0)}$</div>

(d) Modulus of $\vec{c}$

<div class = "answer">$|c| = \sqrt{1^2+2^2+1^2}= \boxed{ \sqrt{6}}$</div>

(e) Find the unit vector in direction of c 

<div class = "answer">$\boxed{\hat{c} = \frac{\vec{c}}{|c|} = \left(\frac{1}{\sqrt{6}},\frac{2}{\sqrt{6}},\frac{1}{\sqrt{6}}\right)}$</div>

(f) Find the volume of the parallelepiped described by the vectors $\vec{a}, \vec{b}$ and $\vec{c}$ (hint: Use Triple scalar product). 

<div class = "answer">$V=|\vec{a}\cdot(\vec{b}\times\vec{c})|=|(2,1,0)\cdot(-4,4,-4)|=|-4|=\boxed{4 \text{ volume units}}$</div>

-----------------------------------------------------------------------------------

### Problem 2
Scalar product calculation

(a) Let $\vec{a} = \hat{i}+2\hat{j} $ and $ \vec{b} =2\hat{i}+\hat{j}. $ Is $ |\vec{a}| = |\vec{b}|?$ Are the vectors $\vec{a}$ and $\vec{b}$ equal ?

<div class = "answer">We have $$|\vec{a}|=\sqrt{1^2+2^2}=\sqrt{5}$$ and $$|\vec{b}|=\sqrt{2^2+1^2}=\sqrt{5}$$ So, $$\boxed{|\vec{a}|=|\vec{b}|.}$$ But, the two vectors are <b>not equal</b> since their corresponding components are distinct.</div>

(b) Find the vector from point $P(2, 3, 0)$ to $Q(-1, -2, -4)$:

<div class = "answer">Since the vector is to be directed from P to Q, clearly P is the initial point and Q is the terminal point. So, the required vector joining P and Q is the vector $\vec{PQ}$ given by 
$$\vec{PQ} = (-1-2)\hat{i}+(-2-3)\hat{j}+(-4-0)\hat{k}$$ $$\boxed{\vec{PQ} = -3\hat{i}-5\hat{j}-4\hat{k}.}$$</div>

(c) Find the angle $\theta$ between the vectors $\vec{a} = \hat{i}+\hat{j}-\hat{k}$ and $\vec{b}=\hat{i}-\hat{j}+\hat{k}$ :

<div class = "answer">The angle $\theta$ between two vectors $\vec{a}$ and $\vec{b}$ is given by $$\cos{\theta} = \frac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}$$ $$\vec{a}\cdot\vec{b} = (\hat{i}+\hat{j}-\hat{k})\cdot (\hat{i}-\hat{j}+\hat{k})=-1$$ $$|\vec{a}||\vec{b}|=\sqrt{1^2+1^2+(-1)^2}\sqrt{1^2+(-1)^2+1^2}=\sqrt{3}\times\sqrt{3}=3$$ Therefore, we have $$\cos\mathrm{\theta} = -\frac{1}{3}$$ Hence,the required angle is $$\boxed{ \theta =\cos^{-1}(-\frac{1}{3}) = 109.5^{\circ} .}$$</div>

(d) If $\vec{a} = 5\hat{i}-\hat{j}-3\hat{k}$ and $\vec{b} = \hat{i}+3\hat{j}-5\hat{k}$,  then show that the vectors $\vec{a}+\vec{b}$ and $\vec{a}-\vec{b}$ are perpendicular.

<div class = "answer">Two non-zero vectors are perpendicular if their scalar product is zero. 
$$\vec{a}+\vec{b} = (5\hat{i}-\hat{j}-3\hat{k})+(\hat{i}+3\hat{j}-5\hat{k})=6\hat{i}+2\hat{j}-8\hat{k}$$
$$\vec{a}-\vec{b} =(5\hat{i}-\hat{j}-3\hat{k})-(\hat{i}+3\hat{j}-5\hat{k})=4\hat{i}-4\hat{j}+2\hat{k}$$
Therefore, we have:
$$\boxed{(\vec{a}-\vec{b})\cdot(\vec{a}+\vec{b}) =(6\hat{i}+2\hat{j}-8\hat{k})\cdot(4\hat{i}-4\hat{j}+2\hat{k})=24-8-16=0}$$</div>

(e) Show the points $A(-2\vec{i}+3\vec{j}+5\vec{k})$, $B(\vec{i}+2\vec{j}+3\vec{k})$, and $C(7\vec{i}-\vec{k})$ are collinear (They lie on the same straight line).

<div class = "answer">We have $$\vec{AB}=(1+2)\hat{i}+(2-3)\hat{j}+(3-5)\hat{k}=3\hat{i}-\hat{j}-2\hat{k},$$ $$\vec{BC}=(7-1)\hat{i}+(0-2)\hat{j}+(-1-3)\hat{k}=6\hat{i}-2\hat{j}-4\hat{k},$$ $$\vec{CA}=(-2-7)\hat{i}+(3-0)\hat{j}+(5+1)\hat{k}=-9\hat{i}+3\hat{j}+6\hat{k},$$ $$|\vec{AB}|=\sqrt{14}, |\vec{BC}|=2\sqrt{14}, $$ and $$|\vec{AC}|=3\sqrt{14},$$
Therefore, $$\boxed{|\vec{AC}|=|\vec{AB}|+|\vec{BC}|.}$$</div>

(f) Find $|\vec{a}\times\vec{b}|,$ if $\vec{a}=2\vec{i}+\vec{j}+3\vec{k}$ and $\vec{b}=3\vec{i}+5\vec{j}-2\vec{k}$

<div class = "answer">We have
$$\vec{a}\times\vec{b}=$$ $$\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
2 & 1 & 3 \\
3 & 5 & -2 \\
\end{vmatrix}$$ Therefore, $$\vec{a}\times\vec{b}= \hat{i}(-2-15)-(-4-9)\hat{j}+(10-3)\hat{k}=-17\hat{i}+13\hat{j}+7\hat{k}$$
Hence, $$|\vec{a}\times\vec{b}|=\sqrt{(-17)^2+(13)^2+(7)^2}= \boxed{\sqrt{507}.}$$ </div>

-----------------------------------

## Exam Style Questions
### Problem n.

-----------------------------------

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">hide all answers</button>


## Challenging Questions
### Problem n.