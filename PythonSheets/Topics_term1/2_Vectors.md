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

## Writing vectors

The vector $\vec{a}= (2,1,0)$ can be written as

```python
a = np.array([2, 1, 0])
```

<details>
<summary>Try it out</summary>

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCgphID0gbnAuYXJyYXkoWzIsIDEsIDBdKQpwcmludChhKQo&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
```

</details>

## Adding and subtracting vectors

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

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCgphID0gbnAuYXJyYXkoWzIsIDEsIDBdKQpiID0gbnAuYXJyYXkoWzYsIDAsIDRdKQoKYWRkID0gYSArIGIKc3VidHJhY3QgPSBhIC0gYgoKcHJpbnQoYWRkKQpwcmludChzdWJ0cmFjdCkK&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
```

</details>

## Modulus of a vector

The modulus of a vector can be calculated with `np.linalg.norm(v)`

For example, the modulus product of $\vec{a}= (2,1,0)$ would be written as

```python
a = np.array([2, 1, 0])
np.linalg.norm(a)
```

<details>
<summary>Try it out</summary>

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCgphID0gbnAuYXJyYXkoWzIsIDEsIDBdKQpwcmludChucC5saW5hbGcubm9ybShhKSkK&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
```

</details>

## Dot product

Dot products can be easily computed with `np.dot(u, v)`

For example, the dot product of $\vec{a}= (2,1,0)$ and $\vec{a}= (6,0,4)$ would be written as

```python
a = np.array([2, 1, 0])
b = np.array([6, 0, 4])
np.dot(a, b)
```

<details>
<summary>Try it out</summary>

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCgphID0gbnAuYXJyYXkoWzIsIDEsIDBdKQpiID0gbnAuYXJyYXkoWzYsIDAsIDRdKQpwcmludChucC5kb3QoYSwgYikpCg&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
```

</details>

## Cross product

Cross products can be easily computed with `np.cross(u, v)`

For example, the cross product of $\vec{a}= (2,1,0)$ and $\vec{a}= (6,0,4)$ would be written as

```python
a = np.array([2, 1, 0])
b = np.array([6, 0, 4])
np.cross(a, b)
```

<details>
<summary>Try it out</summary>

<figure style="margin:0;border:1px solid #e2e8f0;border-radius:8px;overflow:hidden"><iframe src="https://coddy.tech/embed-editor?lang=matplotlib&theme=light&layout=stacked&code=aW1wb3J0IG51bXB5IGFzIG5wCgphID0gbnAuYXJyYXkoWzIsIDEsIDBdKQpiID0gbnAuYXJyYXkoWzYsIDAsIDRdKQpwcmludChucC5jcm9zcyhhLCBiKSkK&credit=0" width="100%" height="420" style="display:block;border:0;width:100%" title="Python code editor by Coddy" loading="lazy"></iframe><figcaption style="box-sizing:border-box;padding:5px 12px;font:11px/1.4 system-ui,-apple-system,sans-serif;color:#64748b;background:#f1f5f9;border-top:1px solid #e2e8f0;text-align:right" dir="ltr">Powered by <a href="https://coddy.tech/embed" target="_blank" rel="noopener" style="color:#0077ff;font-weight:600;text-decoration:none;">Coddy</a></figcaption></figure>
```

</details>
