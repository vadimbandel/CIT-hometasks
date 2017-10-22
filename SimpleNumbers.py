#количество простых чисел
quantitySimpleNumbs = 1000
simpleNumbs = [False, False, True];

while quantitySimpleNumbs > 1:
    simpleNumbs.append(True)
    for i in range(2, len(simpleNumbs) - 1):
        if simpleNumbs[i]:
            if (len(simpleNumbs) - 1) % i == 0:
                simpleNumbs[len(simpleNumbs) - 1] = False
                break
    if simpleNumbs[len(simpleNumbs) - 1]:
        quantitySimpleNumbs -= 1
j = 1

#вывод простых чисел
for i in range(len(simpleNumbs)):
    if simpleNumbs[i]:
        print('#' + str(j) + ' = ' + str(i))
        j += 1