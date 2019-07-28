# В математике функция sign(x) (знак числа) определена так:
# sign(x) = 1, если x > 0, sign(x) = -1, если x < 0, sign(x) = 0, если x = 0.
#
# Для данного числа x выведите значение sign(x).
# Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.

x = int(input('Введите X: '))

if x > 0:
    result = 1
elif x < 0:
    result = -1
else:
    result = 0

print('sign(', x, ') = ', result, sep='')