def spiralize(number):
    n = (number - 1) // 2
    x = (8 * n * (n + 1) * (2*n+1)) / 3 + 2 * n * (n + 1) + 4 * n + 1
    return x

print(spiralize(501)) 
