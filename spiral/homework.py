def spiralize(number):
    n = (number - 1) // 2
    return_value = (8 * n * (n + 1) * (2 * n + 1)) // 3 + 2 * n * (n + 1) + 4 * n + 1

    return return_value
