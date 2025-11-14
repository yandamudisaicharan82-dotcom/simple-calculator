# simple-calculator
1. Functions for operations
2. Each mathematical action is stored in its own function:
def add(a, b): return a + b
This keeps the code clean and organized.
2. Infinite loop
The calculator keeps running until the user chooses Exit.
while True:
3. Asking user for operation
User types:
1 for add
2 for subtract
3 for multiply
4 for divide
5 for exit
4. Taking number inputs
Two numbers are collected:
num1 = float(input("Enter first number: "))
5. Performing the calculation
Based on the user’s choice, the correct function is called:
print("Result:", add(num1, num2))
6. Exiting the program
When the user types 5, the loop breaks and the calculator stops.
