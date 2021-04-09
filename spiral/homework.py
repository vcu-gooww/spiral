def spiralize(number):
    n = 1
    step = 2
    total = 0
    since_last = 0
    while n <= size**2:
    total += n
    n += step
    since_last += 1
    if since_last == 4:
    step +=2
    since_last = 0
    return total
print(sprialize(501))

