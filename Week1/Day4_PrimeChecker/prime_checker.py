def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


if __name__ == "__main__":
    test_values = [1, 2, 3, 4, 17, 20, 29, 30]

    for number in test_values:
        result = "prime" if is_prime(number) else "not prime"
        print(f"{number} is {result}.")
