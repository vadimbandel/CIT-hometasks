def get_prime_numbers(n):
    prime_numbers = [2]
    current_num = 3
    while len(prime_numbers) < n:
        divider = 3
        flag = True
        while divider < current_num:
            if current_num % divider == 0:
                flag = False
                break
            divider = divider + 1
        if flag:
            prime_numbers.append(current_num)
        current_num = current_num + 2
    return prime_numbers


print(get_prime_numbers(100))
