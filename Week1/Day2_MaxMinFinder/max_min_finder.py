numbers = [12, 5, 27, 3, 19, 8]

largest = numbers[0]
smallest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Numbers:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
