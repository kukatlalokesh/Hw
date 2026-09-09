def is_palindrome(text):
    reversed_text = ""

    for index in range(len(text) - 1, -1, -1):
        reversed_text += text[index]

    return text == reversed_text


if __name__ == "__main__":
    text = input("Enter text: ")
    print("Palindrome" if is_palindrome(text) else "Not a palindrome")
