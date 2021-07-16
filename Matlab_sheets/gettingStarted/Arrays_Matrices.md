# Arrays and Matrices
Matlab is an abbreviation for **MAT**rix **LAB**oratory, it has been purely designed to work with matrices and arrays. In fact, all of the data types we saw  earlier are *secretly arrays*.

## Array creation
To create an array use the square brackets "**[ ]**", to separate elements you can use either "**,**" or spaces. Both methods are equally valid.
```matlab:Code
a = [1, 3, 9, 8]
b = [2 4 6 4]
```
The above arrays have only 1 one row, they are also known as **Row vectors**.

To add new rows to your arrays use "**;**" :
```matlab:Code
c = [1 6; 4 2]
```

There are also ways of creating matrices using functions like **zeros(Rows, Cols)** or **rand(Rows, Cols)**.
```matlab:Code
d = zeros(3,2)
e = rand(2,1)
```

## Operations

- **Element-wise addition** adds x number to each entry of the array.
    ```matlab:Code
    a + 5
    ```
 - **Apply functions**, some functions accept arrays as inputs and perform their function element-wise.
    ```matlab:Code
    sin(a)
    ```
- **Transpose Matrix** can be done using the " **'** " operator.
    ```matlab:Code
    a'
    ```
- **Matrix multiplication** is done as expected using the "*" operator, it will only happen when multiplication between the two matrices is possible of course.
    ```matlab:Code
    c * e
    ```
- **Element-wise multiplication, division and to the power-of** are done with their respective operator with a "." preceding them: ".*", "./" and ".^".
    ```matlab:Code
    a .* 3
    a ./ 3
    a .^ 2
    ```
## Concatenation
Arrays must have the same number of rows if they want to be concatenated horizontally and the same number of columns if vertically. Essentially you create a matrix with matrices.
```matlab:Code
f = [c, e]
g = [a; b]
```

## Indexing
**Matlab unlike python starts indexing at 1 instead of 0!**

To index an item from an array, the row and columns should be specified. To access the element from the 2nd row, 1st column you should:
```matlab:Code
c(2,1)
```
If you desire to obtain an entire row or column use the **:** symbol. This extracts the whole 1st column of the c array.
```matlab:Code
c(:,1)
```

###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco