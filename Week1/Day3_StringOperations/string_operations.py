def reverse_text(text):
    return text[::-1]


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for character in text.lower():
        if character in vowels:
            count += 1
    return count


def string_operations(text):
    return {
        "length": len(text),
        "uppercase": text.upper(),
        "lowercase": text.lower(),
        "reverse": reverse_text(text),
        "vowel_count": count_vowels(text),
    }


if __name__ == "__main__":
    text = input("Enter a string: ")
    results = string_operations(text)

    print("Length:", results["length"])
    print("Uppercase:", results["uppercase"])
    print("Lowercase:", results["lowercase"])
    print("Reverse:", results["reverse"])
    print("Vowel count:", results["vowel_count"])
