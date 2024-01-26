def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose operation (enter the operation number or symbol): ")

        if operation == '1' or operation == '+':
            result = add(num1, num2)
        elif operation == '2' or operation == '-':
            result = subtract(num1, num2)
        elif operation == '3' or operation == '*':
            result = multiply(num1, num2)
        elif operation == '4' or operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please choose a valid operation.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    calculator()
