def is_opposite(a, b):
    if a > 0 and b < 0 or a < 0 and b > 0:
        print("True")
    else:
        print("False")
num = int(input("Enter a number: "))
numb = int(input("Enter another number: "))
is_opposite(num, numb)