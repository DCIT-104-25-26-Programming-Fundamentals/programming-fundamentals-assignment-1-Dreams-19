def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(a, b):
    return a ** b


def get_two_numbers():
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    return a, b


def print_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", power),
    }

    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Error: Invalid choice. Please enter a number between 1 and 7.")
            print()
            continue

        symbol, operation = operations[choice]
        a, b = get_two_numbers()

        if choice in ("4", "5") and b == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = operation(a, b)
            print(f"Result: {a:g} {symbol} {b:g} = {result:g}" if isinstance(result, float) else f"Result: {a:g} {symbol} {b:g} = {result}")

        print()


if __name__ == "__main__":
    main()