def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Negative number."
    return a ** 0.5

def remainder(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a % b

def main():
    print("=== Pure Python Calculator ===")
    print("Operations:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Power (a^b)")
    print("6 - Square Root")
    print("7 - Remainder (a % b)")
    print("0 - Exit")

    while True:
        choice = input("\nChoose an operation: ")

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "6":  
            a = float(input("Enter number: "))
            print("Result:", square_root(a))
            continue

        # For all other operations, two numbers are needed
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        elif choice == "5":
            print("Result:", power(a, b))
        elif choice == "7":
            print("Result:", remainder(a, b))
        else:
            print("Invalid choice. Try again.")

main()