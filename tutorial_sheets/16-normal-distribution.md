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

# Normal Distribution Tutorial Sheet, #16

This particular tutorial sheet is short. Do not be alarmed! It reflects the low difficulty of the topic. 

### Learning Outcomes
* Use the general normal distribution equation to determine probabilities
* Sketch bell-curves noting standard deviations
* Use probabilities to determine standard deviation and mean


<br><br>

# Additional Resources

## Tutorials
* [Gaussian](https://www.youtube.com/watch?v=26QbWYBCw7Y) : Extra video by Sam recapping the Gaussian from the lecture.
* [Summary Sheet](https://www.physicsandmathstutor.com/pdf-pages/?pdf=https%3A%2F%2Fpmt.physicsandmathstutor.com%2F%2Fdownload%2FMaths%2FA-level%2FStatistics%2FStatistical-Distributions-2%2FCheat-Sheets%2FNormal%2520Distribution.pdf) : An summary sheet of all we learnt. However remember we can use technology!

## Software 

* [WolframAlpha](https://onlinestatbook.com/2/calculators/normal_dist.html) : A nifty probability calculator with visualisations on the graph itself.

In the answers, some wolfram alpha pages are linked in
[blue](https://www.youtube.com/watch?v=dQw4w9WgXcQ) like this
<br><br>


# Problem sheet
## Essential Questions
### Problem 1.
Alex took a test and scored 940. The mean score was 850 with the standard deviation of 100.

(a) Draw a Gaussian/Bell Curve for this Data and highlight area higher than Alex's score. Include all given information on the diagram.

<div class = "answer">

<img src = "16-normal-distribution/1a.png">

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(b) If there were a total of 200 students taking the test, how many would be expected to get a higher mark than Alex?
<div class  = "answer">
$\Rightarrow{} P(X>940)=1 - \left[\frac{1}{2} \left(1 + \text{ erf}\ \left(\frac{\ 940\ -\ 850}{100\ \sqrt{2}} \right)\right)\right]$ <br>

$\Rightarrow{} P(X>940)=1-0.81594=0.18406$ %<br>

$\Rightarrow{} 0.18406\times 200=36.81$ students <br>

$\Rightarrow{}$ rounding down: $\boxed{\text{ only 36 students are expected to be higher }}$ <br>
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(c) If the failing mark for this test was 600, how many of the 200 students would be expected to failed the test? Show this on your diagram

<div class = "answer" >
$ \Rightarrow{} P(X < 600)=\left[\frac{1}{2} \left(1 + \text{ erf}\ \left(\frac{\ 600\ -\ 850}{100\ \sqrt{2}} \right)\right)\right] $
<br>

$ \Rightarrow{} P(X < 600)=0.006=0.6\% $
<br>

$ \Rightarrow{} \boxed{ 1 \text{ Student} }$

<br>

<img src = "16-normal-distribution/1c.png">

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><br></div>

-----------------

### Problem 2.
According to a survey from 100 undergraduate students, only 5 students were graduated with a grade above 70%. If the average student grade was 55%:

(a) Draw a Gaussian/Bell Curve for the given Data.
<div class = "answer">

<img src = "16-normal-distribution/2a.png">

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(b) Using the given data, find the standard deviation for the graduation grades.

<div class = "answer">

$ \Rightarrow{} P(X>70)=[\frac{1}{2}{({1{-{ \text{ erf}\ {(\frac{\ 70\ -\ 55}{\sigma\ \sqrt{2}})}}}}}]=5\% $ <br>

$ \Rightarrow{} P(X>70)={0.5{ \text{ erf }{(\frac{\ 70\ -\ 55}{\sigma\ \sqrt{2}})}}}=0.45 $ <br>


$ \Rightarrow{} \text{erf }(x) =0.9 $ <br>

$ \Rightarrow{} x =$ <a href="https://www.wolframalpha.com/input/?i=erf%28x%29%3D0.9+solve">$ 1.16 $</a> <br>

<a href="https://www.wolframalpha.com/input/?i=1.16+%3D+%2870-55%29%2F%28x*sqrt%282%29%29+solve">$ \Rightarrow{} 1.16={\frac{\ 70\ -\ 55}{\sigma\ \sqrt{2}}}$</a> <br>

$ \Rightarrow{} \boxed{ SD = \sigma =8.64}$

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>
(c) If the failing grade is to be 40%, how many students would possibly fail the course? Show this on the diagram as well.

<div class = "answer">
$\Rightarrow{} P(X < 40)=\frac{1}{2}{\left({1{+{\text{ erf}\ {\left(\frac{\ 40\ -\ 55}{8.64\ \sqrt{2}}\right)}}}}\right)} $

$\Rightarrow{} P(X<40)=0.049=5% $ <br>

$\Rightarrow{} \boxed{ 5 \text{ Students}}$ <br>

<img src = "16-normal-distribution/2c.png">

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(d) How many students would be expected to pass the course below 60%? Add this to your diagram.
<div class = "answer" >
$ \Rightarrow{} P(40< X < 60)=P(X < 60)-P(X < 40)  $ 
<br>
$ \Rightarrow{} P(40 < X < 60)= \frac{1}{2}\left[\text{ erf}\left(\frac{60-55}{8.64\ \sqrt{2}}\right)- \text{ erf}\left(\frac{40-55}{8.64\ \sqrt{2}}\right)\right] $ 
<br>
$ \Rightarrow{} P(40 < X < 60)=0.678=68 \%  $ 
<br>
$ \Rightarrow{} \boxed{68\ \text{ Students}}$ <br>


<img src = "16-normal-distribution/2d.png">
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><br></div>

-----------------

### Problem 3.
A Packing plant fills bags with cement. The mean weight of these bags is 50kg with standard deviation of 4kg.

(a) Draw a Gaussian/Bell Curve for the given Data.

<div class = "answer">

<img src = "16-normal-distribution/3a.png">

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(b) Find the probability of bags exceeding 53kg.

<div class = "answer" >
$ \Rightarrow{} P(X>53)= 1 - \left[\frac{1}{2} \left( 1 + \text{ erf}\ \left(\frac{\ 53\ -\ 50}{4\ \sqrt{2} }\right) \right) \right] $ <br>

$ \Rightarrow{} \boxed{ P(X>53)= 0.23=23 \\ }$ 
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(c) Find the weight that is exceeded by 82% of the bags.

<div class = "answer" >
$ \Rightarrow{} P(X>Y)=[\frac{1}{2}{({1{-{\text{ erf}\ {(\frac{\ Y\ -\ 50}{4\ \sqrt{2}})}}}})}]=82\% $ <br>

$ \Rightarrow{} P(X>Y)=0.32={ {-\frac{1}{2}}{\text{ erf}(x)}} $ <br>

$ \Rightarrow{} x =$ <a href="https://www.wolframalpha.com/input/?i=solve+0.32%3D-0.5*erf%28x%29"> $-0.65$</a> <br>

$ \Rightarrow{} -0.65={(\frac{\ Y\ -\ 50}{\ 4\ \sqrt{2}})}$ <br>

$ \Rightarrow{} Y = $ <a href="https://www.wolframalpha.com/input/?i=-0.65%3D%28y-50%29%2F%284*sqrt%282%29%29">$ 46.32 $</a> <br>

$ \Rightarrow{} \boxed{ \text{ Weight } =46.32 }$ <br>

<img src = "16-normal-distribution/3c.png">
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(d) Three bags were randomly selected. Find the probability that two bags weigh more than 53kg and one weighs less than 53kg.
<div class = "answer">
$\Rightarrow{} P(X>53)=23\% $ and $P(X < 53)=77\%$ <br>
$\Rightarrow{} \text{ Probability } =P ( X>53)\times\ P(X>53)\times\ P(X < 53)= 0.23\times\ 0.23\times\ 0.77$ <br>
$\Rightarrow{} \boxed{ \text{Probability} = 4 \% }$ 
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><br></div>

-----------------

### Problem 4.
A high-Jumper can clear a jump higher than 1.78m once in every five attempts. This jumper can also clear a height of at least 1.65m on 7 out of 10 attempts:

(a) Draw a Gaussian/Bell Curve for the given Data with highlighting the jumps over 1.78. 

<div class = "answer">

<img src = "16-normal-distribution/4a.png">

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

(b) Find the mean and the standard deviation of the heights the athlete can reach.

<div class = "answer">
$ \Rightarrow{} P(X>1.78)={1-[\frac{1}{2}{({1{+{\text{ erf} \ {(\frac{\ 1.78\ -\ \alpha}{\sigma\ \sqrt{2}})}}}})}]}=20\%$ <br>

$ \Rightarrow{} 2(1-0.2)-1 = \text{ erf} \ {(\frac{\ 1.78\ -\ \alpha}{\sigma\ \sqrt{2}})} = 0.6$ <br>

$ \Rightarrow{} \text{erf }(x) = 0.6 \Rightarrow{} x = $ <a href="https://www.wolframalpha.com/input/?i=erf%28x%29%3D0.6+solve">$ 0.60$</a> <br>

<!-- $ \Rightarrow{} 0.3={\frac{1}{2}{( \text{ tanh}(1.2x))}}$ <br> -->

$ \Rightarrow{} x=0.6={(\frac{\ 1.78\ -\sigma}{\alpha\ \sqrt{2}})}$ <br>

$ \Rightarrow{} \alpha={ {(1.78)}-{(\sigma\times\ 0.6\times\ \sqrt{2})}}$ <br>

Also, 

$ \Rightarrow{} \text{  } P(X>1.65)={1-[\frac{1}{2}{({1{+{ \text{ erf}\ {(\frac{\ 1.65\ -\ \alpha}{\sigma\ \sqrt{2}})}}}})}]}=70\%$ <br>

$ \Rightarrow{} 2(1-0.7)-1 = \text{ erf} \ {(\frac{\ 1.78\ -\ \alpha}{\sigma\ \sqrt{2}})} = -0.4$ <br>

$ \Rightarrow{} \text{erf }(x) = -0.4 \Rightarrow{} x = $ <a href="https://www.wolframalpha.com/input/?i=erf%28x%29%3D-0.4+solve">$ -0.37$</a> <br>

$ \Rightarrow{} \alpha={ {(1.65)}-{(\sigma\times\ (-0.37)\times\ \sqrt{2})}}$ <br>

$ \Rightarrow{} { {(1.78)}-{(\sigma\times\ 0.6\times\ \sqrt{2})}}={ {(1.65)}-{(\sigma\times\ (-0.37)\times\ \sqrt{2})}}$ <br>

$ \Rightarrow{} 1.78-1.65={(\sigma\times\ \sqrt{2})\times\ {(0.37+0.6)}}$ <br>

$ \Rightarrow{} \boxed{ \sigma = \frac{0.13}{\sqrt{2}\times\ 0.97}=0.09m }$ <br>

$ \Rightarrow{} \alpha={ {(1.78)}-{(0.09\times\ 0.6\times\ \sqrt{2})}}$ <br>

$ \Rightarrow{} \boxed{ \alpha=1.7m }$
</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><br></div>

## Exam Questions

### Problem 5.
Due to imperfect manufacturing of circuit laundry machines, their wash times can vary. The machine displays a time of 50 minutes for colors at $40 ^\circ $ but truly has a standard deviation of 17 minutes and 15 seconds around that time. 

(a) Sketch a graph of the wash time for colors at $40 ^\circ $ distribution. Shade the region showing the 80% most reliable wash times and label the duration interval.

<div class = "answer">

Most reliable wash times are around the mean (50 min) interval corresponds to everything but the extreme 10% (upper and lower). 

Upper 10%:

$ \Rightarrow{} P(X>Y)=[\frac{1}{2}{({1{-{\text{ erf}\ {(\frac{\ Y\ -\ 50}{17.25\ \sqrt{2}})}}}})}]=10\% $ 

Solve for Y:

<a href="https://www.wolframalpha.com/input/?i=0.5%281-erf%28%28y-50%29%2F%2817.25*sqrt%282%29%29%29%29+%3D+0.1+solve+y">$ Y = 72.1$</a>

Lower 10%:

$ \Rightarrow{} P(X>Y)=[\frac{1}{2}{({1{+{\text{ erf}\ {(\frac{\ Y\ -\ 50}{17.25\ \sqrt{2}})}}}})}]=10\% $ 

<a href="https://www.wolframalpha.com/input/?i=0.5%281%2Berf%28%28y-50%29%2F%2817.25*sqrt%282%29%29%29%29+%3D+0.1+solve+y">$ Y = 27.9$</a>


<img src = "16-normal-distribution/5a.png">


</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><br></div>

(b) If Imperial College London buys an army of 12 laundry machines for the entirety of Southside Halls and its 350 students, how many of the machines can be expected to have a wash time of more than 60 minutes?
<div class = "answer">

$ \Rightarrow{} P(X>60)=[\frac{1}{2}{({1{-{\text{ erf}\ {(\frac{\ 60\ -\ 50}{17.25\ \sqrt{2}})}}}})}]=0.2811\% $ 

$ 12 * 0.2811 = 3.37 $

$\boxed{3 \text{ machines}}$

<img src = "16-normal-distribution/5b.png">

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br><br></div>

(c) How many of the machines are expected to have a $\pm2$ min accuracy with their colors at $40 ^\circ $ cycles?
<div class = "answer">

$ \Rightarrow{} P(48< X < 52)=P(X < 52)-P(X < 48)  $ 
<br>

$ \Rightarrow{} P(48 < X < 52)= \frac{1}{2}\left[\text{ erf}\left(\frac{52-50}{17.25\ \sqrt{2}}\right)- \text{ erf}\left(\frac{48-50}{17.25\ \sqrt{2}}\right)\right] $ 
<br>

$ \Rightarrow{} P(48 < X < 52)=0.0923$ 
<br>

$\Rightarrow{}0.0923*12 = 1.1076$

$ \Rightarrow{} \boxed{1\ \text{ machine}}$ <br>

<img src = "16-normal-distribution/5c.png">

</div>
<div class = "workingout"><br><br><br><br><br><br><br><br></div>

-----------------

## Answers

<button id="showAnswerButton" type="button" onclick="displayAnswerButtons('block')">Show answer buttons</button>
<button style="display: none" id="hideAnswerButton" type="button" onclick="displayAnswerButtons('none')">Hide answer buttons</button>
<button id="showAnswers" type="button" onclick="displayAnswers('block')">Show all answers</button>
<button style="display: none" id="hideAnswers" type="button" onclick="displayAnswers('none')">Hide all answers</button>
<br><br>

## For Printing
<button id="showPrint" type="button" onclick="prepareForPrint('block')">Add whitespace</button>
<button style="display: none" id="hidePrint" type="button" onclick="prepareForPrint('none')">Remove whitespace</button>

<br><br>

# Revision Questions 

The questions included are optional, but here if you want some extra practice.

* [Engineering Mathematics 7th edition, Stroud and Dexter](https://library-search.imperial.ac.uk/discovery/search?query=any,contains,Engineering%20Mathmematics%20Stroud&tab=all&search_scope=MyInst_and_CI&sortby=date_d&vid=44IMP_INST:ICL_VU1&facet=frbrgroupid,include,9069308747175707749&lang=en&offset=0) : Pages 1106-1116
* [Advanced Engineering Mathematics 5th edition, Stroud and Dexter](https://library-search.imperial.ac.uk/discovery/fulldisplay?docid=alma9956105299701591&context=L&vid=44IMP_INST:ICL_VU1&lang=en&search_scope=MyInst_and_CI&adaptor=Local%20Search%20Engine&tab=all&query=any,contains,Engineering%20Mathmematics%20Stroud&offset=0) : Pages 755-758
* [Easy Questions](https://www.physicsandmathstutor.com/pdf-pages/?pdf=https%3A%2F%2Fpmt.physicsandmathstutor.com%2F%2Fdownload%2FMaths%2FA-level%2FStatistics%2FStatistical-Distributions-2%2FOCR-Set-A%2FThe%2520Normal%2520Distribution.pdf) : A set of quite easy A-Level questions.
* [More Easy Questions](https://www.physicsandmathstutor.com/pdf-pages/?pdf=https%3A%2F%2Fpmt.physicsandmathstutor.com%2F%2Fdownload%2FMaths%2FA-level%2FStatistics%2FStatistical-Distributions-2%2FEdexcel-Set-A%2FNormal%2520distribution.pdf) : More A-Level questions, you can use these for 'learning by rote'.

<br><br>

# The end :) Enjoy your Easter break!