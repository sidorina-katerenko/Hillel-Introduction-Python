# N = int(input('Введите число: '))
#
# tmp = 1
#
# e = 10000000000000000000000
# for i in range(e):
#     tmp *= 2
#     if tmp > N:
#         print(i, tmp//2)
#         break

N = int(input('Введите число: '))

i = 0
tmp = 1

for _ in range(N):
    tmp *= 2
    i += 1
    if tmp > N:
        print(i - 1, 2**(i - 1))
        break
