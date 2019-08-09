# Дан словарь ключами которого являются английские слова, а занчениями - списки латинских слов.
# Необходимо развеннуть словарь. Другими словани, необходимо, на основании заданного словаря, создать новый словарь,
# у которого в качестве ключей будут взяты латинские слова, из первого словаря,
# а значениями будут, соответствующие им, английские слова.

# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa

from pprint import pprint as p

ourDictionary = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa'],
}

p(ourDictionary)
j = list()

for i in ourDictionary.keys():
    j.extend(ourDictionary[i])

newList = set(j)

print(newList)

print('======================')

newDict = {}

for whatWeNeed in newList:
    for key, value in ourDictionary.items():
        if whatWeNeed in value:
            newDict.setdefault(whatWeNeed, []).append(key)

p(newDict)



