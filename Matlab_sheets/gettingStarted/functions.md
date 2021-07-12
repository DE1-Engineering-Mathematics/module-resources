# Functions

In order to call functions you must surround them with "**( )**".
```matlab:Code
A = [1 3 7];
max(A)
```

If there are more than one argument, they are separated with commas.
```matlab:Code
B= [10 5 2];
max(A,B)
```

You can assign the output of a function to a variable
```matlab:Code
maxA = max(A)
```

Sometimes there might be more than one output to a function, they should be *received* in a row vector form.
```matlab:Code
[maxA location] = max(A)
```

Strings are enclosed in " or ', like to other programming languages.

```matlab:Code
text = "Hello World";
```

Finally, some functions do not have input arguments, like **clc**. They are simply typed on the command line.
```matlab:Code
clc
```


###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco