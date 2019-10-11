def maximum_of_three (a,b,c):
    if a > b and a > c:
        print(a)
    if b > a and b > c:
        print(b)
    if c > a and c > b:
        print (c)
num = int(input("Enter a number: "))
numb = int(input("Enter a number: "))
numbe = int(input("Enter a number: "))
maximum_of_three(num, numb, numbe)