# Root finding

In the following example it will be shown how to create a Matlab script for the Root finding **Newton-Rapson method**. I personally encourage you to try and create scripts for the other two root-finding methods.

1. First define the function you want to analyse and their respective derivative.(This method requires the [Symbolic Math Toolbox](https://uk.mathworks.com/products/symbolic.html), it is possible to do it without but it is much quicker)

    ```matlab:Code
    f = @(x) x^2+4 - x^3;
    dfdx = diff(f,x)
    ```
2. Then declare the initial guess of your root and the number of trials.
    ```matlab:Code
    int_guess = 3;
    number_trials = 20
3. Before starting the loop we need to calculate the first guess of the approximation.
    ```matlab:Code
    root = int_guess - f(int_guess)/dfdx(int_guess)
    ```
4. Finally create a loop and perform the algorythm for the number of trials and display the root.
    ```matlab:Code
    for i = 1:number_trials
        root = root - f(double(root))/dfdx(double(root));
        double(root)
    end
    ```



###### Dyson School of Design Engineering 2021 - Ivan Revenga Riesco