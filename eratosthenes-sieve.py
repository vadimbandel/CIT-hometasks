import math


def get_prime_numbers(n):
    numbers = []
    result = []
    for i in range(n):
        numbers.append(True)

    for p in range(2, int(math.sqrt(n))):
        if not numbers[p]:
            continue
        i = 2
        while i * p < n:
            numbers[i * p] = False
            i = i + 1

    for i in range(2, n):
        if numbers[i]:
            result.append(i)

    return result


print(get_prime_numbers(100))
