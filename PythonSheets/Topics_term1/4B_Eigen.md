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

# Eigenproblems

Eigenproblems can easily be solved with the Numpy module. So make sure it is imported in your code:

```python
import numpy as np
```

## Calculating eigenvalues and eigenvectors

Here are the functions you can use:

- `np.linalg.eigh(m)` returns the eigenvalues and eigenvectors of a matrix

Example:

```python
import numpy as np

a = np.array([[1, -2], [2, 5]])

w, v = np.linalg.eigh(a)

print("Eigenvalues = ", w)
print("Eigenvectors = ", v)
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/9873d08a31?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>