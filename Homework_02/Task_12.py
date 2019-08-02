# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!)
# Первая строка содержит следующее значение, а вторая строка содержит предыдущее значение введёного числа

n = int(input('Please enter an integer number: '))

print('The next number for the number {} is {}.'.format(n, n + 1), sep='')
print('The previous number for the number {} is {}.'.format(n, n - 1), sep='')
