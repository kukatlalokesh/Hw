def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"


students = {
    "Alice": [85, 90, 88],
    "Bob": [72, 68, 75],
    "Charlie": [95, 92, 96],
    "Diana": [81, 79, 84],
    "Ethan": [58, 64, 61],
}

for student, marks in students.items():
    average = calculate_average(marks)
    grade = calculate_grade(average)
    print(f"{student}: Average = {average:.2f}, Grade = {grade}")
