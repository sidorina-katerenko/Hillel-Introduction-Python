# Дан список чисел.
# Определите, сколько в этом списке элементов, которые больше двух своих соседей (слева и справа),
# и выведите количество таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.

from random import randint

lst = [randint(1, 50) for _ in range(20)]
print(lst)

bigElements = 0

for i in range(1, len(lst) - 1):
    nextEl = i + 1
    prevEl = i - 1
    if lst[i] > (lst[nextEl] + lst[prevEl]):
        bigElements += 1

print(bigElements)
