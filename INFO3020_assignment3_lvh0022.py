#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Define the function name 'squareRoot' that takes the float number as the input 
def squareRoot(number):

    # Make an initial guess of any positive number.
    # I did found this good link https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html
    # To find the estimate with the rule of 2 and 7, but its too complex so I just stick with dividing the half of
    # the number input as a rule of thumb.
    estimate = number/2
    # Finding the difference between 1st formula and the next iteration
    difference = 1
    #Arbitrary number that is VERY close to zero, but greater than zero.
    epsilon = 0.0001
    # Implement the Babylonian method in the while loop to the find the square roots
    while difference > epsilon:
        # Calculate the square root using the Babylonian formula.
        iteration = (estimate + (number/estimate))/2.0
        # Find the difference between the initial guess and the next iteration using abs for the 
        # absolute value of the difference.
        difference = abs(estimate - iteration)
        # Set old value to new value
        estimate = iteration
    # Return the estimate value based on the agreement to the decimal places that was defined in the epsilon. 
    return estimate


while True:
    # Ask user to enter a positive integer.
    number = float(input("Enter a positive integer value: "))
    
    # Set error message asking for valid number if user enters something other than a positive integer.
    if number <= 0:
        print("Your number must be a positive integer. Please try again.") 
        # Use continue method to request the user for input until a valid response
        continue
    else:
        print("Value", " ", "Square Root")
        print(str(number), "   " + str(round(squareRoot(number), 3)))
        # I chose continue instead of break is to request the program to continue the loop
        continue

    


# In[ ]:





# In[ ]:




