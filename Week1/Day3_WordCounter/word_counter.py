sentence = input("Enter a sentence: ")
words = sentence.split()

print("Word count:", len(words))

for word in words:
    print(f"{word}: {len(word)} characters")
