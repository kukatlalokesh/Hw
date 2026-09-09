def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def calculate_average(numbers):
    if not numbers:
        return 0
    return calculate_sum(numbers) / len(numbers)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    total = calculate_sum(numbers)
    average = calculate_average(numbers)

    print("Numbers:", numbers)
    print("Sum:", total)
    print("Average:", average)
