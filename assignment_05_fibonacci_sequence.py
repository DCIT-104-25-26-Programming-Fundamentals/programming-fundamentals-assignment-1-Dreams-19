def generate_fibonacci_terms(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def is_fibonacci_number(number):
    if number < 0:
        return False

    a, b = 0, 1
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b

    return False


def part_a():
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    sequence = generate_fibonacci_terms(n)
    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))


def part_b():
    number = int(input("Enter a number to check: "))

    if is_fibonacci_number(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


def main():
    part_a()
    part_b()


if __name__ == "__main__":
    main()