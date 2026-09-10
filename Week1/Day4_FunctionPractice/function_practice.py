def square(number):
    return number * number


def cube(number):
    return number * number * number


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(1, number + 1):
        result *= value
    return result


def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    print("Square:", square(5))
    print("Cube:", cube(3))
    print("Factorial:", factorial(5))
    print("Simple Interest:", simple_interest(1000, 5, 2))
