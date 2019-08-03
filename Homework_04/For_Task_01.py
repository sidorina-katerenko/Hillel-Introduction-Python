# Даны два целых числа A и В.
# Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
# или в порядке убывания в противном случае.

A = int(input('Введите целое число А: '))
B = int(input('Введите целое число B: '))

stopValue = B + 1
stepValue = 1

if A > B:
    stopValue = B - 1
    stepValue = -1

for i in range(A, stopValue, stepValue):
    print(i)
