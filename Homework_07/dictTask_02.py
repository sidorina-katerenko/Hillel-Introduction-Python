# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите все, которые подходят по условию задачи.
# Задачу необходимо решить с использованием словаря.

from pprint import pprint as p

textToWorkWith = input('Введите текст: ')
textToWorkWith = textToWorkWith.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(
                                        ';', '').replace(':', '')
listedText = list(textToWorkWith.split())

print(listedText)

ourDictionary = dict.fromkeys(listedText)

for i in ourDictionary.keys():
    j = listedText.count(i)
    ourDictionary[i] = j

p(ourDictionary)
mostOftenWords = list()

for key, value in ourDictionary.items():
    if value == max(ourDictionary.values()):
        mostOftenWords.append(key)

print('Чаще всего встречаются слова: ', mostOftenWords)
