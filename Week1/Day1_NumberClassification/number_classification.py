def classify_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    return "zero"


if __name__ == "__main__":
    value = float(input("Enter a number: "))
    print(f"The number is {classify_number(value)}.")
