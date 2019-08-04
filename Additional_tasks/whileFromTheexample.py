# N = int(input('Введите число: '))
# i = 0
# while True:
#     tmp = 1
#     j = 0
#     while j < i:
#         tmp *= 2
#         j += 1
#     if tmp >= N:
#         break
#     i += 1
# print(i-1, 2**(i-1))

N = int(input('Введите число: '))
i = 0

while N >= 2:
    N /= 2
    i += 1

print(i, 2**i)
