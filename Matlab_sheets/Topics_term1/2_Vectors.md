# Vectors
## Plotting
- **plotv(M)** generates 2 Dimensional plot of vectors from the origin, the input argument M is a matrix that contains the x components of the vectors in the first row and the second row contains the y components of the vectors: M = [x1 x2; y1 y2]. [More documentation needed]()
```matlab:Code
M = [2 3 5; 1 2 3];
plotv(M)
``` 
Image

- **plot3(X,Y,Z)** can be used to plot points on 3D space, X Y Z have to be arrays of equal size. The points are connected with a line [More documentation needed]()
```matlab:Code
X = [4 5 7];
Y = [1 6 5];
Z = [8 4 2];
plot3(X,Y,Z)
```
Image

- **quiver3(X,Y,Z,U,V,W)** plots 3D arrows starting from the coordinates X Y Z with directional vector components of U V W. [More documentation needed]()

```matlab:Code
X = [0 0 0];
Y = [5 -2 1];
Z = [1 3 5];
U = [2 2 2];
V = [3 3 3];
W = [-1 -1 -1];
quiver3(X,Y,Z,U,V,W)
```
Image

## Vector operations
- **dot(v1,v2)** performs the dot product of two vectors, they both should have the same size. [More documentation needed]()
```matlab:Code
v1 = [1 2 5];
v2 = [2 5 2];
dot(v1,v2)
```

- **cross(v1,v2)** performs the cross product of two vectors, the vectors should be of length 3. [More documentation needed]()
```matlab:Code
cross(v1,v2)
```

- **norm(v1)** calculates the magnitude of an array or vector. [More documentation needed]()
```matlab:Code
norm(v1)
```
To calculate the unit vector of a vector then simply:
```matlab:Code
unitv1 = v1/norm(v1)
```

###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco
