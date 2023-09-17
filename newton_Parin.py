# Modify the code below
"""
Program: newton.py
Author: Ken
Compute the square root of a number.
1. The input is a number.
2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""
import math
def improveEstimate(old_estimate, x):
    ans = (old_estimate + x / old_estimate) / 2
    #print("Ans improve = ", ans)
    return ans 
def limitReached(old_estimate, new_estimate):
    tolerance = 1e-6
    ans = abs(old_estimate - new_estimate) < tolerance
    return ans
def newton(x):
    x0 = x/2
    x1 = x/2
    while True:
        x0 = x1
        x1 = improveEstimate(x0,x)
        #print("x1 improve", x1)
        if limitReached(x0,x1):
            #print("inside")
            #print(x0, x1 ,x)
            break
    #print(x0, x1 ,x)
    return x0

def main():
#################################333# Receive the input number from the user
    while True:
        x = float(input("Enter a positive number: "))
    # Initialize the tolerance and estimate
    #tolerance = 0.000001
    #estimate = 1.0
    
# Perform the successive approximations
#while True:
 #    estimate = (estimate + x / estimate) / 2
  #   difference = abs(x - estimate ** 2)
   #  if difference <= tolerance:
    #     break
        if x == '':
            break
        x = float(x)
        if x < 0:
            print("Error : Please enter Postive number.")
        else:
            estimated_sqrt = newton(x)
            print()
            print('The program\'s estimate is ',estimated_sqrt)
            print('Python\'s estimate is ',math.sqrt(x))
                        
if __name__ == "__main__":
    main()

