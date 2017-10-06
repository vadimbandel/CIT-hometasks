k = 1
primes = 0
n = 1000
while primes < n:
    count = 0
    for i in range(1, k+1):
        if k % i == 0:
            count+=1#подсчитываем делители для каждого числа
        if count>2:
            break
    if count ==2:#если два делителя
        print(k)
        primes+=1
    k+=1