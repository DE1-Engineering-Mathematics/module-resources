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

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKClYgPSBucC5hcnJheShbWzEsMV0sIFstMiwyXSwgWzQsLTddXSkKb3JpZ2luID0gbnAuYXJyYXkoW1swLCAwLCAwXSxbMCwgMCwgMF1dKSAjIG9yaWdpbiBwb2ludAoKcGx0LnF1aXZlcigqb3JpZ2luLCBWWzosMF0sIFZbOiwxXSwgY29sb3I9WydyJywnYicsJ2cnXSwgc2NhbGU9MjEpCnBsdC5zaG93KCkK&credit=0" width="100%" height="560" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
```

</details>