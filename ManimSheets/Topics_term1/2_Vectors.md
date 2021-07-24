# [Manim Visualisations](../ManimVisualisations.md) |  Vectors
[Source Code](./02-vectors-files/vectors.py)

<style> 
  video {
    width: 720px;
    height: 480px;
    display: block;
    margin: 0 auto;
</style> 

### Dot Product
Here is a visual proof that the dot product is the length of the projection of one vector (can be thought as the component of the vector in the direction of the other vector), multiplied by the length of the other vector. This is irrespective of which vector you choose to project. Try multiplying the values displayed by the animation.
 
<video controls>
  <source src="./02-vectors-files/DotProduct.mp4" type="video/mp4">
</video>
<br />

### Cross Product
Plots the cross product and pans the camera around it. You can see how the cross product is always orthogonal to the vectors. The magnitude of the cross product is the same as the area of the parallelogram drawn by the two vectors. If the angle between the two vectors changes, so does the area and hence magnitude of the cross product. If the vectors are mirrored diagonally in their plane, the area is the same, but the cross product vector swaps direction, being negative. This is related to negative area linear transformations which will be taught later.

<video controls>
  <source src="./02-vectors-files/CrossProduct.mp4" type="video/mp4">
</video>
<br />

This render is particularly resource intensive, especially if the 3D Arrows are used. 

### Distance between two lines

###### For any mistakes or queries please do not hesitate to email me at cav20@ic.ac.uk
