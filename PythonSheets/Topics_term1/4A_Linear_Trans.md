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

# Linear transforms

As linear transforms are simply multiplications of matrices, you've already seen the tools needed to solve these types of problems in the matrices chapter.

## Plotting vectors

It can often be beneficial to plot vectors to get a visual representation of your results.

This can be done using the `plt.quiver` function of matplotlib.

Here is an example:

```python
import numpy as np
import matplotlib.pyplot as plt

V = np.array([[1,1], [-2,2], [4,-7]])
origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin point

plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
plt.show()
```

<details>
<summary>Try it out</summary>

<iframe src="https://trinket.io/embed/python3/1d77dba42d?outputOnly=true&runOption=console&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
```

</details>