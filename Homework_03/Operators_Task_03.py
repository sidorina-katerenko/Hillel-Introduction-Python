# Дано трехзначное число. Найдите сумму его цифр.

X = int(input('Введите трехзначное число: '))

totalSum = X % 10
X //= 10
totalSum += X % 10
X //= 10
totalSum += X % 10

print(totalSum)
