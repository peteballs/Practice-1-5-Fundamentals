def squares(n):
    square_list = []
    for i in range(n+1):
        square_list.append(2 ** i)
    return square_list
print(squares (20))