def character_frequency(text):
    frequencies = {}

    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1

    return frequencies


if __name__ == "__main__":
    text = input("Enter a string: ")
    frequencies = character_frequency(text)

    print("Character frequencies:")
    for character, count in frequencies.items():
        print(f"{character!r}: {count}")
