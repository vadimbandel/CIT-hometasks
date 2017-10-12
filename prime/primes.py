import math


def n_primes(n, step=10000):
    base_list = []
    for i in range(0, step):
        base_list.append([i, 0])
    for i in range(2, round(math.sqrt(step)+1)):
        j = i+1
        while j < step:
            if j % i == 0:
                base_list[j][1] = 1
                j = j+i
                while j < step:
                    base_list[j][1] = 1
                    j += i
            j += 1
    res_list = []
    for i in range(2, step):
        if base_list[i][1] == 0:
            res_list.append(base_list[i][0])
    k = 2
    while len(res_list)<n:
        base_list = []
        for i in range((k - 1) * step, k * step):
            base_list.append([i, 0])
        for prime in res_list:
            if prime > math.sqrt(k*step):
                break
            i = 1
            while i < step:
                if base_list[i][0] % prime == 0:
                    base_list[i][1] = 1
                    i = i + prime
                    while i < step:
                        base_list[i][1] = 1
                        i += prime
                i += 1
        for i in range(1, step):
            if base_list[i][1] == 0:
                res_list.append(base_list[i][0])
        k += 1
    return res_list[0:n]


print(n_primes(1000))
