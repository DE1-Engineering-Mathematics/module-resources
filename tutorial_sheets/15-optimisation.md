<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], [" \newline("," \newline)"] ],
      processEscapes: true
    }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/javascript" src="tutorialSheetScripts.js"> </script>
<link rel="stylesheet" type="text/css" media="all" href="styles.css">

# Optimisation Tutorial Sheet, #15

<br><br><br><br>

# Problem sheet
## Essential Questions
### Problem 1.
Find the line of best fit, using minimised sum squared residuals, of the form $y=mx+c$, through the following three points: (2,1), (3,5) and (7,9). Plot the resulting curve, points and residuals.

<div class = "answer">
Taking the equation for linear regression directly from notes:

\begin{equation*}
    m = \frac{\sum(x_i-\bar{x})y_i}{\sum(x_i-\bar{x})^2}
\end{equation*}
\begin{equation*}
    c = \bar{y} - m\bar{x}
\end{equation*}

For each of the values that need to be summed or averaged from the points given in the question, we can create a table:

\begin{align*}
& &    &x&       &y&     (x_i&-\bar{x})y_i&    (x_i&-\bar{x})^2& \newline
\hline
& &    &2&       &1&              -&2&       &4& \newline
& &    &3&  &5&  -&5&   &1&   \newline
& &   &7&  &9&  &27&          &9& \newline
& Mean&   & 4&  &5&     & &        & & \newline
& Sum&   & 12&   & 15&   & 20&   & 14& 
\end{align*}

Using these values to calculate $m$ and $c$:
$$
m = \frac{20}{14} = \frac{10}{7} \approx 1.43 \ (3 \ s.f.)
$$

$$
c = 5 - (\frac{10}{7} \times 4) = -\frac{5}{7} \approx -0.714 \ (3 \ s.f.)
$$

$$
\boxed{ \therefore y = 1.43x - 0.714 }
$$
<img src = "13-optimisation/optimisation_graphic_1.png">

Additional lines added for the curious.
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

### Problem 2.
Find the line of best fit, using minimised sum squared residuals, of the form $y = ax^2 + b$, through the points (2,1), (3,5), and (7,9). Plot the resulting cure, points, and residuals.

<div class = "answer">
Still a linear regression problem as the function is linear within it's parameters.

$$
S = \sum_{i=1}^{3} (y_i - f(x_i))^2 = \sum_{i=1}^{3} (y_i - ax^2 - b)^2
$$

$$
\frac{\partial{}S}{\partial{}a} = 2 \sum_{i=1}^{3} (-x_i^2)(y_i - ax_i^2 - b) = 0
$$

$$
\frac{\partial{}S}{\partial{}b} = 2 \sum_{i=1}^{3} (-1)(y_i - ax_i^2 - b) = 0
$$

Rearranging:

$$
\sum_{i=1}^{3} (-y_ix_i^2 + ax_i^4 + bx_i^2) = 0, \ \ \therefore
$$

$$
a = \frac{\sum_{i=1}^{3} (y_ix_i^2 - bx_i^2)}{\sum_{i=1}^{3} (x_i^4)} = \frac{\sum_{i=1}^{3} (y_ix_i^2) - b \sum_{i=1}^{3}(x_i^2)}{\sum_{i=1}^{3} (x_i^4)}
$$

$$
\sum_{i=1}^{3} (y_i - ax_i^2 - b) = 0, \therefore
$$

$$
b = \frac{1}{n} \sum_{i=1}^{3} (y_i) - \frac{a}{n}\sum_{i=1}^{3} (x_i^2)
$$

\begin{align*}
& &    &x&       &y&     &x_i^4&   &x_i^2&   x&_i^2y_i& \newline
\hline
\newline
& &    &2&   &1&     &16&       &4&   &4& \newline
& &    &3&   &5&     &81&       &9&   &45& \newline
& &    &7&   &9&    &2401&      &49&  &441& \newline
& Mean&   &4&    &5&     & &        & &   & & \newline
& Sum&    &12&   &15&   &2498&   & 62& &490&
\end{align*}

<br>

$$
a=\frac{490 - 62b}{2498} \therefore 2498a + 62b =490 
$$

$$
b=\frac{1}{3} \times 15 - \frac{a}{3} \times 62 \therefore 62a + 3b = 15
$$

$$
\begin{bmatrix}
2498 & 62 \newline
62 & 3
\end{bmatrix}
\begin{bmatrix}
a \newline
b
\end{bmatrix}
= \begin{bmatrix}
490 \newline
15
\end{bmatrix}
$$

