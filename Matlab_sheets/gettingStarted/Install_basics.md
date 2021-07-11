# Getting Started with MATLAB
## Installation (Windows & Mac)
1. First you need to create a [Mathworks](https://uk.mathworks.com/login) account using your long imperial email (e.g. name.surname21@imperial.ac.uk).
1. Mathworks will recognise your Imperial email and ask you to log in from through the Imperial portal.
1. Finalise the creation of your Mathworks account.
1. Mathworks should have granted an **educational** Matlab license, you should be able to download and install it as you would normally expect.
## Interface
When you first install Matlab, your interface should look like this, it should have **3 main panels**.

![interface](https://github.com/BigKoala33/module-resources/blob/code-solutions/tutorial_sheets/gettingStarted/Interface.png)

**Current folder**, on this panel you can view and access your files.

![current](https://github.com/BigKoala33/module-resources/blob/code-solutions/tutorial_sheets/gettingStarted/Current.png)

**Command Window**, on this panel you can enter commands and interact with variables in real-time. This panel is where most of the action will happen!

![command window](https://github.com/BigKoala33/module-resources/blob/code-solutions/tutorial_sheets/gettingStarted/Command.png)

**Workspace**, on this panel you can see all your declared variables, their type and their value.

![workspace](https://github.com/BigKoala33/module-resources/blob/code-solutions/tutorial_sheets/gettingStarted/Workspace.png)

## Declaring variables and basic operations
### Declare variables
The following command will create a variable called **a** with the value of 34
```matlab:Code
a = 34
```
Many more variables can be created
```matalb:Code
b = 21
```
These variables can be used to create new variables!
```matlab:Code
c = a + b
c =
    55
```
### Basic Operators
- Addition "+"
- Substraction "-"
- Multiplication "*"
- Division "/"
- Power "^"

These can be used to create all sort of operations:
```matlab:Code
d = (a * b)/c
d = 
    12.9818
```

### Useful information
- If you finish your command with a **";"** the result will not be displayed.
- When Matlab does an operation without declaring a variable, the result gets stored in a variable called **ans**, exactly like physical calculators do!

```matlab:Code
45 - 67
ans = 
    -22
```

- Pressing the **up and down arrows** on the command line will allow you to "recall" commands, give this a try to understand it.
- Press **tab** to autocomplete commands.
- To delete variables from the workspace use the **clear** command, **clear all** will delete all of the variables.
```matlab:Code
clear a b c d
```
- Use **clc** to clear the Command panel and keep things tidy.

###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco