# Matrices

 [<= Back to the Cheatsheet](../WolframCheatsheet.md)

 **IMPORTANT** You will need to have a [WolframAlpha Pro account](https://www.imperial.ac.uk/admin-services/ict/self-service/computers-printing/devices-and-software/get-software/get-software-for-students/wolfram-alpha-pro/) to use Wolfram effectively.

 Wolfram has it's [own documentation](https://www.wolframalpha.com/examples/mathematics/algebra/matrices/).

 ### Writing a Matrix
 In WolframAlpha, matrices are written with curly brackets for each horizontal row, with rows separated by commas, and a pair of curly brackets surrounding the entire matrix.

 ### Addition & Multiplication
 [Addition](https://www.wolframalpha.com/input/?i=%7B%7B2%2C+2%7D%2C+%7B3%2C+8%7D%7D+%2B+%7B%7B-2%2C+3%7D%2C+%7B1%2C+5%7D%7D), [multiplication](https://www.wolframalpha.com/input/?i=%7B%7B2%2C+2%7D%2C+%7B3%2C+8%7D%7D+.+%7B%7B-2%2C+3%7D%2C+%7B1%2C+5%7D%7D) and [scalar multiplication](https://www.wolframalpha.com/input/?i=3.%7B%7B2%2C+2%7D%2C+%7B3%2C+8%7D%7D) work pretty much as you would expect them to. Addition uses a `+` between matrices, and multiplication needs a `.` or a `*`

 ### Operations
 Finding the determinant, minors, cofactors or [inverse](https://www.wolframalpha.com/input/?i=inverse+%28%7B%7B2%2C+1%2C+2%7D%2C+%7B-2%2C+-3%2C+1%7D%2C+%7B-1%2C+-2%2C+1%7D%7D%29) of a matrix is as simple as typing `determinant`, `minors`, `cofactors` or `inverse`, followed by the matrix itself.

 ### Simultaneous Equations
 Wolfram can also [solve](https://www.wolframalpha.com/input/?i=%7B%7B2%2C+2%2C+3%7D%2C+%7B3%2C+8%2C+2%7D%2C+%7B-1%2C+2%2C+-1%7D%7D+.%7B%7Bx%7D%2C+%7By%7D%2C+%7Bz%7D%7D%3D%7B%7B20%7D%2C+%7B50%7D%2C+%7B30%7D%7D) simultaneous equations in matrix form (linear systems). You can do this, as above, by simply leaving the unknows in the matrix as letters.

 You can also solve by [rearranging the equation](https://www.wolframalpha.com/input/?i=+%7B%7Bx%7D%2C+%7By%7D%2C+%7Bz%7D%7D%3D%28inverse+%7B%7B2%2C+2%2C+3%7D%2C+%7B3%2C+8%2C+2%7D%2C+%7B-1%2C+2%2C+-1%7D%7D%29.%7B%7B20%7D%2C+%7B50%7D%2C+%7B30%7D%7D): these will give identical results. The rearrangement is computing the inverse of the matrix form with the equation coefficients, and then do a matrix-vector multiplication to obtain the solution vector. It's usually easier to let Wolfram do the algebra for you, though.