def pattern_one(rows):
    print("Pattern 1")
    for row in range(1, rows + 1):
        for _ in range(row):
            print("*", end=" ")
        print()


def pattern_two(rows):
    print("\nPattern 2")
    for row in range(1, rows + 1):
        for _ in range(rows - row):
            print(" ", end=" ")
        for _ in range(row):
            print("*", end=" ")
        print()


def pattern_three(rows):
    print("\nPattern 3")
    for row in range(1, rows + 1):
        for _ in range(rows - row):
            print(" ", end=" ")
        for _ in range(2 * row - 1):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    rows = 5
    pattern_one(rows)
    pattern_two(rows)
    pattern_three(rows)
