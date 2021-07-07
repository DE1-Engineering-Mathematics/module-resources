

## Data types
In Matlab variables can be many different things, the most frequent ones you will find are the following:

- **Doubles** are the default numerical type in matlab. They can store negative, decimal, numbers in standard form and arrays. They store numbers in 64 bits double-precision floating-point values. You can also have **singles** which are stored in 32 bits.
```matlab:Code
a = 1
b = -5
c = 2.523
d = 4.6^-6
e = [2, 5]
f = [4, 5, 7;
     2, 1, 8]
```

- **Integers** , which store integer values. There are many different ones such as **int8, int16, int32, int64, uint8, uint16, uin32, uint64** but these are normally used only when you want optimise the computational requirements of your code.

```matlab:Code
g = int8(12)
```

- **Symbolics**, this datatype is not native from Matlab as it actually comes from the [Symbolic Math Toolbox](https://uk.mathworks.com/products/symbolic.html). Symbolics, unlike doubles or symbols, are exact representations of numbers. They are also useful to create _unknowns_ in equations. To create symbolic variables you can use **sym** or **syms**.

This example will create a symbolic variable with the exact value of one fifth

```matlab:Code
h = sym(1/5) 
``` 

This example will create 3 symbolic variables: **x, y and z**.

```matlab:Code
syms x y z
```

To figure out the data type of a variable you can use the **whos** function or look at the **Workspace** panel, the data type will be indicated under *Class*.

![type](https://github.com/BigKoala33/module-resources/blob/code-solutions/tutorial_sheets/Matlabsheet/Type.png)


###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco