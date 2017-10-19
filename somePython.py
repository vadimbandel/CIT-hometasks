primes = [2] 
s = 3
while len(primes) < 1000:
    for item in primes: 
        if s%item == 0: 
            break 
    else:
        primes.append(s) 
    s +=1 
print(primes) 
print(len(primes))
