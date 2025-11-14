def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error: cannot divide by zero !"
    return a/b

print(" simple cli calculator")
print("-----------------")
while True:
    print("\n choose an option")
    print("1.Add(+)")
    print("2.Substract(-)")
    print("3.Multiply(*)")
    print("4.Divide(/)")
    print("5.Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("👋 Exiting calculator. Goodbye!")
        break

    # Take numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", sub(num1, num2))

    elif choice == '3':
        print("Result:", multiply(num1, num2))

    elif choice == '4':
        print("Result:", divide(num1, num2))

    else:
        print("❌ Invalid choice! Please select again.")
    