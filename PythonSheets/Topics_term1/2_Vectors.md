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

# Python Tutorial

## What is Python?

<!-- Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed. -->

<br>

## Setup guide

To use Python to solve problems in this course we will need to download the latest version of Python and Numpy.

### Installing Python on Windows

Download and follow the installation instructions from https://www.python.org/downloads/.

When installing make sure to tick the box to add Python to PATH.

### Installing Python on MacOS

1. Open Terminal from the Applications list
2. Install HomeBrew by typing the following command in the terminal window and hit enter

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Install pyenv to manage Python versions on Mac

```bash
brew install pyenv
pyenv install 3.8.5
pyenv global 3.8.5
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

### Installing extra modules

To manipulate matrices we will need to install the Numpy module.

You can do this by typing the following command in the terminal prompt

```bash
pip install numpy
```

---
**NOTE**

If command above fails try 

```bash
pip3 install numpy
```

---

The easiest way to solve simple mathematical problems in Python is by using the Python interpreter. It can be accessed by opening a Terminal window and typing in `python` or `python3`. Alternatively you could write your code in an editor such as VScode and run it from there.

<br>

## Vectors

The easiest way to manipulate vectors in Python is by using the Numpy module, you can import it with

```python
import numpy as np
```

Make sure to do this every time you start a new Python interpreter or at the start of your code.

### Writing vectors

The vector $\vec{a}= (2,1,0)$ can be written as


```python
a = np.array([2, 1, 0])
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/ba8f7fa714?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

</details>

### Adding and subtracting vectors

Vectors can be added and subtracted like numbers in python using `+` and `-`.

For example:

```python
a = np.array([2, 1, 0])
b = np.array([6, 0, 4])

add = a + b 
subtract = a - b
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/eb9b29368a?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

</details>

### Modulus of a vector

The modulus of a vector can be calculated with `np.linalg.norm(v)`

For example, the modulus product of $\vec{a}= (2,1,0)$ would be written as

```python
a = np.array([2, 1, 0])
np.linalg.norm(a)
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/8c52e77947?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

</details>


### Dot product

Dot products can be easily computed with `np.dot(u, v)`

For example, the dot product of $\vec{a}= (2,1,0)$ and $\vec{a}= (6,0,4)$ would be written as

```python
a = np.array([2, 1, 0])
b = np.array([6, 0, 4])
np.dot(a, b)
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/41218a1817?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

</details>

### Cross product

Cross products can be easily computed with `np.cross(u, v)`

For example, the cross product of $\vec{a}= (2,1,0)$ and $\vec{a}= (6,0,4)$ would be written as

```python
a = np.array([2, 1, 0])
b = np.array([6, 0, 4])
np.cross(a, b)
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/c38197d4b9?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

</details>

<br>

## Matrices