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

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCgphID0gbnAuYXJyYXkoW1sxLCAtMl0sIFsyLCA1XV0pCgp3LCB2ID0gbnAubGluYWxnLmVpZ2goYSkKCnByaW50KCJFaWdlbnZhbHVlcyA9ICIsIHcpCnByaW50KCJFaWdlbnZlY3RvcnMgPSAiLCB2KQo&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
</details>