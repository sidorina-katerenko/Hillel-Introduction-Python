# таблица умножения вложенными циклами

for i in range(2, 10):
    for j in range(2, 6):
        print('{} * {} = {}'.format(j, i, i * j), end='\t')
    print()

print()

for i in range(2, 10):
    for j in range(6, 10):
        print('{} * {} = {}'.format(j, i, i * j), end='\t')
    print()

# зато сама! :D
