import math

def square_root(x):
    if x < 0:
        print("Error: Cannot compute the square root of a negative number.")
        return None
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        print("Error: Factorial of a negative number is undefined.")
        return None
    try:
        x_int = int(x)
        if x != x_int:
            print("Note: Factorial accepts only integers. Converting input to", x_int)
        return math.factorial(x_int)
    except OverflowError:
        print("Error: The result is too large to compute.")
        return None

def natural_log(x):
    if x <= 0:
        print("Error: Natural log is undefined for zero or negative numbers.")
        return None
    return math.log(x)

def power_function(x, b):
    return math.pow(x, b)

def main():
    while True:
        print("\nScientific Calculator Menu:")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            try:
                x = float(input("Enter a number: "))
                result = square_root(x)
                if result is not None:
                    print("Square root of", x, "is", result)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            try:
                x = float(input("Enter a number: "))
                result = factorial(x)
                if result is not None:
                    print("Factorial of", int(x), "is", result)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            try:
                x = float(input("Enter a number: "))
                result = natural_log(x)
                if result is not None:
                    print("Natural logarithm of", x, "is", result)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            try:
                x = float(input("Enter the base (x): "))
                b = float(input("Enter the exponent (b): "))
                result = power_function(x, b)
                print(f"{x} raised to the power {b} is {result}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()