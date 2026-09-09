def is_even(number):
    return number % 2 == 0


def check_numbers(numbers):
    for number in numbers:
        result = "even" if is_even(number) else "odd"
        print(f"{number} is {result}.")


if __name__ == "__main__":
    numbers = []
    for index in range(5):
        numbers.append(int(input(f"Enter number {index + 1}: ")))
    check_numbers(numbers)
