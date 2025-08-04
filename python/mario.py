def main():
    print_column1(3)
    print_column2(6)

    print_row(5)

    print_square(9)

def print_column1(height):
    for _ in range (height):
        print("#")
    print()


def print_column2(height):
    print("#\n" * height, end ="\n")
    

def print_row(width):
    print("?" * width, end = "\n") #pythonic way
    print()

def print_square (size):
    for i in range (size): #represents each row
        print("#" * size)

main()