$$
\begin{bmatrix}
a \newline
b
\end{bmatrix}
= \begin{bmatrix}
0.1479 \newline
1.9425
\end{bmatrix}
$$

<img src = "13-optimisation/optimisation_graphic_2.png">

Additional lines added for the curious.
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

### Problem 3.
Find the line of best fit, using minimised sum squared residuals, of the form $y=ae^x+b$, through the points (2,1), (3,5) and (7,9). Plot the resulting curve, points and residuals.

<div class = "answer">
Still a linear regression problem as the function is linear within it's parameters.}

$$
S = \sum_{i=1}^{3} (y_i - f(x_i))^2 = \sum_{i=1}^{3} (y_i - ae^{x_i} - b)^2
$$

$$
\frac{\partial{}S}{\partial{}a} = 2 \sum_{i=1}^{3} (-e^{x_i})(y_i - ae^{x_i} - b) = 0
$$

$$
\frac{\partial{}S}{\partial{}b} = 2 \sum_{i=1}^{3} (-1)(y_i - ae^{x_i} - b) = 0
$$

Rearranging:

$$
\sum_{i=1}^{3} (-y_ie^{x_i} + ae^{2x_i} + be^{x_i}) = 0, \ \ \therefore
$$

$$
a = \frac{\sum_{i=1}^{3} (y_ie^{x_i} - be^{x_i})}{\sum_{i=1}^{3} (e^{2x_i})} = \frac{\sum_{i=1}^{3} (y_ie^{x_i}) - b \sum_{i=1}^{3}(e^{x_i})}{\sum_{i=1}^{3} (e^{2x_i})}
$$

$$
\sum_{i=1}^{3} (y_i - ae^{x_i} - b) = 0, \ \ \therefore
$$

$$
b = \frac{1}{n} \sum_{i=1}^{3} (y_i) - \frac{a}{n}\sum_{i=1}^{3} (e^{x_i})
$$

\begin{align*}
& &    &x&       &y&     &e^{x_i}&   &e^{2x_i}&   e&^{x_i}y_i& \newline
\hline
 \newline
& &    &2&   &1&     &e^2&       &e^4&   &e^2& \newline
& &    &3&   &5&     &e^3&       &e^6&   &5e^3& \newline
& &    &7&   &9&    &e^7&      &e^{14}&  &9e^7& \newline
& Mean&   &4&    &5&     & &        & &   & & \newline
& Sum&    &12&   &15&   &c.1124&   &c.1.2E6& &c.9978&
\end{align*}

<br>

$$
a = \frac{9978 - 1124b}{1.2E6} \therefore 1.2E6a + 1124b = 9978
$$

$$
b = \frac{1}{3} \times 15 - \frac{a}{3} \times 1124 \therefore 62a + 3b = 1
$$

$$
\begin{bmatrix}
1.2E6 & 1124 \newline
1124 & 3
\end{bmatrix}
\begin{bmatrix}
a \newline
b
\end{bmatrix}
= \begin{bmatrix}
9978 \newline
15
\end{bmatrix}
$$

$$
\begin{bmatrix}
a \newline
b
\end{bmatrix}
= \begin{bmatrix}
0.0056 \newline
2.91
\end{bmatrix}
$$

<img src = "13-optimisation/optimisation_graphic_3.png">

Additional lines added for the curious.

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

### Problem 4.
The following contour plot shows the summed square error, S, for the two-parameter fit to some data for the function $f(x)=ae^{-x^2}+b$.

![figure1](13-optimisation/optimisation_graphic_4.png)

(a) Make a sketch of the curve corresponding to the best fit parameters suggested by the contour plot.


(b) On the same axis, sketch the curves corresponding to the “\&” and “\%” points from the contour plot.


(c) Add five example data points to your sketch that could reasonably have been responsible for this contour plot.

<div class = "answer">

<img src = "13-optimisation/optimisation_graphic_5.png">

</div>

<div class = "workingout"><br><br><br><br><br><br><br><br><P style="page-break-before: always"></div>


## Answers

<button type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button type="button" onclick="displayAnswers('block')">Show all answers</button>
<button type="button" onclick="displayAnswers('none')">Hide all answers</button>
<br><br>
### For Printing
<button type="button" onclick="prepareForPrint('block')">Add whitespace</button>
<button type="button" onclick="prepareForPrint('none')">Remove whitespace</button>

<br><br>

# Next week, the Normal Distribution!