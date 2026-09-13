FILE_NAME = "sample.txt"


def write_file():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write("This is the first line.\n")
        file.write("Python file handling practice.\n")


def append_file():
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write("This line was added using append mode.\n")


def read_file():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    write_file()
    print("After write:")
    print(read_file())

    append_file()
    print("After append:")
    print(read_file())
