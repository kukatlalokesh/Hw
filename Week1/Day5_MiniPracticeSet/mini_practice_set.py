def count_even_numbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def find_largest(numbers):
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)


if __name__ == "__main__":
    numbers = [12, 7, 4, 19, 22, 9]
    print("Problem 1 - Even count:", count_even_numbers(numbers))

    print("Problem 2 - Largest:", find_largest(numbers))

    sentence = "Python makes coding fun"
    print("Problem 3 - Reversed words:", reverse_words(sentence))
