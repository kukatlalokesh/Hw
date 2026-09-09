def calculate(first, second, operator):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError("Invalid operator. Use +, -, *, or /.")


if __name__ == "__main__":
    print("Simple Calculator")
    print("Enter q at any prompt to exit.")

    while True:
        first_input = input("Enter first number: ").strip()
        if first_input.lower() == "q":
            break

        second_input = input("Enter second number: ").strip()
        if second_input.lower() == "q":
            break

        operator = input("Enter operation (+, -, *, /): ").strip()
        if operator.lower() == "q":
            break

        try:
            first = float(first_input)
            second = float(second_input)
            result = calculate(first, second, operator)
            print(f"Result: {result}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"Invalid input: {error}")
