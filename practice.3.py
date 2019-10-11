def is_close(num):
    if num > 110 or num < 90:
        print("False")
    else:
        print("True")
num = int(input("Enter a number: "))
is_close(num)