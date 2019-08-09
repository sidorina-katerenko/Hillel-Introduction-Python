# В единственной строке записан текст.
# Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.

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
