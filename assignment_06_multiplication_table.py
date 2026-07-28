def print_single_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:<2} =  {number * i}")


def print_tables_up_to_n(n):
    for number in range(1, n + 1):
        print_single_table(number)
        if number != n:
            print("---------------------------")


def part_a():
    number = int(input("Enter a number: "))
    print_single_table(number)


def part_b():
    n = int(input("Enter N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print_tables_up_to_n(n)


def main():
    part_a()
    print()
    part_b()


if __name__ == "__main__":
    main()