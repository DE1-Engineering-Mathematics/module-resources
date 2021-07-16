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

# Vectors

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