def spiralize(number):
    n = (number - 1) // 2
    return_value = (16 * n * n * n + 30 * n * n + 26 * n + 3) // 3

    return return_value
