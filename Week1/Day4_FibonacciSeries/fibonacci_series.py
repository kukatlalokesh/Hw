def fibonacci_series(terms):
    """Generate the Fibonacci series for the requested number of terms."""
    if terms <= 0:
        return []

    series = []
    first, second = 0, 1

    # Each loop adds the current value, then shifts to the next pair.
    for _ in range(terms):
        series.append(first)
        first, second = second, first + second

    return series


if __name__ == "__main__":
    number_of_terms = int(input("Enter the number of terms: "))
    print("Fibonacci series:", fibonacci_series(number_of_terms))
